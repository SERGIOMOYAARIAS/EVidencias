#SERGIO SMITH MOYA ARIAS
Entradas=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]
with open("agenda.csv","w+") as f:
 for e in Entradas:
    f.write(f"{e[0]}|{e[1]}|{e[2]}\n")
