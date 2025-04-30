# Création d'un environnement virtuel

```
conda create -n deeplabcut_live_env python=3.8
```

# Installation des librairie nécessaires

```
conda activate deeplabcut_live_env
pip install 'deeplabcut[gui]'
pip install numpy==1.22
pip install --upgrade tensorflow
pip install tensorpack
pip install tf-slim
```

# Lancer *test_deeplabcut_live.py*
Dans l'environnement créé :
```
python test_deeplabcut_live.py
```