# Analyzing Crossfit Subreddit with NLP

*Using Natural Language Processing techniques on the discourse within the Crossfit subreddit community to gain insights for athletes and gym owners.*

> ## **Please see my [blog post](https://gretteljuarez.medium.com/analyzing-crossfit-subreddit-with-nlp-4a4e9f008518) for a more detailed walkthrough of project insights.**

![](./images/garage_gym.png)

2020 was a particularly bad year for gym athletes and owners due to the pandemic and Greg Glassman's (former Crossfit owner) negative actions. What Crossfitters discuss and value can be informative to gym business owners looking to recover from these impacts or just improve their services.

In this project, NLP methods are used to discover insights about what recent changes mean for Crossfit athletes and gym owners.

---

<div style="text-align:center"><img src="./images/rcrossfit.png" /></div>

> What is r/crossfit?

**Crossfit** is a sport for everyone incorporating constant variation, functional movements, and high intensity training.

**Reddit** is a network of communities based on people's interests.

**r/crossfit** is a reddit community channel (subreddit) for people interested in crossfit, open to anyone to join and discuss

---
# Approach:

1. Data Collection
2. Data Cleaning / Pre-Processing
4. Topic modeling / Tuning
4. Pre-pandemic vs Pandemic analysis
5. Results/Findings

# Data:

Data was collected by scraping subreddit posts using [pushshift](https://www.reddit.com/r/pushshift/comments/bcxguf/new_to_pushshift_read_this_faq/) API.

Details:
- posts dated 2008 - Feb 19, 2021
- 232K subreddit members
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

# Findings

Using applied Natural Language Processing techniques, this analysis provides insights for athletes and gym owners from the online Crossfit reddit community. This investigation outlined:
- Athletes actively use this online community to seek feedback on their lifts and celebrate personal records. The volume of posts in this topic correlates with Crossfit Games and Open. Perhaps hosting in-house competitions could increase gym member engagement
- Racism is an important discussion and many feel strongly about taking a stance against it
- There is a potential opportunity for gym owners to provide remote services such as combined programming and lift feedback given many more athletes have their own equipment due to the pandemic


# File Organization:
- ```images``` - dir containing pictures/images used in readme and notebook
- ```scatter_text``` - dir containing scatter_text output
- ```1_cf_data_collection.ipynb``` - notebook used to collect reddit submissions. Also includes code for collecting comments/replies for future work
- ```2_cf_topic_modeling.ipynb``` - notebook used for topic modeling
- ```3_cf_visualizations.ipynb``` - notebook used for visualizations
- ```4_cf_pandemic_vs_prepandemic_text``` - notebook used to make pre-pandemic vs pandemic scatter text for word frequency analysis
- ```5_cf_sentiment_analysis``` notebook used to perform sentiment analysis on glassman documents. small sample size. future work would invlolve more posts and include comments/replies
- ```Crossfit Subreddit.pdf``` - 5 minute presentation of project findings
- ```reddit.py``` - helper functions utilized by notebooks


