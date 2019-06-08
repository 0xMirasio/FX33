"""
Created on Wed May 22 10:18:58 2019
@author: thibault.poncetta

Projet d'encodage FX33 v1.2
projet démarré : 22/05/19
"""
#ERR : phrase/mdp a encodé
#key_primary : clé primaire => clé unique obligatoire pour déchifrer le code
#key_secondary: clé secondaire => taux d'extension de ERR
#--------------------INIT LIBRAIRIE/MODULE----------
import FX33_table as fx
import random
#--------------------GENERATION Suite fibonacie----------
def fibonnaci_suite():
    fibo = [0,1]
    for i in range(1,12):
        fibo.append(fibo[i]+fibo[i-1])
    return fibo

#--------------------GENERATION LISTE ERR----------
def string_decomposition(err):
    res= []
    for i in range(len(err)):
        res.append(err[i])
    return res
    
#---------------------CONV TABLE FX -------------
def conv_FX(err):
    FX_code =[]
    for i in range(len(err)):
        FX_code.append(ord(err[i]))
    return FX_code   


#--------------------CONVERSION STRING-ENCODAGE-BINAIRE-------------------
def binary_code(entry):
    code=[]
    value = string_decomposition(entry)
    value_dec = conv_FX(value)
    for i in range(len(value_dec)):
        code.append(fibo_encodage(value_dec[i]))
    return code

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
    for i in range(len(err)):
        val=0
        for k in range(len(err[i])):
            val = str(val) + str(err[i][k])
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
           

err = str(input("Data to encode? >> "))
key_primary = int(input("primary key ? >> "))
err_1 = binary_code(err)
err_2 = conv_ASCII(err_1)
err_final = final_code(err_2,key_primary)
print(err_final)
