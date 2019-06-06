"""
Created on Wed May 22 10:18:58 2019

@author: thibault.poncetta
"""

#Projet d'encodage FX33 v1.2
"""
projet démarré : 22/05/19
objectif:  encoder grace au suite de Fibonnaci un string en un code encodé undéchiffrable
un seul moyen de déchiffrer: posséder la clé primaire défini par l'utilisateur

LISTE DES operations:
    1-recupération du MDP utilisateur
    2-décomposition en caractéere du mot de passe
    3- conversion en décimal (TABLE ASCII) de chaque caractère
    4- F-decomposition de chaque caractère(transformée en base10)
    5- Encodage binaire de la F-decomposition
    6 - Passage de base2 (bin) à une base10 (pour chaque caractère)
    7- passage en FX33 encodé pour les décimal<80(max de la TABLE FX33) et génération aléatoire de décomposition
    pour les décimal>80 à l'aide de la clé primaire
    8-assemblage final et affichage du mot MDP entièrement encodé
"""

#--------------------INIT----------
import sys
import FX33_table as fx
import random
#on crée une suite de fibonnaci
def fibonnaci_suite():
    fibo = [0,1]
    for i in range(1,12):
        fibo.append(fibo[i]+fibo[i-1])
    return fibo
    
    
#--------------------CONVERSION STRING-ENCODAGE-BINAIRE-------------------
def final(entry):
    code=[]
    if type(entry) == str:
        value = string_decomposition(entry)
        value_dec = conv_FX(value)
        for i in range(len(value_dec)):
            code.append(encodage(value_dec[i]))
    else:
        print("usage : string or int to encode")
    return code

#-------------------ENCODAGE_BINAIRE_F_DECOMPOSITION--------------------------
def encodage(arr):
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
    
#-------------decomposition string---------------
def string_decomposition(arr_str):
    fin = []
    for i in range(len(arr_str)):
        fin.append(arr_str[i])
    return fin
#----------------CONVERSION ASCII-------------
def conv_FX(err):
    FX_code =[]
    for i in range(len(err)):
        FX_code.append(ord(err[i]))
    return FX_code

#---------------CONVERSION CODE-BASE10--------------    
def conv_base10(err):
    base10=[]
    for i in range(len(err)):
        val=0
        for k in range(len(err[i])):
            val = str(val) + str(err[i][k])
        base10.append(int(val,2))
    return base10
#-------------ENCODAGE ASCII CODE-BASE10- FINAL
def final_code(err,first_key):
    mdp_encode=""
    for i in range(len(err)):
        if err[i] <=80:
            mdp_encode = mdp_encode+ fx.FX33(err[i])
        else:
            mdp_encode = mdp_encode+ primary(err[i],first_key)    
    return mdp_encode
#------------------VERIF CLE PRIMAIRE VALIDE-----------------------------------------
def primary_key(first_key):
    if type(first_key) != int:
        print("clé d'entier 5 chiffre!")
        sys.exit(0)
    else:
        return first_key
#GENERATION ENCODAGE CLE PRIMARE
def primary(err,first_key):
    seuil1= 0
    seuil2= 80
    decompo = ["■"]
    val=decompo[0]
    while True:
       if err>80:
           vale = random.randint(seuil1,seuil2)
           err = err - vale
           decompo.append(vale)
       else:
           decompo.append(err)
           break
    for i in range(1,len(decompo)):
        val = str(val)  + fx.FX33(int(decompo[i]))
    val = val + "▓"
    return val
           
    

mdp = str(input("votre phrase à  encoder? >> "))
first_key = int(input("Votre clé primaire ? >> "))
mpd_code = final(mdp)
mpd_code_10 = conv_base10(mpd_code)
mdp_encode = final_code(mpd_code_10,first_key)
print(mdp_encode)
