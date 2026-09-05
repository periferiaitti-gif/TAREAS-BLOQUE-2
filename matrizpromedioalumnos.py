estudiantes = [
    #       0              1.   2
    ["Alejandro Morales", 18, "Qhari"],
    ["Ana Lucía Gómez", 19, "Warmi"],
    ["Carlos Eduardo Paredes", 18, "Qhari"],
    ["Daniela Sofía Castro", 20, "Warmi"],
    ["Diego Fernando Torres", 19, "Qhari"],
    ["Gabriel Alejandro Silva", 18, "Qhari"],
    ["Isabella Martínez", 21, "Warmi"],
    ["Javier Enrique López", 19, "Qhari"],
    ["José Luis Rodríguez", 20, "Qhari"],
    ["Juan David Benítez", 18, "Qhari"],
    ["Laura Camila Romero", 19, "Warmi"],
    ["Luis Alberto Mendoza", 22, "Qhari"],
    ["María Fernanda Delgado", 18, "Warmi"],
    ["Mateo Sebastián Aguirre", 19, "Qhari"],
    ["Natalia Isabel Ruiz", 20, "Warmi"],
    ["Paula Andrea Vargas", 18, "Warmi"],
    ["Ricardo Antonio Flores", 21, "Qhari"],
    ["Santiago Esteban Ortiz", 19, "Qhari"],
    ["Sofia Alejandra Navarro", 18, "Warmi"],
    ["Valeria Beatriz Salazar", 20, "Warmi"],
]
 
Warmi = 0
Qhari = 0
 
for fila in estudiantes:
    if fila[2] == 'Warmi':
        Warmi +=1
    else:
        Qhari+=1
 
print(f"El numero de hombres es: {Qhari}")
print(f"El numero de mujeres es: {Warmi}")