frutas = ["manzana", "plátano", "uva", "naranja","pera","coco"]

contador = 0
try:
    print("Listado de frutas\n")
    for f in frutas:
        contador += 1
        print(f'{contador}. {f}')
        
except:
    print("No existe una lista de frutas")