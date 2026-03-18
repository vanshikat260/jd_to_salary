# jd_to_salary
Salary Prediction using NLP & Machine Learning
Overview

This project predicts job salaries based on unstructured job descriptions and key job attributes using Natural Language Processing (NLP) and Machine Learning.

The system processes raw job postings and estimates salary in real time through an interactive web interface.

Problem Statement

Salary information is often:

Missing

Inconsistent (hourly, monthly, yearly)

Difficult to estimate from job descriptions

This project aims to predict salary using job description, location, job type, and other contextual features.

Approach
1. Data Collection

Job data collected from APIs (e.g., Remotive)

Additional dataset sourced from job postings (Glassdoor dataset)

2. Data Preprocessing
Salary Cleaning

Converted all salaries into a consistent annual format

Handled:

Hourly to annual

Monthly to annual

Salary ranges to mean value

Text Cleaning

Removed HTML tags

Removed special characters

Converted text to lowercase

3. Feature Engineering
Feature	Description
Job Description	Main textual input
Location	Geographic factor
Job Type	Full-time / Contract
Seniority	Junior / Mid / Senior
Company Size	Organizational scale
4. NLP Pipeline

Used TF-IDF vectorization to convert text into numerical features

Limited vocabulary size to balance text and structured features

5. Model

Implemented using scikit-learn.

Models experimented:

Random Forest Regressor


Pipeline:
Text (TF-IDF) + categorical features → regression model → salary prediction

Results and Observations

Model predicts salary ranges based on job input

Text features dominate prediction due to high dimensionality

Limited dataset leads to:

Lower variation in predictions

Bias toward average salary

Limitations

Small dataset (~600 rows)

Limited salary diversity

Inconsistent real-world salary data

Reduced accuracy across different geographic regions

Future Improvements

Increase dataset size

Extract experience directly from text

Add skill-based features (Python, ML, NLP, etc.)

Improve salary normalization

Use more advanced models

Deploy the application online

#Streamlit Web App

Built using Streamlit.

Features:

Input raw job description

Select job attributes

Get instant salary prediction

Run Locally:
streamlit run app.py
Project Structure
salary_app/
│
├── app.py
├── salary_model.pkl
├── notebook.ipynb
└── README.md
Key Learnings

Importance of data quality over model complexity

Challenges in real-world NLP problems

Feature imbalance between text and structured data

End-to-end machine learning pipeline development

Conclusion

It highlights practical challenges in working with real-world data and provides a foundation for building more advanced salary prediction systems.
