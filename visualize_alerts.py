import os
import pandas as pd
import plotly.express as px

# Vérifie si le fichier filtré existe, sinon utilise logs.csv
csv_file = 'filtered_logs.csv' if os.path.exists('filtered_logs.csv') else 'logs.csv'
logs = pd.read_csv(csv_file)

# Compter les alertes et renommer les colonnes pour Plotly
alert_counts = logs['alert_type'].value_counts().reset_index()
alert_counts.columns = ['alert_type', 'count']

# Graphique interactif Plotly
fig = px.bar(alert_counts,
             x='alert_type', y='count',
             labels={'alert_type':'Type d’alerte', 'count':'Nombre d’alertes'},
             title='Alertes par type')
fig.show()