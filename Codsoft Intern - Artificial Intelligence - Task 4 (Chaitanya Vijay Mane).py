
# RECOMMENDATION SYSTEM
# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie and rating data
movies = pd.read_csv('/content/movie.csv')  # Assuming you have a 'movies.csv' file with columns 'movieId' and 'title'
ratings = pd.read_csv('/content/rating.csv')  # Assuming you have a 'ratings.csv' file with columns 'userId', 'movieId', and 'rating'

# Merge the ratings and movies dataframes
df = pd.merge(ratings, movies, on='movieId')

# Create a user-item matrix
user_movie_ratings = df.pivot_table(index='userId', columns='title', values='rating')

# Fill NaN values with 0
user_movie_ratings = user_movie_ratings.fillna(0)

# Transpose the matrix to get item-user matrix
movie_user_ratings = user_movie_ratings.T

# Calculate the cosine similarity between movies (sparse matrix version)
movie_similarity = cosine_similarity(movie_user_ratings, dense_output=False)

# Create a DataFrame with the similarity values
movie_similarity_df = pd.DataFrame(data=movie_similarity, index=user_movie_ratings.columns, columns=user_movie_ratings.columns)

def get_movie_recommendations(user_ratings):
    similar_scores = movie_similarity_df.dot(user_ratings)
    print("Similar Scores:")
    print(similar_scores)

    similar_movies = similar_scores.sort_values(ascending=False)
    print("\nSimilar Movies:")
    print(similar_movies)

    recommended_movies = similar_movies[~similar_movies.index.isin(user_ratings.index)]
    return recommended_movies.head(10)  # You can adjust the number of recommendations

# Example: Get recommendations for a user (user with userId=1)
user_id = 1
user_ratings = user_movie_ratings.loc[user_id]
recommendations = get_movie_recommendations(user_ratings)

print("Top 10 Movie Recommendations:")
print(recommendations)