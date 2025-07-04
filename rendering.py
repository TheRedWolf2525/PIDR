import cv2
import numpy as np

DEPL_LAT = 3
NB_LEDS = 30
LED_SPEED = 0.4

def polyg(n):
    L = [(1, 0)]
    for i in range(1,n):
        L.append((np.cos((2*i*np.pi)/n), np.sin((2*i*np.pi)/n)))
    return L

ledsPos = polyg(NB_LEDS)
centralPointIndex = 0
pc = 0

### Fonction pour dessiner l'intersection entre le cercle et la demi droite
def draw_ray_circle_intersection(frame, start, end, circle_center, radius, color=(0, 0, 255)):
    x0, y0 = start[:2]
    x1, y1 = end[:2]
    cx, cy = circle_center
    dx = x1-x0
    dy = y1-y0
    a = dx**2 + dy**2
    b = 2 * (dx*(x0-cx) + dy*(y0-cy))
    c = (x0-cx)**2 + (y0-cy)**2 - radius**2
    discriminant = b**2 - 4*a*c

    # Tracer la demi-droite
    ray_end = (int(x0 + 1000 * dx), int(y0 + 1000 * dy))
    cv2.line(frame, (int(x0), int(y0)), ray_end, color, 2)

    # Tracer point d'intersection
    intersect = None
    if discriminant >= 0:
        sqrt_disc = np.sqrt(discriminant)
        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)
        for t in [t1, t2]:
            if t >= 0:
                intersect = x0 + t*dx, y0 + t*dy
                cv2.circle(frame, (int(intersect[0]), int(intersect[1])), 5, (255, 0, 0), -1)
    return intersect

def render(frame, pose, circle_center, circle_diameter_pixels):
    global centralPointIndex, pc
    circle_frame = np.ones_like(frame) * 255
    cv2.circle(circle_frame, circle_center, int(circle_diameter_pixels // 2), (0, 255, 255), 2)
    for p in ledsPos:
        cv2.circle(circle_frame, (int(circle_center[0]+p[0]*circle_diameter_pixels//2), int(circle_center[1]+p[1]*circle_diameter_pixels//2)), 3, (0, 255, 0), 1)

    intersect = None
    if pose.shape[0] >= 2:
        validPoints = []
        for p in pose:
            if p[2] > 0.6:
                validPoints.append(p)
        if len(validPoints) >= 2 : intersect = draw_ray_circle_intersection(circle_frame, validPoints[1], validPoints[0], circle_center, int(circle_diameter_pixels // 2))
    
    if intersect != None:
        theta = np.arctan2(intersect[1]-circle_center[1], intersect[0]-circle_center[0])
        if (theta < 0):
            theta += 2* np.pi
        
        centralPointIndex = round(theta/(2*np.pi/NB_LEDS)) % NB_LEDS
    
    for k in range(centralPointIndex-DEPL_LAT, centralPointIndex+DEPL_LAT+1):
        cv2.circle(circle_frame, (int(circle_center[0]+ledsPos[k%NB_LEDS][0]*circle_diameter_pixels//2), int(circle_center[1]+ledsPos[k%NB_LEDS][1]*circle_diameter_pixels//2)), 4, (127, 0, 255), 1)
    
    offset = int((DEPL_LAT + 0.5) * (np.sin(pc) + 1)) % NB_LEDS
    indexLed = (centralPointIndex + offset - DEPL_LAT) % NB_LEDS
    pc = (pc+LED_SPEED) % (2*np.pi)
    cv2.circle(circle_frame, (int(circle_center[0]+ledsPos[indexLed][0]*circle_diameter_pixels//2), int(circle_center[1]+ledsPos[indexLed][1]*circle_diameter_pixels//2)), 4, (127, 0, 255), -1)

    cv2.imshow('Circle and Ray', circle_frame)
