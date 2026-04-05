import pandas as pd
import numpy as np
from datetime import datetime, timedelta




logs = pd.read_csv('logs.csv')

# Exemple de règle simple pour filtrer les alertes "low" provenant de sources internes
filtered_logs = logs[~((logs['severity'] == 'low') & (logs['source_ip'].str.startswith('192.168.1')))]

print("Alertes après filtrage des faux positifs :", len(filtered_logs))
filtered_logs.to_csv('filtered_logs.csv', index=False)