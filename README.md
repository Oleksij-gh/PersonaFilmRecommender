# PersonaFilmRecommender
Application for recommending a movie based on a psychological portrait

# Датасет взят с [Kaggle](https://www.kaggle.com/datasets/arslanali4343/top-personality-dataset/data)
Описание данных:
## 2018-personality-data.csv

About this file

The personality-data contains the header which described as follows:

Userid: the hashed user_id.

Openness: an assessment score (from 1 to 7) assessing user tendency to prefer new experience. 1 means the user has tendency NOT to prefer new experience, 7 means the user has tendency to prefer new experience.

Agreeableness: an assessment score (from 1 to 7) assessing user tendency to be compassionate and cooperative rather than suspicious and antagonistic towards others. 1 means the user has tendency to NOT be compassionate and cooperative. 7 means the user has tendency to be compassionate and cooperative.

Emotional Stability: an assessment score (from 1 to 7) assessing user tendency to have psychological stress. 1 means the user has tendency to have psychological stress, and 7 means the user has tendency to NOT have psychological stress.

Conscientiousness: an assessment score (from 1 to 7) assessing user tendency to be organized and dependable, and show self-discipline. 1 means the user does not have such a tendency, and 7 means the user has such tendency.

Extraversion: an assessment score (from 1 to 7) assessing user tendency to be outgoing. 1 means the user does not have such a tendency, and 7 means the user has such a tendency.

Assigned Metric: one of the follows (serendipity, popularity, diversity, default). Each user, besides being assessed their personality, was evaluated their preferences for a list of 12 movies manipulated with serendipity, popularity, diversity value or none (default option).

Assigned Condition: one of the follows (high, medium, low). Based on the assigned metric, and this assigned condition, the list of movies was generated for the users. For example: if the assigned metric is serendipity and the assigned condition is high, the movies in the list are highly serendipitous. We document how we manipulated the movie list based on the assigned condition and assigned metric in page 6 of our research paper mentioned above.

Movie_x (x is from 1 to 12): The list consists of 12 movies. These fields contain the ids of the twelve movies in the list

## 2018_ratings.csv

About this file

For more information about the data, and how we collected and ran the study, please refer to page 5 in our research paper.

The ratings.csv file contains the header as described as follows:

userId: the hashed user_id.
movieId: the id of the movie that the user (corresponding to userId) rated.
rating: the rating (from 0.5 to 5 stars) provided by the user.
tstamp: when the user rated the movie.
