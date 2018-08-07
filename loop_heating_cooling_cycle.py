"""
Draw heating and cooling cycle of a coronal loop
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

patch_kwargs = {'edgecolor': 'k', 'lw': 1, 'facecolor': 'none'}

# TODO: arcs for cycle arrows
# TODO: illustrations for loop physics


def draw_loop(center, width=1, height=1,):
    # Create loop
    inner_width, inner_height = 0.9*width, 0.9*height
    arc1 = patches.Arc(center, width, height, theta1=90, theta2=180, **patch_kwargs)
    arc2 = patches.Arc(center, inner_width, inner_height, theta1=90, theta2=180, **patch_kwargs)
    cap_width = 0.1*width/2
    cap_height = cap_width/2

    cap1 = patches.Ellipse((center[0]-(width/2 + inner_width/2)/2, center[1]),
                           cap_width, cap_height,
                           **patch_kwargs)
    cap2 = patches.Ellipse((center[0], center[1]+(height/2 + inner_height/2)/2),
                           cap_height, cap_width,
                           **patch_kwargs)
    # Draw loop
    ax.add_patch(arc1)
    ax.add_patch(arc2)
    ax.add_patch(cap1)
    ax.add_patch(cap2)

fig = plt.figure()
ax = fig.gca()
#ax.axis('off')
draw_loop((-.5, 0))
draw_loop((1.5,0))
draw_loop((0.5,1))
draw_loop((0.5,-1))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', 'datalim')
plt.show()