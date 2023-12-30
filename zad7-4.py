from faker import Faker
import random
from datetime import date

today = date.today()
fake = Faker()


class Movie:
    def __init__(self, title, year, genre, views):
        self.title = title
        self.year = int(year)
        self.genre = genre
        self.views = int(views)

    def play(self, step=1):
        self.views += step

    def __str__(self):
        return f"{self.title} ({self.year}) {self.views}"


class Series(Movie):
    def __init__(self, episode, sezon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = str(episode).zfill(2)
        self.sezon = str(sezon).zfill(2)

    def __str__(self):
        return f"{self.title} S{self.sezon}E{self.episode} {self.views}"


def get_show(data, needed_class):
    show = [i for i in data if type(i) is needed_class]
    show.sort(key=lambda p: p.title)
    return show


def get_series(data):
    return get_show(data, Series)


def get_movies(data):
    return get_show(data, Movie)


def search(data):
    word = input("Jaki film/serial? ")
    for x in data:
        if x.title == word:
            print(x)


def generate_views(data):
    ran = random.choice(data)
    ran.views += random.choice(range(1, 101))


def gen10times(data):
    for j in range(10):
        generate_views(data)


def top_titles(data):
    quantity = int(input("Ile filmów/seriali chcesz? "))
    ser = data
    ser.sort(key=lambda p: p.views, reverse=True)
    for i in ser[:quantity]:
        print(i)


def add_series(data):
    while True:
        title1 = input("Podaj tytuł: ")
        while True:
            year1 = input("Podaj rok produkcji: ")
            if len(year1) == 4:
                break
        genre1 = input("Podaj gatunek: ")
        sezon1 = input("podaj numer sezonu: ")
        episode1 = input("Podaj liczbe odcinków do dodania: ")
        data.append(
            Series(
                title=title1,
                year=year1,
                genre=genre1,
                views=0,
                episode=episode1,
                sezon=sezon1,
            )
        )
        end = input("Czy to wszystko? napisz 'tak' lub 'nie' ")
        if end == "tak":
            break


def show(data):
    print("\nSeriale:")
    for i in get_series(data):
        print(i)
    print("\nFilmy:")
    for i in get_movies(data):
        print(i)


def main():
    vid = Movie(title="Pulp Fiction", year="1994", genre="comedy", views=200)

    ser = Series(
        title="The Simpsons", year="1998", genre="comedy", views=100, episode=1, sezon=2
    )

    doc = []

    for i in range(10):
        doc.append(
            Series(
                title="The Simpsons",
                year="1998",
                genre="comedy",
                views=fake.random_number(digits=2),
                episode=i,
                sezon=1,
            )
        )

    for i in range(5):
        doc.append(
            Movie(
                title=fake.sentence(nb_words=3),
                year=fake.year(),
                genre=fake.emoji(),
                views=fake.random_number(digits=2),
            )
        )
        doc.append(
            Series(
                title=fake.sentence(nb_words=3),
                year=fake.year(),
                genre=fake.emoji(),
                views=fake.random_number(digits=2),
                episode=fake.random_number(digits=2),
                sezon=fake.random_number(digits=1),
            )
        )

    doc.append(vid)
    doc.append(ser)

    vid.play()
    ser.play()

    print("Biblioteka filmów")
    show(doc)
    generate_views(doc)
    print()
    show(doc)
    print()
    print(f"Najpopularniejsze filmy i seriale dnia {today} to:")
    top_titles(doc)
    search(doc)


if __name__ == "__main__":
    main()
