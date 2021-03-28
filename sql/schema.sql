-- Drop table if exists
DROP TABLE twitter_tweets;

--create table in Twitter_DB
CREATE TABLE twitter_tweets(
    tweets VARCHAR NOT NULL,
    id INT NOT NULL,
    len INTEGER,
    date DATETIME,
    source VARCHAR NOT NULL,
    likes INTEGER,
    retweets INTEGER,
);

--create table in Twitter_DB
CREATE TABLE tweet_words(
    words VARCHAR NOT NULL,
);