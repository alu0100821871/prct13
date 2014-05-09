#! /usr/bin/python
#! encoding: UTF-8

import matplotlib.pyplot as pl

X = [1, 2, 3, 4, 5, 6]
Y1 = [20, 80, 100, 100, 100, 100]
Y2 = [0, 10, 45, 100, 100, 100]
Y3 = [0, 0, 20, 85, 100, 100]
Y4 = [0, 0, 10, 45, 70, 90]
Y5 = [0, 0, 0, 10, 50, 75]
Y6 = [0, 0, 0, 5, 35, 60]
Y7 = [0, 0, 0, 0, 20, 40]

xt = [1, 2, 3, 4, 5, 6, 7]
yt = [0, 0.002, 0.005, 0.09, 0.156, 0.21, 0.265]

pl.subplot (2,1,1)

pl.plot(X,Y1, 'c--')
pl.plot(X,Y2, 'go-') 
pl.plot(X,Y3, 'y*-') 
pl.plot(X,Y4, 'md-')
pl.plot(X,Y5, 'ks-') 
pl.plot(X,Y6, 'r-')
pl.plot(X,Y7, 'bp-') 

pl.xlim(0.0,7.0)
pl.ylim(-10.0,110.0)

pl.xticks([1,2,3,4,5,6], [r'$1e-4$',r'$1e-5$',r'$1e-6$',r'$1e-7$',r'$1e-8$', r'$1e-9$'], rotation = 45)
pl.yticks( [0, 20, 40, 60, 80, 100],[r'$0$',r'$20$',r'$40$',r'$60$',r'$80$', r'$100$'])

pl.legend(['10','50','100','250','500','750','1000'], loc = 0, numpoints = 1)

pl.title('Porcentaje de errores')
pl.xlabel('Umbral')
pl.ylabel('Porcentaje')




pl.subplot (2,1,2)

pl.plot(xt,yt, 'mo-') 

pl.xticks([1, 2, 3, 4, 5, 6, 7], [r'$10$',r'$50$',r'$100$',r'$250$',r'$500$', r'$700$', r'$1000$'])
pl.yticks([0, 0.05, 0.1, 0.15, 0.2, 0.25], [r'$0.0$',r'$0.005$',r'$0.01$',r'$0.15$',r'$0.2$', r'$0.3$'])


pl.xlabel('Intervalos')
pl.ylabel('Tiempo')

pl.xlim(0,8)
pl.ylim(-0.05,0.3)

pl.savefig("graficapi.eps", dpi=72)
pl.show()

