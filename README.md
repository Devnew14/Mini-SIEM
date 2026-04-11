# 🔐 Mini-SIEM

![Python](https://img.shields.io/badge/python-3.12-blue)

**Mini-SIEM** est un projet Python qui simule un **Security Information and Event Management (SIEM)** à petite échelle.  
Il a pour objectif de démontrer les principes de **collecte, analyse et détection d’événements de sécurité**.

---

## 🚀 Fonctionnalités

- 📝 **Génération de logs**  
  Simulation d’événements systèmes et réseau (connexions, erreurs, activités suspectes…)

- 🧹 **Filtrage des faux positifs**  
  Nettoyage des données pour isoler uniquement les événements réellement pertinents

- 🚨 **Détection d’alertes**  
  Identification des comportements anormaux ou suspects

- 📊 **Visualisation des données**  
  Représentation graphique des alertes pour une meilleure analyse

---

## 🛠️ Prérequis

- Python **3.12** ou supérieur  

### 📦 Dépendances

- `pandas`
- `numpy`
- `plotly`
- `matplotlib` *(optionnel)*

### Installation

```bash
pip install pandas numpy plotly matplotlib


mini-siem/
│
├── logs/              # Fichiers de logs générés
├── src/               # Code source principal
│   ├── generator.py   # Génération de logs
│   ├── analyzer.py    # Analyse et filtrage
│   ├── detector.py    # Détection d’anomalies
│   └── visualizer.py  # Visualisation
│
├── main.py            # Point d’entrée du programme
└── README.md

▶️ Utilisation

Lancer le programme principal :

python main.py
Exemple d’utilisation
Générer des logs simulés
Filtrer les événements suspects
Afficher les alertes détectées
Visualiser les résultats sous forme de graphiques
📊 Exemple de sortie
Liste d’alertes critiques
Graphiques interactifs (via Plotly)
Statistiques sur les événements détectés
🎯 Objectifs pédagogiques

Ce projet permet de comprendre :

Le fonctionnement d’un SIEM
Le traitement et l’analyse de logs
La détection d’anomalies simples
La visualisation de données de sécurité
🔧 Améliorations possibles
Intégration de logs réels (syslog, firewall…)
Détection basée sur du machine learning
Interface web (Dashboard)
Alertes en temps réel (email, webhook…)
