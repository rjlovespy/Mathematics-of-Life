import matplotlib.animation as ani      
import matplotlib.pyplot as plt
import numpy as np 


x= np.linspace(-3*np.pi, 3*np.pi, 361)
y1= np.floor(x)
y2= np.floor(-x)


fig = plt.figure()
ax = plt.axes(xlim=(-10,10), ylim=(-10,10))
Ram, = ax.plot(x[0], y1[0], marker="*", markerfacecolor="fuchsia", markersize=25, label="Ram")
success, = ax.plot(x[0], y1[0], color="red", linestyle="-", label="Success")
Shyam, = ax.plot(x[0], y2[0], marker="*", markerfacecolor="gold", markersize=25, label="Shyam")
failure, = ax.plot(x[0], y2[0], color="blue", linestyle="-", label="Failure")


def update(i):
  Ram.set_data(x[i],y1[i])
  success.set_data(x[:i],y1[:i])
  Shyam.set_data(x[i],y2[i])
  failure.set_data(x[:i],y2[:i])
  return Ram, success, Shyam, failure,


anime = ani.FuncAnimation(fig, update, frames=len(x), interval=15, blit=True, repeat=True)
fig.suptitle("Life is all about the intersection\n of Success & Failure")
fig.patch.set_facecolor("lime")
ax.axis(False)
ax.annotate("Courtesy of Rishikesh Jha", (-1.5,-9.5))
plt.legend(loc="upper center")
# anime.save("mathematics_of_life.gif")
plt.show()