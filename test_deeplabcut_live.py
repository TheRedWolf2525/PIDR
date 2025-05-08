import cv2
from dlclive import DLCLive, Processor
import numpy as np

### Chemin vers le dossier où se trouve l'entraînement
# Du type "nom_du_dossier/exported-models/DLC_nom_du_projet_resnet_50_iteration-0_shuffle-1/"
model_path = '/home/emeline/Documents/PIDR/MouseTopView-MTV-2025-04-26/exported-models/DLC_MouseTopView_resnet_50_iteration-0_shuffle-1/'

dlc_proc = Processor()
dlc_live = DLCLive(model_path, processor=dlc_proc)
dlc_live.init_inference()

### Régalges caméra
cap = cv2.VideoCapture(0)   # 0 pour la caméra de l'ordi, sinon caméra externe souvent 2
cap.set(cv2.CAP_PROP_FPS, 60)
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS de la caméra: {fps}")

### Paramètres du cercle (calcul échelle)
real_circle_diameter_cm = 20  # Diamètre du cercle en cm
real_object_size_cm = 5  # Taille réelle de l'objet en cm
object_size_in_pixels = 50  # Taille de l'objet en pixels dans l'image
# Calcul de l'échelle (cm par pixel)
scale = real_object_size_cm / object_size_in_pixels
# Calcul du diamètre du cercle en pixels en fonction de la taille réelle
circle_diameter_pixels = real_circle_diameter_cm / scale  # Diamètre du cercle en pixels
# Distance à la caméra (ici tu es à 20 cm)
distance_to_camera_cm = 20


### Fonction pour dessiner l'intersection entre le cercle et la demi droite
def draw_ray_circle_intersection(frame, start, end, circle_center, radius, color=(0, 0, 255)):
    x0, y0 = start[:2]
    x1, y1 = end[:2]
    cx, cy = circle_center
    dx = x1 - x0
    dy = y1 - y0
    a = dx ** 2 + dy ** 2
    b = 2 * (dx * (x0 - cx) + dy * (y0 - cy))
    c = (x0 - cx) ** 2 + (y0 - cy) ** 2 - radius ** 2
    discriminant = b ** 2 - 4 * a * c
    # Tracer la demi-droite
    ray_end = (int(x0 + 1000 * dx), int(y0 + 1000 * dy))
    cv2.line(frame, (int(x0), int(y0)), ray_end, color, 2)
    if discriminant >= 0:
        sqrt_disc = np.sqrt(discriminant)
        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)
        for t in [t1, t2]:
            if t >= 0:
                ix = x0 + t * dx
                iy = y0 + t * dy
                cv2.circle(frame, (int(ix), int(iy)), 5, (255, 0, 0), -1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Obtenir la taille de la fenêtre
    height, width = frame.shape[:2]
    circle_center = (width // 2, height // 2)
    # Tracer les points de pose sur la fenêtre principale (video)
    pose_raw = dlc_live.get_pose(frame)
    pose = np.array(pose_raw).reshape(-1, 3)
    for i, point in enumerate(pose):
        x, y, likelihood = point
        if likelihood > 0.5:
            cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)
            cv2.putText(frame, f"{i}", (int(x) + 5, int(y) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    # Affichage vidéo avec les points
    cv2.imshow('Video Feed', frame)

    # Création d'une image avec un fond blanc pour la fenêtre "Circle and Ray"
    circle_frame = np.ones_like(frame) * 255  # Créer une image toute blanche (même taille que le frame)
    # Dessiner le cercle et la demi-droite sur le fond blanc
    cv2.circle(circle_frame, circle_center, int(circle_diameter_pixels // 2), (0, 255, 255), 2)
    # Tracer la demi-droite et l'intersection
    if pose.shape[0] >= 2 and pose[0][2] > 0.5 and pose[1][2] > 0.5:
        draw_ray_circle_intersection(circle_frame, pose[0], pose[1], circle_center, int(circle_diameter_pixels // 2))
    # Affichage de la fenêtre "Circle and Ray" avec fond blanc
    cv2.imshow('Circle and Ray', circle_frame)

    ### Arrêt
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()