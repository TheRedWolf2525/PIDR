# Création d'un environnement virtuel

```
conda create -n dlc-live python=3.7 tensorflow==1.13.1
```

# Installation des librairie nécessaires

```
conda activate dlc-live
pip install deeplabcut-live-gui
sudo apt update
sudo apt install libgtk2.0-dev pkg-config
pip uninstall opencv-python-headless opencv-python -y
pip install opencv-python
```

# Lancer *test_deeplabcut_live.py*
Dans l'environnement créé :
```
python test_deeplabcut_live.py
```