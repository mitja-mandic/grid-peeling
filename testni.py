import matplotlib.pyplot as plt
from razredi import Tocka
from jarvis_march import grid_peel_jarvis_enakomerna
from graham_scan import grid_peel_graham_enakomerna
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

sez_x = []
sez_y = []
sez_z = []




for i in range(3,50):
    for j in range(3,50):
        st = grid_peel_graham_enakomerna(i,j)
        sez_x.append(i)
        sez_y.append(j)
        sez_z.append(len(st[1]))

#seznam_x = sez_x
#seznam_y = sez_y
#seznam_z = sez_z

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(sez_x,sez_y,sez_z)
plt.show()
