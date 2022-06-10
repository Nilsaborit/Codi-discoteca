from os import system, name
def clear(): system('cls') if name == 'nt' else system('clear')
import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.40.67",
    user="asix",
    password="asix",
    database="escodisco"
)

mycursor = mydb.cursor()

def continuar():
    input("\nPrem la tecla enter per continuar...")

def llegirOpcio(min,max):
    opcio=min-1
    while opcio<min or opcio>max:
        opcio=int(input(f"({min},{max}): "))
    return opcio

    continuar()



def guions():
    print('-'*25)

def mostrarMenu():
    guions()
    print("base de dades".upper())
    guions()
    print('\n1) Arribada Clients\n2) Sortida client\n3) Assignar consumició\n4) Modificar SEXE\n5) Visualitzar els clients registrats\n6) Exit')

def arribada():
    clear()
    guions()
    print("Introdueix les dades del client".upper())
    guions()
    nom = input("Introdueix el Nom: ")
    cognom = input("Introdueix els cognoms: ")
    dni = input("Introdueix el DNI: ")
    sexe = input("Introdueix el sexe: ")
    print("Introdueix la teva edat:", end=(" "))
    edat = llegirOpcio(18,100)
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO Clients (Nom, Cognoms, DNI, Sexe, Edat) VALUES (%s, %s, %s, %s, %s)", (nom,cognom,dni,sexe,edat))
    mydb.commit()
    mycursor.execute("select ID from Clients where DNI = (%s)", (dni,))
    dataset = mycursor.fetchall()
    with open('registreClients.txt','a+',encoding='utf-8') as wat:
        wat.seek(0)
        wat.write(f'ID={dataset[0]} | {nom} | {cognom} | {dni} | {edat}\n')
    continuar()
    clear()

def sortida(total):
    clear()
    guions()
    print("Sortida client".upper())
    guions()
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM Clients")
    dataset = mycursor.fetchall()
    print('ID: \t\tNOM:\t\t       COGNOM:\t\t          DNI:\n')    
    for asset in dataset:
        print(f'{str(asset[0]).ljust(20)}{str(asset[1]).ljust(26)}{str(asset[2]).ljust(26)}{str(asset[3]).ljust(26)}')

    dni = input("\nIntrodueix el num(ID) de el client que surt: ")

    mycursor = mydb.cursor()
    mycursor.execute("select quant*Preu_Unitat as fii from Consumicions where client = (%s)", (dni,))
    dataset = mycursor.fetchall()
    nuum = 0
    
    for asset in dataset:
        nuum += asset[0]
    total += nuum
    print(f"\nDiners a pagar de el client ({dni}): {nuum}")
    
    mycursor = mydb.cursor()
    mycursor.execute("DELETE from Consumicions where Client = (%s)", (dni,))
    mycursor.execute("DELETE from Clients where ID = (%s)", (dni,))
    mydb.commit()
    continuar()
    clear()
    return total

def consu(y):
    clear()
    guions()
    print("Assignar consumició".upper())
    guions()
    print("\nProducte:                 Preu:".upper())
    print("\n         (1) Refresc           5€")
    print("         (2) Xupito            3€")
    print("         (3) Combinat          8€")
    print("         (4) Aigua             4€\n")

    mycursor = mydb.cursor()
    print("Introdueix el numero de producte", end=(" "))
    article = llegirOpcio(1,4)
    print("Introdueix la quantitat", end=(" "))
    quanti = llegirOpcio(1,10)
    continuar()
    clear()
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM Clients")
    dataset = mycursor.fetchall()
    print('ID: \t\tNOM:\t\t       COGNOM:\t\t          DNI:\n')    
    for asset in dataset:
        print(f'{str(asset[0]).ljust(20)}{str(asset[1]).ljust(26)}{str(asset[2]).ljust(26)}{str(asset[3]).ljust(26)}')

    dni = input("\nIntrodueix el num(ID) de el client que li vols assignar: ")
    with open('registreConsumicions.txt','a+',encoding='utf-8') as wat:
        wat.seek(0)
        if y == 0:
            dia = input("Introdueix el la data d'avui: ")
            wat.write( '\n----------------------------------------------\n')
            wat.write(  f'                   {dia}                      \n')
            wat.write( '----------------------------------------------')
        if article== 1:
            mycursor.execute("INSERT INTO Consumicions (Article, Quant, Preu_Unitat, Client) VALUES ('Refresc', %s, 5, %s )", (quanti,dni,))
            wat.write(f'\n{y} | Refresc | {quanti} | 5€ | {dni} ')

        if article== 2:
            mycursor.execute("INSERT INTO Consumicions (Article, Quant, Preu_Unitat, Client) VALUES ('Xupito', %s, 3, %s)", (quanti,dni,))
            wat.write(f'\n{y} | Xupito | {quanti} | 3€ | {dni} ')

        if article== 3:
            mycursor.execute("INSERT INTO Consumicions (Article, Quant, Preu_Unitat, Client) VALUES ('Combinat', %s, 8, %s)", (quanti,dni,))
            wat.write(f'\n{y} | Combinat | {quanti} | 8€ | {dni} ')

        if article== 4:
            mycursor.execute("INSERT INTO Consumicions (Article, Quant, Preu_Unitat, Client) VALUES ('Aigua', %s, 4, %s)", (quanti,dni,))
            wat.write(f'\n{y} | Aigua | {quanti} | 8€ | {dni} ')
    
    dataset = mycursor.fetchall()
    mydb.commit()
    
    continuar()
    clear()
    return y

def modificar():
    clear()
    guions()
    print("Modificar SEXE de client".upper())
    guions()
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM Clients")
    dataset = mycursor.fetchall()
    print('ID: \t\tNOM:\t\t       COGNOM:\t\t          DNI:\n')    
    for asset in dataset:
        print(f'{str(asset[0]).ljust(20)}{str(asset[1]).ljust(26)}{str(asset[2]).ljust(26)}{str(asset[3]).ljust(26)}')

    dni = input("\nIntrodueix el num(ID) de el client que vols canviar el sexe: ")
    sx = input("\nIntrodueix el nou sexe: ")

    mycursor = mydb.cursor()
    mycursor.execute("UPDATE Clients SET Sexe = %s WHERE ar_cod = %s", (sx,dni,))
    mydb.commit()
    continuar()
    clear()

def visCli():
    clear()
    guions()
    print("Visualitzar els clients registrats:".upper())
    guions()
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM Clients")
    dataset = mycursor.fetchall()
    print('ID: \t\tNOM:\t\t       COGNOM:\t\t          DNI:\n')    
    for asset in dataset:
        print(f'{str(asset[0]).ljust(20)}{str(asset[1]).ljust(26)}{str(asset[2]).ljust(26)}{str(asset[3]).ljust(26)}')
    continuar()
    clear()

opcio=int (0)
y=int(0)
total = int(0)
while opcio!=6:
    mostrarMenu()
    opcio=llegirOpcio(1,6)
    match opcio:
        case 1: arribada()
        case 2: 
            total = sortida(total)
        case 3: 
            y = consu(y)
            y+=1
        case 4: modificar()
        case 5: visCli()

print(f'\nBeneficis totals (Nomes es conten si el client a sortit): {total}\n')
print('\nA reveure guap@/e¡!¡!')