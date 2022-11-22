import random


###############
## FUNCTIONS ##
###############

def get_char(car_spe):
    
    dico = {"alphabet_low":["a","b","c","d","e","f","g","h","i","j","k","l","m",
                            "n","o","p","q","r","s","t","u","v","w","x","y","z"],
            "alphabet_up":["A","B","C","D","E","F","H","I","J","K","K","L","M",
                           "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
            "numbers":["0","1","2","3","4","5","6","7","8","9"]}

    if car_spe == False:
        dico["car_spe"] = []
    else:
        print("Entrez le nombre correspondant a l'ensemble des caractere que vous souhaitez utilisez")
        print('1: - _ ')
        print('2: - _ /')
        print('3: - _ / .')
        print('4: - _ / . + *')
        print('5: - _ / . + *  $')
        print('6: - _ / . + *  $ ( ) [ ]')
    
        rep2 = input()
        if rep2 not in ["1","2","3","4","5","6"]:
            i = 1
            while rep2 not in ["1","2","3","4","5","6"]:
                print("Aller retape un nombre correcte")
                rep2 = input()
                if i == 5:
                    exit("Trop d'erreur")
                i += 1
                
        if rep2 == "1":
            dico["car_spe"] = ["-", "_"]
        elif rep2 == "2":
            dico["car_spe"] = ["-","_","/"]
        elif rep2 == "3":
            dico["car_spe"] = ["-","_","/","."]
        elif rep2 == "4":
            dico["car_spe"] = ["-","_","/",".","+","*"]
        elif rep2 == "5":
            dico["car_spe"] = ["-","_","/",".","+","*","$"]
        elif rep2 == "6":
            dico["car_spe"] = ["-","_","/",".","+","*","$","(",")","[","]"]
                
    return dico

def get_lenght():
    
    print("Entrez la taille minimum du mot de passe")
    rep3 = input()
    try:
        rep3 = int(rep3)
    except:
        print("Il nous faut un nombre entier (1, 2...)")
        print(f"Vous avez entré : {rep3}")
        rep3 = 8
        print(f"La taille minimum est fixée à 8")
        
    print("Entrez la taille maximum du mot de passe")
    rep4 = input()
    try:
        rep4 = int(rep4)
    except:
        print("Il nous faut un nombre entier (1, 2...)")
        print(f"Vous avez entré : {rep4}")
        rep4 = 16
        print(f"La taille minimum est fixée à 16")
        
    return rep3, rep4
    
def get_password(dico, mini, maxi):
    
    mdp = []
    
    m = random.randint(mini, maxi)
    
    alphabet_low = dico["alphabet_low"]
    random.shuffle(alphabet_low)
    mdp.append(random.choice(alphabet_low))
    
    alphabet_up = dico["alphabet_up"]
    random.shuffle(alphabet_up)
    mdp.append(random.choice(alphabet_up))
    
    numbers = dico["numbers"]
    random.shuffle(numbers)
    mdp.append(random.choice(numbers))
    
    complete = alphabet_up + numbers + alphabet_low
    random.shuffle(complete)
    
    if dico["car_spe"] != []:
        car_spe = dico["car_spe"]
        random.shuffle(car_spe)
        mdp.append(random.choice(car_spe))
        
        complete += car_spe
        
    while len(mdp) < m:
        random.shuffle(complete)
        mdp.append(random.choice(complete))
    
    random.shuffle(mdp)   
    return "".join(mdp)
            
        
        
        
          

##########
## MAIN ##
##########

print("Voulez vous utilisez des caracteres speciaux (oui, non) ?")
rep1 = input()

if rep1 not in ["oui", "non"]:
    exit(f"On a dit oui ou non pas : {rep1}")
elif rep1 == "oui":
    car_spe = True
    
else:
    car_spe = False
    
dico = get_char(car_spe)
mini, maxi = get_lenght()

print("Combien de mot de passe vous voulez générer ?")
rep5 = input()
try:
    rep5 = int(rep5)
except:
    print("1 mot de passe sera généré")
    rep5 = 1
    
if rep5 == 1:
    mdp = get_password(dico, mini, maxi)
    print(mdp)
else:
    print("Les mots de passe seront écrit dans le fichier suivant :")
    print("MDP.txt")
    list_mdp = []
    for i in range(rep5):
        mdp = get_password(dico, mini, maxi)
        list_mdp.append(mdp)
        
    with open("MDP.txt", "w") as filout:
        for mdp in list_mdp:
            filout.write(mdp + "\n")
            
    print("Les Mots de passe ont été générés")