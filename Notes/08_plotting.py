# Plotting
# 3/21/19
# SAMMY KAGAN GOT IN TO POMONA COLLEGE AND HE WON'T STOP BEING DISTRACTED BY IT

import matplotlib.pyplot as plt
import random

plt.figure(1) # create a new window

plt.plot([1, 2, 4, 4]) # plots y against the index
plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) # plot (x_data, y_data)

plt.figure(2) # makes a second window

x1 = [x for x in range(1, 101)]
y1 = [y ** 2 for y in x1]

plt.plot(x1, y1)

x2 = [x for x in range(1, 101)]
y2 = [random.randrange(1000) for y in range(100)]

plt.plot(x2, y2, color='green', marker='+', markersize=10, linestyle = '--', alpha=0.5)

# title axes label unit numbers key
plt.xlabel('time (seconds)', color='red', fontsize=10)
plt.ylabel('intensity (dB)')
plt.title('Example Plot')
plt.axis([0, 50, 0, 1000]) # [xmin, xmax, ymin, ymax]

plt.show()
