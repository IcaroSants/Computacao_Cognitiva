# Import the necessary modules
from nlp_utils import get_tweets_sample
from nltk.tokenize import regexp_tokenize, word_tokenize, sent_tokenize, TweetTokenizer
import re

tweets = get_tweets_sample()

# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"
# Use the pattern on the first tweet in the tweets list
hashtags = re.findall(pattern1,tweets[0])
print(hashtags)

# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"[@|#]\w+"
a_hashtags = regexp_tokenize(tweets[-1],pattern2)
print(a_hashtags)


# Use the pattern on the last tweet in the tweets list

for tweet in tweets:
    mentions_hashtags = regexp_tokenize(tweet,pattern2)
    print(mentions_hashtags)

# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)
