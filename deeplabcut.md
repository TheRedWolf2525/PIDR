# Utilisation de DEEPLABCUT
Tout se fait dans l'environnement : ```conda activate DEEPLABCUT```

## Création d'un projet
```bash
python
```
```python
import deeplabcut
deeplabcut.create_new_project('NomProjet', 'NomUtilisateur', ['/chemin/vers/ta_video.mp4'], working_directory='/chemin/vers/le/dossier_du_projet', copy_videos=True)```  
```

## Extraction des images (frames)
Si plus de 20 frames : 
```bash
nano /home/emeline/Documents/PIDR/VESPA-Souris-2025-05-08/config.yaml
```
Et changé la ligne : ```numframes2pick: 20```  
Puis :
```python
deeplabcut.extract_frames("/chemin/vers/le/dossier_du_projet/config.yaml")
```

## Labellisation des points 
A faire via l'interface graphique.
Lancement de l'interface graphique : ```python -m deeplabcut```

## Vérification des labels
```python
deeplabcut.check_labels("/chemin/vers/le/dossier_du_projet/config.yaml")
```

## Entraînement du réseau
```python
deeplabcut.create_training_dataset("/chemin/vers/le/dossier_du_projet/config.yaml")
deeplabcut.train_network("/chemin/vers/le/dossier_du_projet/config.yaml", maxiters= 5000 , displayiters = 100)
```

## Évaluation du réseau
```python
deeplabcut.evaluate_network("/chemin/vers/le/dossier_du_projet/config.yaml")
```

## Analyse d'une vidéo
```python
deeplabcut.analyze_videos("/chemin/vers/le/dossier_du_projet/config.yaml", ['/chemin/vers/ta_video.mp4'])
```

## Filtration des points
```python
deeplabcut.filterpredictions("/chemin/vers/le/dossier_du_projet/config.yaml", ['/chemin/vers/ta_video.mp4']")
```

## Génération d'une vidéo avec points
```python
deeplabcut.create_labeled_video("/chemin/vers/le/dossier_du_projet/config.yaml", ['/chemin/vers/ta_video.mp4']")
```

## Création du dossier *exported_model* pour le live
```python
deeplabcut.export_model("/chemin/vers/le/dossier_du_projet/config.yaml")
```