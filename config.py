# UI  тесты
MAIN_URL = 'https://www.kinopoisk.ru/'
TITLE = ('Кинопоиск. Онлайн кинотеатр. '
         'Фильмы сериалы мультфильмы и энциклопедия')

# API  тесты
BASE_URL = "https://api.kinopoisk.dev/v1.4"
API_KEY = "PQN92YB-YNNM8WF-PZAQ11R-KPH6TNM"

# Тестовые данные
VALID_SEARCHES = [
    "Ищейка",
    "Весна на заречной улице",
    "Ёлки 12"
]
VALID_MOVIE_ID = 841048
EMPTY_QUERY = ""
INVALID_QUERY = "а-а"
SPECIAL_CHARS_QUERY = ":**(\"№%_)(*%!\"№_)*?:%%;!;%%:"
RUSSIAN_NO_SPACES = "веснаназаречнойулице"
INVALID_MOVIE_ID = 9999999999
