# Projet VESPA : Environnement Virtuel pour la Stimulation et les Adaptations Post-Chute des Personnes Âgées
Le projet **VESPA** vise à développer un système innovant pour améliorer la prise en charge des personnes âgées ayant subi une chute, en utilisant des techniques de stimulation bilatérale alternée (SBA) pour traiter les troubles anxieux post-traumatiques. Ce système repose sur l’utilisation de la thérapie **EMDR** (Eye Movement Desensitization and Reprocessing), qui est renforcée par un suivi visuel de la position d'une souris en temps réel.
Le but principal de ce projet est de concevoir un dispositif capable de suivre en temps réel l'orientation d'une souris, en utilisant la technologie **DeepLabCut**, afin de piloter dynamiquement un ensemble de **LEDs** pour la stimulation visuelle. Cette méthode offre un potentiel de réduction de l'anxiété et de l'isolement des personnes âgées ayant subi des traumatismes physiques ou psychologiques.

### Objectifs du projet

- Développer un système automatisé de suivi visuel pour stimuler la récupération post-chute.
- Utiliser **DeepLabCut** pour suivre la position de la souris en temps réel.
- Piloter un système de LEDs pour réaliser des stimulations bilatérales alternées.
- Étudier les impacts de ce système sur la réduction des troubles anxieux chez les personnes âgées.
- Fournir une plateforme ouverte et reproductible pour la communauté scientifique.

### Contenu du dépôt

Ce dépôt GitHub contient :

- Le **code source** nécessaire à la mise en œuvre du suivi en temps réel avec **DeepLabCut**.
- Des **vidéos de démonstration** illustrant le fonctionnement du système.
- Une **documentation détaillée** pour comprendre la mise en place et l’utilisation du système.
- Des **ressources expérimentales** (données d'entraînement, vidéos d'exemple, etc.).


## Installation

Conda est nécessaire pour utiliser DeepLabCut (obtenable via le lien suivant)  
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Création d'un environnement virtuel conda :
```bash
conda env create -f DEEPLABCUT.yaml
```

Activation / Désactivation environnement conda :
```bash
conda activate DEEPLABCUT
```
```bash
conda deactivate
```

Lancement GUI DeepLabCut :
```bash
python3 -m deeplabcut
```

## Utilisation de DEEPLABCUT
Tout se fait dans l'environnement : ```conda activate DEEPLABCUT```

### Création d'un projet
```bash
python
```
```python
import deeplabcut
deeplabcut.create_new_project('NomProjet', 'NomUtilisateur', ['/chemin/vers/ta_video.mp4'], working_directory='/chemin/vers/le/dossier_du_projet', copy_videos=True)```  
```

### Extraction des images (frames)
Si plus de 20 frames : 
```bash
nano /home/emeline/Documents/PIDR/VESPA-Souris-2025-05-08/config.yaml
```
Et changé la ligne : ```numframes2pick: 20```  
Puis :
```python
deeplabcut.extract_frames("/chemin/vers/le/dossier_du_projet/config.yaml")
```

### Labellisation des points 
A faire via l'interface graphique.
Lancement de l'interface graphique : ```python -m deeplabcut```

### Vérification des labels
```python
deeplabcut.check_labels("/chemin/vers/le/dossier_du_projet/config.yaml")
```

### Entraînement du réseau
```python
deeplabcut.create_training_dataset("/chemin/vers/le/dossier_du_projet/config.yaml")
deeplabcut.train_network("/chemin/vers/le/dossier_du_projet/config.yaml", maxiters= 5000 , displayiters = 100)
```

### Évaluation du réseau
```python
deeplabcut.evaluate_network("/chemin/vers/le/dossier_du_projet/config.yaml")
```

### Analyse d'une vidéo
```python
deeplabcut.analyze_videos("/chemin/vers/le/dossier_du_projet/config.yaml", ['/chemin/vers/ta_video.mp4'])
```

### Filtration des points
```python
deeplabcut.filterpredictions("/chemin/vers/le/dossier_du_projet/config.yaml", ['/chemin/vers/ta_video.mp4']")
```

### Génération d'une vidéo avec points
```python
deeplabcut.create_labeled_video("/chemin/vers/le/dossier_du_projet/config.yaml", ['/chemin/vers/ta_video.mp4']")
```

### Création du dossier *exported_model* pour le live
```python
deeplabcut.export_model("/chemin/vers/le/dossier_du_projet/config.yaml")
```

## Utilisation de DEEPLABCUT LIVE

### Création d'un environnement virtuel

```bash
conda create -n dlc-live python=3.7 tensorflow==1.13.1
```

### Installation des librairie nécessaires

```bash
conda activate dlc-live
pip install deeplabcut-live-gui
sudo apt update
sudo apt install libgtk2.0-dev pkg-config
pip uninstall opencv-python-headless opencv-python -y
pip install opencv-python
```

### Lancer *test_deeplabcut_live.py*
Dans l'environnement créé :
```bash
python test_deeplabcut_live.py
```
