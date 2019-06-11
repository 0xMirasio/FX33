"""
Created on Wed May 22 10:18:58 2019
@author: thibault.poncetta
Projet d'encodage FX33 v1.2
projet démarré : 22/05/19
"""
#ERR : fichier a encoder
#key_primary : clé primaire => clé unique obligatoire pour déchifrer le code
#--------------------INIT LIBRAIRIE/MODULE----------
import FX33_table as fx
import random
import os
#--------------------INIT FICHIER----------
def ouv(file):
    f=open(file,"rb")
    num=list(f.read())
    f.close()
    return num
  #--------------------GENERATION Suite fibonacie----------
def fibonnaci_suite():
    fibo = [0,1]
    for i in range(1,19):
        fibo.append(fibo[i]+fibo[i-1])
    return fibo

#-------------------ENCODAGE_BINAIRE_F_DECOMPOSITION--------------------------
def fibo_encodage(arr):
    fibo_temp,fibo_code= [],[]
    val=arr
    fibo = fibonnaci_suite()
    while val != 0:
        i=0
        while True:
            if val < fibo[i]:
                fibo_temp.append(fibo[i-1])
                val = val - fibo[i-1]
                break
            else:
                i=i+1
    for i in range(len(fibo)):
        if fibo[i] in fibo_temp:
            fibo_code.append(1)
        else:
            fibo_code.append(0)
    return fibo_code

#---------------CONVERSION TABLE ASCII--------------    
def conv_ASCII(err):
    base10=[]
    val=""
    for i in range(len(err)):
        val = str(val) + str(err[i])
    base10.append(int(val,2))
    return base10

#-------------Sum of All Caracters encoded
def final_code(err,key_primary):
    mdp_encode=""
    for i in range(len(err)):
            mdp_encode = mdp_encode+ gen(err[i],key_primary)
    return mdp_encode

#GENERATION PROBABILITE / EXTENSION => CLE PRIMAIRE/SECONDAIRE
def gen(err,key_primary):
    s1= 0
    s2= 80
    sep_start = "■"
    sep_end = "▓"
    val = []
    res=sep_start
    while True:
        value = random.randint(s1,s2)
        err = err - value
        if err==0:
            val.append(value)
            break
        elif err<0:
            err = err+value
        else:
            val.append(value) 
    for i in range(len(val)):
        res = str(res)  + fx.FX33(int(val[i]))
    res = res + sep_end
    return res

file = input("File to encode ? >> ")          
data= ouv(file)
key_primary = int(input("primary key ? >> "))
print("encoding, can take some time... ")
code=[]
for i in range(len(data)):
    err1= fibo_encodage(data[i])
    err_2 = conv_ASCII(err1)
    code.append(final_code(err_2,key_primary))
file_encrypted = file+".fx33"
fichier = open(file_encrypted, "wb")
for i in range(len(code)):
    a= code[i]
    fichier.write(a.encode("utf-8"))
    
fichier.close()
os.remove(file)
print("finished!")