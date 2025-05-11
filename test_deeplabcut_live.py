import cv2
from dlclive import DLCLive, Processor
import numpy as np
from rendering import render

### Chemin vers le dossier où se trouve l'entraînement
# Du type "nom_du_dossier/exported-models/DLC_nom_du_projet_resnet_50_iteration-0_shuffle-1/"
model_path = './VESPA-Souris-2025-05-08/exported-models/DLC_VESPA_resnet_50_iteration-0_shuffle-1/'

dlc_proc = Processor()
dlc_live = DLCLive(model_path, processor=dlc_proc)
dlc_live.init_inference()

### Régalges caméra
cap = cv2.VideoCapture(2)   # 0 pour la caméra de l'ordi, sinon caméra externe souvent 2
cap.set(cv2.CAP_PROP_FPS, 60)
fps = cap.get(cv2.CAP_PROP_FPS) # Tentative d'amélioration des fps
print(f"FPS de la caméra: {fps}")

### Paramètres du cercle (calcul échelle)
real_circle_diameter_cm = 20  # Diamètre du cercle en cm
real_object_size_cm = 20  # Taille réelle de l'objet en cm
object_size_in_pixels = 480  # Taille de l'objet en pixels dans l'image
# Calcul de l'échelle (cm par pixel)
scale = real_object_size_cm / object_size_in_pixels
# Calcul du diamètre du cercle en pixels en fonction de la taille réelle
circle_diameter_pixels = real_circle_diameter_cm / scale  # Diamètre du cercle en pixels
# Distance à la caméra (ici tu es à 20 cm)
distance_to_camera_cm = 20

while True:
    ret, frame = cap.read()
    if not ret:
        break
    height, width = frame.shape[:2]
    circle_center = (width // 2, height // 2)

    # Pose estimation
    pose_raw = dlc_live.get_pose(frame)
    pose = np.array(pose_raw).reshape(-1, 3)
    for i, point in enumerate(pose):
        x, y, likelihood = point
        if likelihood > 0.5:
            cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)
            cv2.putText(frame, f"{i}", (int(x) + 5, int(y) - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    # Dessiner le cercle sur la vidéo principale
    cv2.circle(frame, circle_center, int(circle_diameter_pixels // 2), (0, 255, 255), 2)
    # Affichage de la vidéo
    cv2.imshow('Video Feed', frame)
    
    # Image blanche pour dessin isolé
    render(frame, pose, circle_center, circle_diameter_pixels)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()