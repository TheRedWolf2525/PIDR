import cv2  # Importer OpenCV
from dlclive import DLCLive, Processor

# Spécifie le chemin vers le modèle exporté (le répertoire contenant le fichier .pb et le fichier pose_cfg.yaml)
model_path = '/home/emeline/Documents/PIDR/MouseTopView-MTV-2025-04-26/exported-models/DLC_MouseTopView_resnet_50_iteration-0_shuffle-1/'

# Initialisation du processeur et du modèle (assurez-vous que le modèle est correctement spécifié)
dlc_proc = Processor()

# Initialisation de l'inférence avec le modèle
dlc_live = DLCLive(model_path, processor=dlc_proc)

# Initialisation du modèle (pas besoin de passer un frame ici)
dlc_live.init_inference()  # Ici pas de frame passé, juste l'initialisation

# Capturer la vidéo depuis une caméra
cap = cv2.VideoCapture(2)  # 0 pour la caméra par défaut

# Essayer de définir les FPS à 60
cap.set(cv2.CAP_PROP_FPS, 60)

# Vérifier si la caméra a bien réglé les FPS
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS de la caméra: {fps}")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Passer l'image à DLC Live pour récupérer les points
    pose = dlc_live.get_pose(frame)

    # Afficher l'image avec les points (si tu veux voir l'image avec les points)
    for point in pose:  # Tu peux itérer sur les points de la pose si c'est un tableau
        cv2.circle(frame, (int(point[0]), int(point[1])), 5, (0, 255, 0), -1)  # Exemple de dessin des points sur l'image

    # Afficher l'image avec les points (si tu veux voir l'image avec les points)
    cv2.imshow('Frame', frame)

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
