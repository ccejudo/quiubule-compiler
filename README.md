# El Mexiquense Compiler. Equipo #3.

![Logo](./logo/logo_large.png)

El lenguaje está basado en una mezcla de Python, C y la famosa banda mexicana de rock alternativo Café Tacvba haciendo referencia al vocablo chilango de la Ciudad de México. Esto con el objetivo de representar un lenguaje tan icónico en el país ahora también en el mundo de la programación.

## Manual de Usuario
### Requerimientos
- Python
- Github (opcional)

### Instalación
Clonar el repositorio https://github.com/ccejudo/quiubule-compiler o descargar el archivo ZIP y descomprimir.
Modificar un archivo ```<nombre>.chilango``` de forma que contenga el programa deseado a compilar.
Abrir una terminal en la dirección del proyecto.
Ejecutar el programa main seguido del archivo de texto input de la siguiente manera en la terminal: ```python quiubule.py <nombre>.chilango```.

### Gramática del programa
El programa a compilar debe constar de una o más instrucciones, las cuales pueden ser declaraciones, asignaciones, condicionales, ciclos, entradas, salidas y llamadas a funciones. A continuación se muestran ejemplos de cómo escribir dichas estructuras para su correcta compilación.

#### Declaraciones
- Variables
```
% Declaration of variables
coso var1;
coso var2 = 10;
coso var3 = 10.45;
coso var4 = var2;
```
- Arreglos
```
% Declaration of arrays
juntitos arr1;
juntitos arr2 = {1,var2,3,4};
```
- Estructuras
```
% Declaration of struct
chafirete chaf1 {
    coso a;
    coso b;
    };
```
- Funciones
```
% Declaration of functions
rifate f(a,b,c){
    coso a = 5;
}
% Function that returns
rifate f2(a,b,c){
    ahiteva;
}
```

#### Asignaciones
- Variables
```
% Assignation of variables
var1 = 6;
var2 = 8.9;
var3 = var4;
var5 = “A”;
```
- Arreglos
```
% Assignation of arrays
arr[0] = 10;
arr[1] = var2;
```
- Estructuras
```
% Assignation of struct
s.b = 7;
```

#### Condicionales
- IF
```
% If conditional
chance(5 <= 10){
    var1 = 5;
}
```
- IF-ELSE
```
% If-else conditional
chance("hola" != "adios"){
     key = 5;
}hijole{
     coso new_key = 10; 
}
```
#### Ciclos
- FOR
```
% FOR cycle
chambea(a=0;a<10;a=a+1){
    var1 = 5;
}
```

#### Entradas y salidas
- LEE
```
% Read
leete id, 5, 10;
```

- ESCRIBE
```
% Write
escribete id, 5, 10;
```

- ESCRIBE NL
```
% Write in multiple lines
escribetel id, 5, 10;
```

- Llamadas a funciones
```
% Call functions
f(a,b,c);
f2(1,5,”juan”);
```

### Más consideraciones
- El lenguaje no permite la repetición de identificadores dentro y fuera de funciones.
- El lenguaje no requiere que el usuario defina el tipo de datos de variables y funciones.
- Dado que el lenguaje permite que el usuario no declare el tipo de los datos en asignaciones, funciones, arreglos y registros, el analizador semántico indica errores de tipos en condiciones y en la tabla de símbolos los datos y arreglos se guardan y actualizan con su tipo de datos.
- Los caracteres deben tener más de una letra.
- Si lo último que hay es un error se manda un error de lineno.
- Se debe declarar todas las variables que se vayan a usar durante el código, incluso los parámetros de las funciones.

