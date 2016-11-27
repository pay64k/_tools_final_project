import prediction
import load_dataset

prediction.movies_data = load_dataset.read_from_file('prediction/static/prediction/dataset/imdb_dataset_v6.0.2_3_actors_complete.tsv', 3)