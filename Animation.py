import matplotlib.animation as ani      
import matplotlib.pyplot as plt
import numpy as np 

# Initializing the objects
fig = plt.figure()
ax = plt.axes(xlim=(-11, 11), ylim=(-11,11))
Ram, = ax.plot([], [], marker="*", markerfacecolor="fuchsia", markersize=25, label="Ram")
success, = ax.plot([], [], color="red", linestyle="-", label="Success")
Shyam, = ax.plot([], [], marker="*", markerfacecolor="gold", markersize=25, label="Shyam")
failure, = ax.plot([], [], color="blue", linestyle="-", label="Failure")

# Defining the paths to move
x= np.linspace(-3*np.pi, 3*np.pi, 361)
y1= np.floor(x)
y2= np.floor(-x)

# Defining a function that takes care of motion frame by frame
def Life(i):
  Ram.set_data(x[i],y1[i])
  success.set_data(x[:i],y1[:i])
  Shyam.set_data(x[i],y2[i])
  failure.set_data(x[:i],y2[:i])
  return Ram, success, Shyam, failure,

# Calling the FuncAnimation
anim = ani.FuncAnimation(fig, Life, frames=len(x), interval=15, blit=True, repeat=True)
fig.suptitle("Life is all about the intersection\n of Success & Failure")
fig.patch.set_facecolor("lime")
fig.tight_layout()
plt.annotate("Courtesy of Rishikesh Jha", (8.5,-11))
plt.legend(loc="upper center")
plt.axis(False)
plt.show()
