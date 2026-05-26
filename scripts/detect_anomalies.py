import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

print("AI anomaly detection script started...")

df = pd.read_csv("data/failed_logins.csv")

features = df[
    [
        "failed_logins",
        "hour_of_day",
        "day_of_week",
        "unique_users_attempted"
    ]
]

model = IsolationForest(
    contamination=0.30,
    random_state=42
)

df["anomaly"] = model.fit_predict(features)

df["status"] = df["anomaly"].apply(
    lambda x: "ANOMALY" if x == -1 else "NORMAL"
)

df["risk_score"] = (
    df["failed_logins"] * 2 +
    df["unique_users_attempted"] * 5
)

df.to_csv("reports/anomaly_results.csv", index=False)

alerts = df[df["status"] == "ANOMALY"]

print("\n=== ANOMALY ALERTS ===")
print(alerts[["timestamp", "username", "source_ip", "failed_logins", "risk_score", "status"]])

plt.figure(figsize=(10, 5))
plt.scatter(df["hour_of_day"], df["failed_logins"])
plt.xlabel("Hour of Day")
plt.ylabel("Failed Logins")
plt.title("AI Failed Login Anomaly Detection")
plt.savefig("screenshots/anomaly_chart.png")
print("\nChart saved to screenshots/anomaly_chart.png")
print("Report saved to reports/anomaly_results.csv")
