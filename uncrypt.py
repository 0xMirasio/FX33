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
        res.append(errcd[i])
    k = len(res)
    del res[k-1]
    return res

#--------------------CONVERSION BaseFX----------
def conv_FX(dep):
    base10char = []
    for i in range(len(dep)):
        char = dep[i]
        new_char = char[0]
        res=0
        for k in range(len(new_char)):
              res = res+ fx.FX33_reverse(str(new_char[k]))
        base10char.append(res)
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
        
    
    
drr = input("Code encrypté ? >> ")  
primary_key = int(input("clé primaire ? >> "))
drr_1 = separ(drr)
drr_2 = conv_FX(drr_1)
drr_3 = binary_decompo(drr_2)
res_f = somme_fibo(drr_3)
mdp_decode = decode(res_f)
print(mdp_decode)