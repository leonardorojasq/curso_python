frutas = ["banana","pera","manzana","coco"]


frutas.append("Mandarina")
print(frutas)



frutas.extend(["uchua","uva"])
print(frutas)


frutas.pop()
frutas.append("Mango")
frutas.remove("pera")
print(frutas)
del frutas[4]
print(frutas)
