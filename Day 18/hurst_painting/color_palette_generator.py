import colorgram

color_palette = []

# Extract 6 colors from an image.
colors = colorgram.extract('hurst.jpg', 30)

# extract and append colors to list
for _ in colors:
    color_r = _.rgb.r
    color_g = _.rgb.g
    color_b = _.rgb.b
    new_color = (color_r, color_g, color_b)

    color_palette.append(new_color)

print(color_palette)