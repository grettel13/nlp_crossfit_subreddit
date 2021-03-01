# Classifying Hotel Reservation Cancelations

Demand forecasting is essential for hotel management to accurately meet guest needs while avoiding unnecessary costs. Reliable estimates of net demand are necessary for:
- Preparation of resources including staff and food offered at hotel
- Revenue management
- Pricing and cancelation policy governance

Hotels have the option of implementing strict cancelation policies, but these can be a detriment and result in less bookings.

>## Can hotel reservation cancelations be predicted?

Of course, no prediction can ever be exact, but implementing data science models for this classficiation problem can narrow the degree of uncertainty around reservation cancelations.

>By implementing a random forest model, a precision of 89% for 'canceled' class was achieved on unseen data.

Tuning the classification model for the precision metric allows for a more conservative approach. This sides on higher confidence of predicted cancelations in efforts to avoid situations of under-preparedness for hotel guests.

---
# Approach:

1. Understand/clean data
2. Perform Exploratory Data Analysis (EDA)
3. Metrics selection
4. Implement classification algorithms
4. Model selection

# Data used:

The data is sourced from an article called [Hotel booking demand datasets](https://www.sciencedirect.com/science/article/pii/S2352340918315191#bib6) by Nuno Antonio, Ana Almeida, and Luis Nunes in 2019.

The scrubbed data was made publicly available from the hotels' property management system (PMS) for investigation and learning.

Data over a 2-year span contains:
- 2 hotels
- ~120K observations
- 32 features

# Features used:

18 features were selected. For a full list of features and additional details, please reference the data source article.

Basic booking features:

| Feature | Description
| --------------- | --------------
| Hotel | H1 (Resort Hotel) or H2 (City Hotel)
| Stay Month | Month the arrival date occurs
| Week nights | Number of week nights in reservation
| Weekend nights | Number of weekend nights in reservation
| Lead time | Days in advance of arrival date booking was made
| Adults | Number of adults in reservation
| Country | **Transformed**: Nationality of guest. 1 for Portugal, 0 for any other
| ADR | Average daily rate
| Total stay cost | **Calculated**: Number of days in stay * ADR
| ADR over average hotel cost | **Calculated**: 1 if exceeds average hotel ADR for all bookings in train set. 0 if under average ADR
<br/>

Additional Details:
| Feature | Description
| --------------- | --------------
| Meal | Meal type following hospitality standards
| Parking spaces | Number of parking spaces needed
| Special requests | Number of special requests made
| Deposit type | Ex: No deposit, Non-refundable
| Agent | **Transformed**: 1 if agent used for booking. 0 if no agent used
| Marget segment | Ex: Online Travel Agency

<br/>

# Tools Used:

- Tableau
- Pandas
- Seaborn
- Matplotlib

# File Organization:
- **Hotel Reservation Cancelations.pdf** - 5 minute presentation of project findings
- **hotel_bookings.ipynb** - main notebook
- **hotels.py** - helper functions utilized by main notebook
- **hotel_create_psql_db.ipynb** - notebook used to load original data in CSV formats to a postgres sql database locally
- **sql_challenges** dir - used to submit SQL exercises unrelated to project success
