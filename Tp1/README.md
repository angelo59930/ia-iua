# TP1: Algoritmo de Búsqueda en Redes de Conexiones Cinematográficas

Este trabajo práctico implementa un algoritmo para encontrar la menor cantidad de conexiones (grados de separación) entre dos actores o actrices en base a su participación en películas. La idea se basa en el concepto del "juego de Kevin Bacon", donde los actores están conectados entre sí a través de las películas en las que han trabajado juntos.

## Descripción

El script `degrees.py` busca la conexión más corta entre dos personas dentro de una red de actores y películas utilizando un algoritmo de búsqueda de rutas. El programa carga datos de archivos CSV que contienen información sobre personas, películas y estrellas de cine, y luego permite al usuario ingresar dos nombres de actores para buscar cuántos "grados de separación" existen entre ellos.

El programa utiliza los siguientes archivos CSV para cargar los datos:

- `people.csv`: Contiene información sobre personas (ID, nombre, año de nacimiento).
- `movies.csv`: Contiene información sobre películas (ID, título, año).
- `stars.csv`: Contiene relaciones entre personas y películas en las que han actuado.

## Funcionalidades Principales

- **Cargar datos**: El script carga toda la información desde los archivos CSV especificados en la carpeta `large` o `small`, según se indique.
- **Búsqueda de actores**: El usuario introduce el nombre de dos personas, y el programa busca sus identificadores únicos.
- **Calcular la ruta más corta**: Utiliza una búsqueda en anchura (BFS) para encontrar el camino más corto de conexiones entre los actores, representado por una serie de películas en las que trabajaron juntos.
- **Mostrar resultado**: El programa imprime el número de grados de separación y muestra la secuencia de películas que conectan a los dos actores.

## Estructura del Código

- `load_data(directory)`: Carga los datos de los archivos CSV de personas, películas y estrellas.
- `main()`: Es el punto de entrada del programa, donde se solicita al usuario ingresar dos nombres y se muestra la conexión entre ellos, si existe.
- `shortest_path(source, target)`: Utiliza el algoritmo de búsqueda para encontrar la menor cantidad de pasos entre dos personas.
- `person_id_for_name(name)`: Convierte un nombre en su ID único en la base de datos.
- `neighbors_for_person(person_id)`: Devuelve las películas y los actores que han trabajado con la persona indicada.

## Ejecución

### Dependencias

Este trabajo práctico no requiere de dependencias externas más allá de la librería estándar de Python.

### Cómo ejecutar el programa

1. Clona el repositorio o descarga los archivos necesarios.
2. Coloca los archivos CSV de datos en la carpeta adecuada (`large` o `small`).
3. Desde la terminal, navega hasta el directorio del TP1 y ejecuta el siguiente comando:

```bash
python degrees.py [directory]
```

Donde `[directory]` puede ser el nombre de la carpeta que contiene los archivos CSV. Si no se especifica, se usará la carpeta `large` por defecto.

El programa te pedirá ingresar los nombres de dos personas para encontrar la conexión más corta entre ellos.

## Ejemplo de uso

```
$ python degrees.py
Loading data...
Data loaded.
Name: Kevin Bacon
Name: Tom Hanks
2 degrees of separation.
1: Kevin Bacon and Tom Cruise starred in A Few Good Men
2: Tom Cruise and Tom Hanks starred in Apollo 13
```

## Notas

- En algunos casos, puede haber más de una persona con el mismo nombre. El programa solicitará al usuario que elija la persona correcta en caso de ambigüedad.
- Si no se encuentra ninguna conexión entre las personas, se indicará que no están conectadas.
