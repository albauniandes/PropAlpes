# PropAlpes

Repositorio con código base para el uso de un sistema usando el patrón CQRS y usando eventos de dominio e integración para la comunicación asíncrona entre componentes internos parte del mismo contexto acotado y sistemas externos.

## Estructura del proyecto

Este repositorio sigue en general la misma estructura del repositorio de origen. Sin embargo, hay un par de adiciones importante mencionar:

- El proyecto de PropAlpes tiene los siguientes modulos:
    - **api**: En este módulo se agregaron los endpoint : `/compania-commando` y `/compani-query`, los cuales por detrás de escenas usan un patrón CQRS como la base de su comunicación.
    - **modulos/../aplicacion**: Este módulo ahora considera los sub-módulos: `queries` y `comandos`. En dichos directorios podrá ver como se desacopló las diferentes operaciones lectura y escritura. 
    - **modulos/../aplicacion/handlers.py**: Estos son los handlers de aplicación que se encargan de oir y reaccionar a eventos. 
    - **modulos/../dominio/eventos.py**: Este archivo contiene todos los eventos de dominio que son disparados cuando una actividad de dominio es ejecutada de forma correcta.
    - **seedwork/aplicacion/comandos.py**: Definición general de los comandos, handlers e interface del despachador.
    - **seedwork/infraestructura/queries.py**: Definición general de los queries, handlers e interface del despachador.
    - **seedwork/infraestructura/uow.py**: La Unidad de Trabajo (UoW) mantiene una lista de objetos afectados por una transacción de negocio y coordina los cambios de escritura. Este objeto nos va ser de gran importancia, pues cuando comenzamos a usar eventos de dominio e interactuar con otros módulos, debemos ser capaces de garantizar consistencia entre los diferentes objetos y partes de nuestro sistema.

### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/compania/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/compania/api --debug run
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f companias.Dockerfile -t companias/flask
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 5000:5000 companias/flask
```