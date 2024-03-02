import random

x = 0 #DEFINIR QUAL O VALOR MINIMO DO NUMERO ALEATORIO GERADO (antes da soma)
y = 50 #DEFINIR QUAL O VALOR MAXIMO DO NUMERO ALEATORIO GERADO (antes da soma)
file = "data.txt"
timesitwillrun = 1000 #DEFINIR A QUANTIDADE DE NUMEROS ALEATÓRIOS GERADOS (depois da soma)

waittostart = input(f"The code will generate random numbers between {x} and {y}, {timesitwillrun * 2} times and add them, are you sure? Press enter to start: ")

def get_random():
    random_num1 = random.randint(x,y)
    random_num2 = random.randint(x,y)
    randomadd = random_num1 + random_num2
    return randomadd

def get_data():
    data_write = str(get_random())
    with open(file, 'a') as f:
        f.write(f"{data_write} ")
        
data = open(file, "r") 

def count(data):
    numberz = []
    for line in data:
       line = line.strip()
       numberz += line.split (" ")
       return numberz
   
counts = count(data)

d = dict()

for i in range(timesitwillrun):
    get_random()
    get_data()
    
data = open(file, "r") 

for line in data: 
    line = line.strip() 
    words = line.split(" ") 
    for word in words: 
        if word in d: 
            d[word] = d[word] + 1
        else: 
            d[word] = 1
for key in sorted(d, key=int, reverse=True):
    print(key, ":", d[key])
    
reset = input("Wanna reset the counter? (y/n) ")

if reset == "y":
     with open("PY/BB/data.txt", 'w') as f:
        f.write("")

print("Alright! You can run the code again now!")








dontleavemenow = input("")


























