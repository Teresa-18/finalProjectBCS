-- Drop table if exists
DROP TABLE twitter_tweets;

--create table in Twitter_DB
CREATE TABLE twitter_tweets(
<<<<<<< HEAD
    tweets VARCHAR NOT NULL,
    id BIGINT NOT NULL,
    len INTEGER,
    date DATE,
    source VARCHAR NOT NULL,
    likes INTEGER,
    retweets INTEGER,
    PRIMARY KEY (id)
=======
    monday_tweets VARCHAR NOT NULL
    friday_tweets VARCHAR NOT NULL,
    april_tweets VARCHAR NOT NULL
    -- date DATE,
    -- source VARCHAR NOT NULL,
    -- likes INTEGER,
    -- retweets INTEGER,
    -- PRIMARY KEY (index)
>>>>>>> 9a4b5f988ec9e25c061e30035d0e95f14bda46b9
);

-- --create table in Twitter_DB
-- CREATE TABLE twitter_friday(
--     friday_tweets VARCHAR NOT NULL
--     -- friday_tweets VARCHAR NOT NULL,
--     -- april_tweets VARCHAR NOT NULL
--     -- date DATE,
--     -- source VARCHAR NOT NULL,
--     -- likes INTEGER,
--     -- retweets INTEGER,
--     -- PRIMARY KEY (index)
-- );

-- --create table in Twitter_DB
-- CREATE TABLE twitter_april(
--     april_tweets VARCHAR NOT NULL
--     -- friday_tweets VARCHAR NOT NULL,
--     -- april_tweets VARCHAR NOT NULL
--     -- date DATE,
--     -- source VARCHAR NOT NULL,
--     -- likes INTEGER,
--     -- retweets INTEGER,
--     -- PRIMARY KEY (index)
-- );