class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


mighty = User('1123', 'mightyman')
kofi = User('1023', 'Kofi')
ama = User('1113', 'Amakay')
prisca = User('1103', 'Pricy1_')

mighty.follow(kofi)
mighty.follow(ama)
mighty.follow(prisca)

kofi.follow(mighty)
kofi.follow(ama)

print(mighty.followers)
print(mighty.following)

print(kofi.followers)
print(kofi.following)
