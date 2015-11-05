import numpy as np
import matplotlib.pyplot as plt
import sys


entrada=str(sys.argv[1])
ARCHIVO=np.loadtxt(open(entrada,"r"))
ids=np.size(ARCHIVO[:,0])
mag=np.size(ARCHIVO[0,:])-5

ID=ARCHIVO[:,0]

#comienza la lectura del archivo 

for i in range(len(ID)):

    nombre="ID"+str(int(ID[i]))+".dat"

    archivo=open(nombre,"w")
    
    Mag=ARCHIVO[i,:]

    archivo.write("#"+str(int(ID[i])) +" mag error\n" )

    for j in range((len(Mag)-5)/2):

        escribe=str(Mag[3+2*j])+" "+str(Mag[4+2*j])

        archivo.write(escribe+"\n")

    archivo.close()


        





