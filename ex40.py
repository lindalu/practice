class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print "Sing: %s" % line
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                   
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
                        
lcd_lines = ["Where", "are", "your", "friends", "tonight"]
lcd = Song(lcd_lines)
print ' '.join(lcd_lines)
print '''
'''

happy_bday.sing_me_a_song()

print''

bulls_on_parade.sing_me_a_song()

print ''

lcd.sing_me_a_song()

print '''
'''
