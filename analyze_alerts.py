import pandas as pd
import numpy as np
from datetime import datetime, timedelta


logs = pd.read_csv('logs.csv')

# Compter les alertes par type
alert_count = logs['alert_type'].value_counts()
print("Alertes par type :\n", alert_count)

# Détecter anomalies simples : par exemple, plus de 10 alertes de même type en 1 heure
logs['timestamp'] = pd.to_datetime(logs['timestamp'])
logs.set_index('timestamp', inplace=True)
hourly_counts = logs.groupby([pd.Grouper(freq='1H'), 'alert_type']).size().reset_index(name='count')
anomalies = hourly_counts[hourly_counts['count'] > 10]
print("Anomalies détectées :\n", anomalies)