import cv2
import numpy as np

DEPL_LAT = 3
NB_LEDS = 20
LED_SPEED = 3000

def polyg(n):
    L = [(1, 0)]
    for i in range(1,n):
        L.append((np.cos((2*i*np.pi)/n), np.sin((2*i*np.pi)/n)))
    return L

ledsPos = polyg(NB_LEDS)

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

def render(frame, pose, circle_center, circle_diameter_pixels):
    circle_frame = np.ones_like(frame) * 255
    cv2.circle(circle_frame, circle_center, int(circle_diameter_pixels // 2), (0, 255, 255), 2)
    for p in ledsPos:
        cv2.circle(circle_frame, (int(p[0]*circle_diameter_pixels), int(p[1]*circle_diameter_pixels)), 3, (0, 255, 0), 1)

    if pose.shape[0] >= 2 and pose[0][2] > 0.5 and pose[1][2] > 0.5:
        draw_ray_circle_intersection(frame, pose[1], pose[0], circle_center, int(circle_diameter_pixels // 2))
    
    cv2.imshow('Circle and Ray', circle_frame)
