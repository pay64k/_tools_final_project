import csv


def read_from_file(file, actors_amount):

    if actors_amount == 6:

        movies = {}

        with open(file) as csvfile:
            reader = csv.DictReader(csvfile, delimiter="\t")
            for entry in reader:
                movies[
                    entry["title"]
                ] = {
                    "director": entry["director"],
                    "rating": entry["rating"],
                    "votes": entry["votes"],
                    "year": entry["year"],
                    "genre": entry["genre"],
                    "gross": entry["gross"],
                    "budget": entry["budget"],
                    "run-time": entry["run-time"],
                    "actor1": entry["actor1"],
                    "actor1_rank": entry["actor1_rank"],
                    "actor1_sex": entry["actor1_sex"],
                    "actor2": entry["actor2"],
                    "actor2_rank": entry["actor2_rank"],
                    "actor2_sex": entry["actor2_sex"],
                    "actor3": entry["actor3"],
                    "actor3_rank": entry["actor3_rank"],
                    "actor3_sex": entry["actor3_sex"],
                    "actor4": entry["actor4"],
                    "actor4_rank": entry["actor4_rank"],
                    "actor4_sex": entry["actor4_sex"],
                    "actor5": entry["actor5"],
                    "actor5_rank": entry["actor5_rank"],
                    "actor5_sex": entry["actor5_sex"],
                    "actor6": entry["actor6"],
                    "actor6_rank": entry["actor6_rank"],
                    "actor6_sex": entry["actor6_sex"],
                    # "plot": entry["plot"]
                }
        return movies

    if actors_amount == 3:

        movies = {}

        with open(file) as csvfile:
            reader = csv.DictReader(csvfile, delimiter="\t")
            for entry in reader:
                movies[
                    entry["title"]
                ] = {
                    "director": entry["director"],
                    "rating": entry["rating"],
                    "votes": entry["votes"],
                    "year": entry["year"],
                    "genre": entry["genre"],
                    "gross": entry["gross"],
                    "budget": entry["budget"],
                    "run-time": entry["run-time"],
                    "actor1": entry["actor1"],
                    "actor1_rank": entry["actor1_rank"],
                    "actor1_sex": entry["actor1_sex"],
                    "actor2": entry["actor2"],
                    "actor2_rank": entry["actor2_rank"],
                    "actor2_sex": entry["actor2_sex"],
                    "actor3": entry["actor3"],
                    "actor3_rank": entry["actor3_rank"],
                    "actor3_sex": entry["actor3_sex"],
                    # "plot": entry["plot"]
                }
        return movies