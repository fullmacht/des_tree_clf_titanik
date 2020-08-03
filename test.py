import pandas as pd
import numpy as np

# from tqdm.notebook import tqdm

from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer


desired_width=320
pd.set_option('display.width', desired_width)
# np.set_printoption(linewidth=desired_width)
pd.set_option('display.max_columns',30)


links = pd.read_csv(r'C:\Users\laptop\PycharmProjects\des_tree_clf_titanik\Classwork\data\links.csv')
movies = pd.read_csv(r'C:\Users\laptop\PycharmProjects\des_tree_clf_titanik\Classwork\data\movies.csv')
ratings = pd.read_csv(r'C:\Users\laptop\PycharmProjects\des_tree_clf_titanik\Classwork\data\ratings.csv')
tags = pd.read_csv(r'C:\Users\laptop\PycharmProjects\des_tree_clf_titanik\Classwork\data\tags.csv')
# print(ratings.head())
ratings = ratings.drop(['timestamp','userId'],axis=1)
data = pd.merge(movies,tags, left_on='movieId',right_on='movieId')
data = pd.merge(data,ratings, left_on='movieId',right_on='movieId')
data = data.drop(['userId','timestamp'],axis=1)
print(data.head())
# def change_string(s):
#     return ' '.join(s.replace(' ', '').replace('-', '').split('|'))
#
# movie_genres = [change_string(g) for g in data.genres.values]

# movies_with_tags = movies.join(tags.set_index('movieId'), on='movieId')
# print(movies_with_tags.head())
data.dropna(inplace=True)

tag_strings = []
movies = []
movie_genres = []
# print(data.head())
def gen():
    for k in data.genres.values:
        movie_genres.append(' '.join(str(k).replace(' ', '').replace('-', '').split('|')))
for movie, group in data.groupby('title'):
    gen()
    tag_strings.append(' '.join([str(s).replace(' ', '').replace('-', '') for s in group.tag.values]))
    movies.append(movie)

# print(movie_genres[:10])
# print(tag_strings[:10])
# print(movies[:10])