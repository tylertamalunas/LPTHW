class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

apple_bottom_jeans = Song(["Shake that ass for me",
                            "Shake that ass for me",
                            "C'mon girl, shake that ass"])

twinkle = ["Twinkle twinkle little star"]

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

apple_bottom_jeans.sing_me_a_song()

twinkle_twinkle =  Song(twinkle)
twinkle_twinkle.sing_me_a_song()
