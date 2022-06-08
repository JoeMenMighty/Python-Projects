import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_PRICE_API_KEY = "XMT39CXIC1UF6697"
NEWS_API_KEY = "dd90ab5084724831a65648194fe8c381"
TWILIO_ACCOUNT_SID = "ACdac96ba682b9a88e632348bd07006ee1"
TWILIO_AUTH_TOKEN = "0a79b68fc415edebc5c57429f0f1b776"


# twillio message function
def send_sms(msg):
    # send sms using twillio
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=msg,
            from_='+17163034273',
            to='+233501588573'
        )

    print(message.status)


def construct_message(percent):
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_url = "https://newsapi.org/v2/everything"
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
        'q': COMPANY_NAME
    }
    news_response = requests.get(url=news_url, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]
    # construct news
    relevant_news = ""
    for news in news_data:
        news_source = news['source']['name']
        news_heading = news['title']
        news_description = news['description']
        news_content = news['content']

        final = f"\nSource: {news_source} \nTitle: {news_heading} \nBrief: {news_description}\n"
        relevant_news += final
    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    if percentage_difference > 0:
        sign = "🔺"
    else:
        sign = "🔻"
    stock_msg = f"TSLA: {sign}{percent}%\n{relevant_news}"
    return stock_msg


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_url = "https://www.alphavantage.co/query"
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_PRICE_API_KEY
}
stock_response = requests.get(url=stock_url, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']

last_2_days_price = float(list(stock_data.items())[0][1]['4. close'])
yesterday_price = float(list(stock_data.items())[1][1]['4. close'])

percentage_difference = round(((yesterday_price - last_2_days_price) / last_2_days_price) * 100, 4)


if abs(percentage_difference) >= 3:
    send_sms(construct_message(percent=percentage_difference))
