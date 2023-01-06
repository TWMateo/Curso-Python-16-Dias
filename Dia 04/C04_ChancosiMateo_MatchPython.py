#Match nos permite hacer lo que switch case hace en otro lenguajes

serie='N-01'

match serie:
    case 'N-01':
        print("Samsung")
    case 'N-02':
        print("Nokia")
    case 'N-03':
        print('Motorola')
    case _:
        print('No existe esta serie')

#Tambien se puede usar al recorrer una lista de objetos

cliente={'Nombre':'Fernanda','Edad':21,'Ocupacion':'Enfermera'}
pelicula={'Titulo':'Matrix','Ficha tecnica':{'Protagonista':'Keanu Reeves','Director':'Lana y Lilly Wachowski'}}
elementos=[cliente,pelicula,"Libro"]

for e in elementos:
    match e:
        case {'Nombre':nombre,'Edad':edad,'Ocupacion':ocupacion}:
            print(f"Cliente: {nombre} {edad} {ocupacion}")
        case{'Titulo':titulo,'Ficha tecnica':{'Protagonista':prota,'Director':dire}}:
            print(f"Pelicula: {titulo} Protagonista {prota} director {dire}")
        case _:
            print("Este objeto no existe")