# -*- coding: utf-8 -*-

import numpy as np

nfil=int(input("Cuantos días: "))
ncol=int(input("Cuantas Vacas: "))
M=np.zeros((nfil,ncol))
print(M)

for i in range(nfil):
  for j in range(ncol):
    M[i][j]=int(input("Cantidad de litros de leche: "))

print(M)

Sume=lambda M: [ sum(i) for i in M]
x=Sume(M)
y=[]
y=np.zeros(nfil)
y[0]=3
print(M)
print("**************")
for i in range(nfil):
  print("Leche "+str(i+1)+" dia: "+str(x[i]))

for i in range(nfil):
  print(M[i])
  z=max(M[i])
  w=list(M[i])
  y[i]=w.index(z)
print("**************")
for i in range(nfil):
  print("El "+str(i+1)+" dia la vaca que mas dio leche fue="+str(y[i]+1))