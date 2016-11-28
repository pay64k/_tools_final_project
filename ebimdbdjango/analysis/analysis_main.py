from prediction import prediction
from operator import itemgetter

movies_data = prediction.movies_data


def find_grossing_movies():
    gross = []
    for title in movies_data:
        gross.append([title,float(movies_data[title]["gross"])])
    result = sorted(gross, key=itemgetter(1), reverse=True)

    return result

# find_grossing_movies()