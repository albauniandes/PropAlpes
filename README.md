# PropAlpes

Repositorio con código base para el uso de un sistema usando el patrón CQRS y usando eventos de dominio e integración para la comunicación asíncrona entre componentes internos parte del mismo contexto acotado y sistemas externos.

## Estructura del proyecto

Dentro de la carpeta src contamos con 4 microservicios:
- companias (Se encarga de registrar los datos de las compañías)
- geograficos (Se encarga de registrar los datod geográficos de las propiedades)
- auditoria (Se encarga de revisar los datos faltantes de compañías y propiedades)
- bff_web (Se encarga de la comunicación de los componentes de la UI web)

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

# Escenarios de calidad a probar

Atributo de calidad: Escalabilidad
![image](https://github.com/albauniandes/PropAlpes/assets/98656753/12c1d88f-b766-43cc-bda1-c5a72e3c1a1f)

Atributo de calidad: Modificabilidad

![image](https://github.com/albauniandes/PropAlpes/assets/98656753/c14ad867-a06a-4c7e-8160-9c54826e6360)


Atributo de calidad: Disponibilidad
![image](https://github.com/albauniandes/PropAlpes/assets/98656753/8bd9ec40-b660-4f09-9f2f-2cb30ea4027d)

# Documento con la descripción de actividades realizada por cada miembro.

| Nombre          | Descripción de actividades         | 
|-----------------|------------------------------------|
| Alba Cardona    | Desarrollo de microservicio companias, con unidades de trabajo comandos, y API, la configuración de la base de datos de dicho microservicio y el desarrollo de algunas partes del microservicio de auditoría |
| Patrick Mykoda          | Desarrollo de microservicio BFF, con su API, las consultas que ha realizar, los esquemas, mutaciones a través de GraphQL, router, los consumidores y despachadores, asi mismo la comunicación con los microservicios de geogáficos y compañias |
| Carlos Villamil         | Implementación de Apache pulsar y asincronía en el microservicio compañias desarrollo del microservicio auditoria |
| Christian Borrás Torres | Desarrollo microservicio geográficos, con API, módulos y eventos. |
