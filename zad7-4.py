from faker import Faker
import random
from datetime import date
today = date.today()
fake=Faker()
class movie:
    def __init__(self, title, year, genre, views ):
        self.title = title
        self.year = int(year)
        self.genre = genre
        self.views = int(views)
    def play(self, step = 1):
       self.views += step
    def __str__(self):
       return f"{self.title} ({self.year}) {self.views}"
   
class series(movie):
    def __init__(self,episode, sezon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = str(episode)
        self.sezon = str(sezon)
    def __str__(self):
        self.sezon = self.sezon.zfill(2)
        self.episode = self.episode.zfill(2)
        
        return f"{self.title} S{self.sezon}E{self.episode} {self.views}"
    
def get_series(data):
    ser=[]
    for i in data:
        if issubclass(type(i), series)==True:    
            ser.append(i)
    by_title=sorted(ser, key=lambda p:p.title)
    for i in by_title:
        print(i)
        
def get_movies(data):
    mov=list(data)
    for i in data:
        if issubclass(type(i), series)==True:    
            mov.remove(i)
    by_title=sorted(mov, key=lambda p:p.title)
    for i in by_title:
        print(i)

def search(data):
    word=input("Jaki film/serial? ")
    any(print(x) for x in data if x.title == word)

def generate_views(data):
    ran=random.choice(data)
    for i in data:
        if i == ran:
            i.views += random.choice(range(1, 101))

def gen10times(data):
    for j in range(10):
        generate_views(data)

def top_titles(data):
    ilosc = int(input("Ile filmów/seriali chcesz? "))
    ser = []
    for i in data:
        ser.append(i)
    by_views=sorted(ser, key=lambda p:p.views, reverse=True)
    for i in by_views[0:ilosc]:
        print(i)
        
def add_thing(data):
    while True: 
        title1 = input("Podaj tytuł: ")
        while True:
            year1 = input("Podaj rok produkcji: ")
            if len(year1)==4:
                break
        genre1 = input("Podaj gatunek: ")
        sezon1 = input("podaj numer sezonu: ")
        episode1 = input("Podaj liczbe odcinków do dodania: ")
        data.append(series(title=title1, year=year1, genre=genre1, views=0, episode=episode1, sezon=sezon1))
        end = input("Czy to wszystko? napisz \"tak\" lub \"nie\" ")
        if end == "tak":
            break
def show(data):
    for i in data:
        print(i)

    
vid=movie(title="Pulp Fiction", year="1994", genre="comedy", views=200)
ser=series(title="The Simpsons", year="1998", genre="comedy", views=100, episode=10, sezon=1)
both=[vid]+[ser]

vid.play()



ser.play()



doc=[]
for i in range(10):
    doc.append(movie(title=fake.sentence(nb_words=3), year=fake.year(), genre=fake.emoji(), views=fake.random_number(digits=2)))
    doc.append(series(title=fake.sentence(nb_words=3), year=fake.year(), genre=fake.emoji(), views=fake.random_number(digits=2), episode=fake.random_number(digits=2), sezon=fake.random_number(digits=1)))
doc.append(vid)
doc.append(ser)



print("Biblioteka filmów")
show(both)
generate_views(both)
print()
show(both)
print(f"Najpopularniejsze filmy i seriale dnia {today} to:")
top_titles(doc)

#search(doc)