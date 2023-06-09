# In[1]:
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
# In[2]:
movies = pd.read_csv("mrs_main/movies.csv")

# In[3]:
new_df = movies
# In[4]:
cv = CountVectorizer(stop_words="english", max_features=5000)
# In[5]:
vectors = cv.fit_transform(new_df["tags"]).toarray()
# In[6]:
similarity = cosine_similarity(vectors)


# In[7]:
def recommend(movie):
    movie_index = new_df[new_df.title.str.contains(movie, case=False)].index
    if len(movie_index) == 0:
        print("Movie not found.")
        return

    movie_index = movie_index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(new_df.iloc[i[0]].to_dict())

    return recommended_movies


# In[8]:
movies_cleaned = movies.dropna(subset=['title'])


def search(movie_title):
    results = movies_cleaned[movies_cleaned['title'].str.contains(movie_title, case=False)]
    similar_movies = results.head(50).to_dict(orient='records')

    return similar_movies


# In[9]:

def find_movie(movie_id):
    row = movies.loc[movies['id'] == movie_id]
    similar_movies = row.iloc[0].to_dict()

    return similar_movies

# In[10]


def random_movies():
    random_indices = random.sample(range(len(movies_cleaned)), 5)
    random_movie_list = []
    for index in random_indices:
        random_movie_list.append(movies_cleaned.iloc[index].to_dict())
    return random_movie_list