
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import sys


#This is main function that calls the argument from command line
def main(argv):
    #open from command line
    with open(sys.argv[0], 'w') as out_file:
        y = np.random.normal(0, 1, 1000000).cumsum(axis=0)
        x = np.arange(y.size) + 1
        out_file.write("{},{}\n".format(x, y))


    
    


    fig, ax = plt.subplots()
    
    line, = ax.plot([], [],'k-')
    ax.margins(0.05)
    a=max(y)
    b=min(y)
    ax.set_xlabel('max={}'.format(a))
    ax.set_ylabel('min={}'.format(b))

    #Initialize
    def init():
        line.set_data(x[:2],y[:2])
        return line,
 
        
    #This is animation function which animates and displays
    def animate(i):
        win = 300
        imin = min(max(0, i - win), x.size - win)
        xdata = x[imin:i]
        ydata = y[imin:i]
        line.set_data(xdata, ydata)
        ax.relim()
        ax.autoscale()
        
       
        
        return line
   
    anim = animation.FuncAnimation(fig, animate,init_func=init, interval=25)
   


    plt.show()

if __name__=="__main__":
    main(sys.argv[1:])


