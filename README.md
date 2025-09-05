## Project Title: Predicting Customer Churn Risk Score

### Objective: 
##### This project is aimed at building a multi-class classification model to assign churn risk score to customers. Firstly what is Churn? Churn  is the percentage of customers who stopped using a company’s product or service during a specified time period. For example, if a company starts its quarter with 400 customers and ends with 380, its quarterly churn rate is 5%.

## Dataset:
##### This Dataset was gotten from HackerEarth ML Challange, and it includes a train.csv and test.csv with the following features: Demographics, Transactions behaviour and engagement metrics.

## Preprocessing Steps:
#### Dropped irrelevant columns like `customer_id` during modeling, and also handled missing values using mean imputation, then encoded categorical variables using get_dummies method,after that i scaled numerical feaures using StandardScaler and i applied smote to handle or to balance the class distribution in the dataset.

## Exploratory Data Analysis (EDA)
##### Before building any predictive model, it's essential to understand the underlying structure and patterns within the dataset. In this project, EDA was performed to uncover relationships between customer attributes and their churn risk scores.
## Key Insights:
##### Class Imbalance: Churn scores were skewed toward mid-to-high values, requiring resampling.
##### Membership Category vs Churn:  
##### Basic and No Membership customers showed the highest churn risk (score 5).
##### Premium and Platinum members had the lowest churn risk, likely due to better service quality.
##### Feature Correlations:
##### `tenure_days`, `points_in_wallet`, and `avg_transaction_value` showed moderate correlation with churn risk.
##### Missing Values: Found in `avg_frequency_login_days` and `points_in_wallet`, handled via median imputation.

##### Visualizations included histograms, box plots, and count plots segmented by churn score and membership category.

## Feature Engineering:
##### To enhance model performance, several behavior features were engineered:
##### Tenure: Days since signup (`tenure_days`)
##### Estimated Purchase Frequency: Approximated using `points_in_wallet / avg_transaction_value`.
##### Login Engagement: Inverse of `avg_frequency_login_days` to reflect activity.
##### Offer Engagement Score: Derived from `used_offer` and `offer_type` interactions.
##### These features helped capture customer loyalty, engagement, and transactional behavior.

## Modeling
##### We trained multiple models and selected the best based on multi-class classification performance:
##### Models Used:
##### XGBoost (`objective='multi:softmax'`, `num_class=5`)
#### Random Forest

## Training Strategy:
##### Applied SMOTE to balance classes
##### Used `StandardScaler` for feature normalization
##### Shifted labels to start from 0 for XGBoost compatibility
##### Evaluated using accuracy, precision, recall, and F1-score

## Evaluation
##### The best-performing model was **XGBoost**, achieving:
##### Accuracy: 72%
##### Macro F1-score: 0.67
##### Weighted F1-score: 0.71

## Classification Report Highlights:
##### Strong recall for churn scores 2–5
##### Weak recall for scores 0 and 1, indicating difficulty identifying loyal customers
##### Confusion matrix revealed over-prediction of mid-tier churners

## Business Impact
##### This model enables:
##### Targeted retention campaigns for high-risk customers
##### Resource prioritization based on churn severity
##### Customer segmentation for personalized engagement strategies

##### By identifying churn risk early, businesses can reduce customer loss and improve lifetime value.

### Author
### Promise Emefile 
### Data Scientist | Passionate about solving real-world problems with machine learning  
##### LinkedIn Profile:https://www.linkedin.com/in/promise-emefile
