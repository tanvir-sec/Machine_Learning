import matplotlib.pyplot as plt

x1=[1,2,3,4,5]
x2=[1,0,1,4,9]
y1=[2,3,4,6,7]
y2=[1,4,7,8,2]
plt.figure(figsize=(10,5))

plt.subplot(2,2,1)
plt.plot(x1,y2,color='black',linestyle='dashdot')
plt.title('plot 1')

plt.subplot(2,2,2)
plt.plot(x2,y1,color='blue',linestyle='dashdot')
plt.title('plot 2')

plt.subplot(2,2,3)
plt.plot(x2,y2,color='red',linestyle='dashdot')
plt.title('plot 3')

plt.subplot(2,2,4)
plt.plot(x1,y1,color='black',linestyle='dashdot')
plt.title('plot 4')
plt.show()