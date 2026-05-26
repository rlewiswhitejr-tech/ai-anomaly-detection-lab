# AI-Powered SOC Anomaly Detection Lab

## Overview
This project uses machine learning to detect suspicious failed-login behavior. It simulates SOC authentication logs and uses an Isolation Forest model to identify abnormal activity.

## Tools Used
- Python
- pandas
- scikit-learn
- matplotlib
- Isolation Forest

## Detection Goal
The lab detects possible brute-force or password-spraying behavior using:
- Failed login count
- Hour of day
- Day of week
- Number of unique users attempted

## Results
The model flags high-volume failed login activity as anomalous and generates a CSV security report.

## Output Files
- reports/anomaly_results.csv
- screenshots/anomaly_chart.png

## Cybersecurity Value
This lab demonstrates:
- AI/ML security analytics
- SOC-style alerting
- Brute-force detection
- Risk scoring
- Python automation
- Security reporting

## Resume Bullet
Built an AI-powered SOC anomaly detection lab using Python, pandas, and Isolation Forest to identify suspicious authentication behavior, generate risk scores, and create security reports for brute-force attack analysis.