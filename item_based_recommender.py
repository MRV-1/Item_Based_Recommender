###########################################
# Item-Based Collaborative Filtering
###########################################

# Step 1: Preparing the Data Set
# Step 2: Creating User Movie Df
# Step 3: Making Item-Based Movie Recommendations
# Step 4: Preparing the Working Script

######################################
# Step 1: Preparing the Data Set
######################################

import pandas as pd
pd.set_option('display.max_columns', 500)
movie = pd.read_csv( r'dataset\movie_lens_dataset\movie.csv')
rating = pd.read_csv(r'dataset\movie_lens_dataset\rating.csv')
df = movie.merge(rating, how="left", on="movieId")
df.head()


######################################
# Step 2: Creating User Movie Df
######################################

df.head()
df.shape    
df["title"].nunique()    

# Question: There is a movie that got 10,000 comments, there is a movie that got 30 comments, should I really focus on all of them?

df["title"].value_counts().head()  # The value_counts of the titles are used to find out which movie has the highest rate.


comment_counts = pd.DataFrame(df["title"].value_counts())
rare_movies = comment_counts[comment_counts["count"] <= 1000].index   
common_movies = df[~df["title"].isin(rare_movies)]                  
common_movies.shape
common_movies["title"].nunique()
df["title"].nunique()

# An operation should be performed on the incoming information so that there are users in the rows and titles in the columns.

user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")

# Pivot table; It receives the data regarding the answer to the questions "Which variable will come to the index, which variable will come to the column, and what will come to the intersection of these?"

user_movie_df.shape  #(138493, 3159)  (user, film)
user_movie_df.columns


######################################
# Step 3: Making Item-Based Movie Recommendations
######################################

movie_name = "Matrix, The (1999)"
movie_name = "Ocean's Twelve (2004)"
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)


movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)


# returns all movies belonging to the entered keyword
def check_film(keyword, user_movie_df):
    return [col for col in user_movie_df.columns if keyword in col]

check_film("Insomnia", user_movie_df)

######################################
# Step 4: Preparing the Working Script
######################################

def create_user_movie_df():
    import pandas as pd
    movie = pd.read_csv(r'dataset\movie_lens_dataset\movie.csv')
    rating = pd.read_csv(r'dataset\movie_lens_dataset\rating.csv')
    df = movie.merge(rating, how="left", on="movieId")
    comment_counts = pd.DataFrame(df["title"].value_counts())
    rare_movies = comment_counts[comment_counts["count"] <= 1000].index
    common_movies = df[~df["title"].isin(rare_movies)]
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return user_movie_df

user_movie_df = create_user_movie_df()

# It looks at the liking patterns of the given movie and other movies, then brings 10 movies with high tan correlation
def item_based_recommender(movie_name, user_movie_df):
    movie_name = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)

item_based_recommender("Matrix, The (1999)", user_movie_df)

movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]

item_based_recommender(movie_name, user_movie_df)





