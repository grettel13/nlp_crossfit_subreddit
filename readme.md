# Analyzing Crossfit Subreddit with NLP

*Using Natural Language Processing techniques on the discourse within the Crossfit subreddit community to gain insights for athletes and gym owners.*

Please see my [blog post](https://gretteljuarez.medium.com/analyzing-crossfit-subreddit-with-nlp-4a4e9f008518) for more detailed insights.

![](./images/garage_gym.png)

**First:** What is r/crossfit?

**Crossfit** is a sport for everyone incorporating constant variation, functional movements, and high intensity training.

**Reddit** is a network of communities based on people's interests. r/crossfit is a subreddit group open to anyone to join and discuss.

---

What Crossfitters discuss and value can be informative to gym business owners looking to recover from pandemic impacts or just improve their services.

>## What is the discourse amongst crossfit redditors?


In this project, NLP methods are used to discover insights about what Crossfitters value and discuss in the subreddit community.


---
# Approach:

1. Scraped subreddit posts using [pushshift](https://www.reddit.com/r/pushshift/comments/bcxguf/new_to_pushshift_read_this_faq/) API
2. Data Cleaning / Pre-Processing
4. Topic modeling / Tuning
4. Pre-pandemic vs Pandemic analysis

# Data:

r/crossfit:
- 2008 - Feb 19, 2021
- 221K members
- 65,792 submissions (posts) not including comments

# Features:

Each document in corpus is a post: Title + Body

Additional features collected include:

| Feature | Description
| --------------- | --------------
| id | Reddit submission (post) ID. Can be used to pull comments / replies
| author | Submission author
| time | Time of submission converted to datetime
| num_comments | Number of comments submission received
| score | Net score submission received. Upvotes minus downvotes
| upvote_ratio | % upvotes contributing to score
| url | URL related to post, commonly to comment, image, video, or external link posted
| video | Categorical identifying whether post contains: video, image, or none. Imputed from reddit features.
<br/>

# Tools:

- Pandas
- Spacy - lemmatization
- Sklearn
    - TFIDF Vectorization
    - NMF Topic Modeling
- Sentiment Analysis
    - IBM Tone Analyzer
    - Vader Sentiment
- Visualization
    - Tableau
    - Seaborn
    - Matplotlib

# File Organization:
- **scatter_text** dir - notebook used to make pre-pandemic vs pandemic scatter text for word frequency analysis
- **sentiment_analysis** dir - notebook used to perform sentiment analysis on glassman documents. small sample size. future work would invlolve more posts and include comments/replies
- **Crossfit Subreddit.pdf** - 5 minute presentation of project findings
- **cf_reddit_data_collection.ipynb** - notebook used to collect reddit submissions. Also includes code for collecting comments/replies for future work
- **cf_reddit_topics.ipynb** - main notebook used for topic modeling
- **reddit.py** - helper functions utilized by main notebook


