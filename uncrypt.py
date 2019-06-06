# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:15:53 2019

@author: thibault.poncetta
reverse script pour le codage FX33
"""
import FX33_table as fx
#--------------------CREATION DE LA SUITE DE FIBONNACI-----------
def fibonnaci_suite():
    fibo = [0,1]
    for i in range(1,12):
        fibo.append(fibo[i]+fibo[i-1])
    return fibo
    

#--------------------RECUPERATION DES CARACTERE 1par1----------

def separ(err):
    errcd,res=[],[]
    errc = err.split("▓")
    for i in range(len(errc)):
        errcd.append(errc[i].split("■"))
        if errcd[i][0] == "":
              del errcd[i][0]
    for i in range(len(errc)):
        if len(errcd[i])>1:
            errcd[i][0] = errcd[i][0] + "solo"
            res.append(errcd[i][0])
            res.append(errcd[i][1])
        else:
            res.append(errcd[i])
    return res

#--------------------CONVERSION STRING EN BASE10----------
def conv_base10(dep):
    base10char = []
    for i in range(len(dep)):
        char = dep[i]
        new_char = char[0]
        char10=0
        if "solo" in new_char:
            a=ord(new_char-"solo")
            print(a)
            base10char.append(a)
        else:
           for k in range(len(new_char)):
               char10 = char10+ fx.FX33_reverse(str(new_char[k]))
           base10char.append(char10)
    return base10char
    

#--------------------DECOMPOSITION EN BINAIRE----------
def binary_decompo(dec):
     res=[]
     for i in range(len(dec)):
         res_bin = bin(dec[i])
         res.append(res_bin.replace("0b",""))
     return res

     
#--------------------RECUPERATION NOMBRE FIBONNACI----------
def somme_fibo(bine):
    res_fin = []
    fibo = fibonnaci_suite()
    for i in range(len(bine)):
        res=0
        car = bine[i]
        car_fin = "0"*(13-len(car)) + car
        for j in range(len(car_fin)):
            if car_fin[j] == "1":
                res = res + fibo[j]
        if car_fin[1] == car_fin[2] == "1":
                    res=res-1        
        res_fin.append(res)
    return res_fin

def decode(err):
    res=""
    for i in range(len(err)):
        res = res+ chr(err[i])
    return res
        
    
    
entry = input("Code encrypté ? >> ")  
primary_key = int(input("clé primaire ? >> "))
dep = separ(entry)
dec = conv_base10(dep)
bine = binary_decompo(dec)
res_f = somme_fibo(bine)
mdp_decode = decode(res_f)
print(mdp_decode)