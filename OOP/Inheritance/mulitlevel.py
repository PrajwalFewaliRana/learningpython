class Books:
    @staticmethod
    def like():
        print("I like to read books")

class Genre(Books):
    def __init__(self,genre):
        self.genre = genre
        
class Book_name(Genre):
    def __init__(self,name):
        self.name = name
s1= Book_name("RichDad and Poor Dad")
print(s1.name)
print(s1.like())