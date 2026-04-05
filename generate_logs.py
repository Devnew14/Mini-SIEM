import pandas as pd
import random
from datetime import datetime, timedelta

# Générer 200 timestamps espacés de 15 minutes
base_time = datetime.now()
timestamps = [base_time - timedelta(minutes=15*i) for i in range(200)]

# Types d’alertes
alert_types = ['login_failed', 'malware_detected', 'port_scan', 'file_access', 'cpu_spike']

# Créer le DataFrame
logs = pd.DataFrame({
    'timestamp': timestamps,
    'alert_type': [random.choice(alert_types) for _ in range(len(timestamps))],
    'source_ip': [f"192.168.1.{random.randint(1,254)}" for _ in range(len(timestamps))],
    'severity': [random.choice(['low','medium','high']) for _ in range(len(timestamps))]
})

# Sauvegarder correctement avec des virgules
logs.to_csv('logs.csv', index=False)
print("Logs simulés générés correctement !")