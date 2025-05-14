import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier avec en-têtes hiérarchiques
df = pd.read_csv("/home/emeline/Documents/PIDR/Résul_40000/v1DLC_resnet50_VESPAMay8shuffle1_40000_filtered.csv", header=[0, 1, 2])
# "/home/emeline/Documents/PIDR/Résul_40000/v1DLC_resnet50_VESPAMay8shuffle1_40000_filtered.csv"
# Liste des bodyparts à tracer
bodyparts = ['bodypart1', 'bodypart2', 'bodypart3']
scorer = df.columns.levels[0][0]  # ex: 'DLC_resnet50_VESPAMay8shuffle1_40000'

# Tracer les trajectoires XY de chaque point
plt.figure(figsize=(6, 6))
for bp in bodyparts:
    x = df[(scorer, bp, 'x')]
    y = df[(scorer, bp, 'y')]
    plt.plot(x, y, label=bp)
gi
plt.xlabel('x (pixels)')
plt.ylabel('y (pixels)')
plt.title('Trajectoires des points')
plt.legend()
plt.gca().invert_yaxis()  # Pour correspondre à l'image vidéo
plt.grid()
plt.show()

plt.figure(figsize=(8, 4))
for bp in bodyparts:
    likelihood = df[(scorer, bp, 'likelihood')]
    plt.plot(likelihood, label=f'Likelihood {bp}')

plt.xlabel('Frame')
plt.ylabel('Confiance')
plt.title('Probabilités de détection')
plt.ylim(0, 1.05)
plt.grid()
plt.legend()
plt.show()
