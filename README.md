# Item_Based_Recommender
Application based on Item-Based Collaborative Filtering 🐍 

### Step 1: Preparing the Data Set
### Step 2: Creating User Movie Df
### Step 3: Making Item-Based Movie Recommendations
### Step 4: Preparing the Working Script

# Dataset Story

An online movie viewing platform wants to develop a recommendation system with a collaborative filtering method.
The company, which is experimenting with content-based recommendation systems, wants to develop recommendations that accommodate the opinions of the community.

When users like a movie, they want to recommend other movies that have a similar liking pattern to that movie.


*****
Provided by a company called MovieLens.
It contains movies and the scores given to these movies.
The dataset contains approximately 2000000 ratings for approximately 27000 movies.

--> For dataset : https://grouplens.org/datasets/movielens/

# Step 2: Creating User Movie Df

--> It is the most important step of the application
***

Let's say a user has rated only one movie, in this case it will create a cell for all movies in user_movie_df.

This causes delays and performance problems in calculation processes.

There is a solution to this situation and some reduction processes that need to be done because users will not recommend movies to movies they have never watched.

For example; Excluding movies that have a rating of less than 1000 from the study may be a solution.

# Step 3: Making Item-Based Movie Recommendations

# Step 4: Preparing the Working Script
