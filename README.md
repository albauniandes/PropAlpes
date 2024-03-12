# PropAlpes - PoC

Repositorio con código base para el uso de un sistema usando el patrón CQRS y usando eventos de dominio e integración para la comunicación asíncrona entre componentes internos parte del mismo contexto acotado y sistemas externos.

## Estructura del proyecto

Dentro de la carpeta src contamos con 4 microservicios:
- companias (Se encarga de registrar los datos de las compañías)
- geograficos (Se encarga de registrar los datod geográficos de las propiedades)
- auditoria (Se encarga de revisar los datos faltantes de compañías y propiedades)
- bff_web (Se encarga de la comunicación de los componentes de la UI web)


- Para los servicios companias, geograficos y auditoria se implementó una arquitectura hexagonal. Por eso, cuentan con los siguientes sub-módulos:
    - **api**: En este módulo se agregaron los endpoint : Por ejemplo `/compania-commando` y `/compani-query`, los cuales por detrás de escenas usan un patrón CQRS como la base de su comunicación.
    - **modulos/../aplicacion**: Este módulo ahora considera los sub-módulos: `queries` y `comandos`. En dichos directorios podrá ver como se desacopló las diferentes operaciones lectura y escritura. 
    - **modulos/../aplicacion/handlers.py**: Estos son los handlers de aplicación que se encargan de oir y reaccionar a eventos. 
    - **modulos/../dominio/eventos.py**: Este archivo contiene todos los eventos de dominio que son disparados cuando una actividad de dominio es ejecutada de forma correcta.
    - **seedwork/aplicacion/comandos.py**: Definición general de los comandos, handlers e interface del despachador.
    - **seedwork/infraestructura/queries.py**: Definición general de los queries, handlers e interface del despachador.
    - **seedwork/infraestructura/uow.py**: La Unidad de Trabajo (UoW) mantiene una lista de objetos afectados por una transacción de negocio y coordina los cambios de escritura. Este objeto nos va ser de gran importancia, pues cuando comenzamos a usar eventos de dominio e interactuar con otros módulos, debemos ser capaces de garantizar consistencia entre los diferentes objetos y partes de nuestro sistema.

## Arquitectura para el experimento
Para la etapa final de la experimentación implementamos la siguiente arquitectura:
![Borrador_arquitectura drawio_final](https://github.com/albauniandes/PropAlpes/assets/98788512/14268ab5-9e72-4343-99a2-b19f23b30ded)

El BFF se comunica con la capa UI a través de una API de GraphQL y envia los comandos de creación a los servicios compañías y geograficos usando un tópico de comandos. Cuando se crearon los registros de las compañías y de los datos gergráficos en las bases de datos de cada servicio, se envía un mensaje que informa el servicio de auditoría sobre la creación de dichos registros. Para este último paso se usa un tópico de eventos.

# Justificación de tipos de eventos a utilizar

Para justificar las decisiones en nuestro proyecto, empezamos con el reconocimiento de que necesitábamos una arquitectura capaz de manejar datos y eventos eficientemente en un entorno distribuido. Aquí están las claves:

## Elección de Eventos de Integración: 
Nos decidimos exclusivamente por eventos de integración porque nuestro sistema necesita comunicar acciones y cambios entre servicios de manera eficiente sin transferir estados completos. Esto simplifica la interacción entre microservicios, permitiendo que cada uno responda a eventos relevantes sin necesidad de conocer el estado completo del sistema. Es una estrategia que favorece la desacoplación y la escalabilidad, ya que los servicios pueden evolucionar de forma independiente.

## Uso de Avro para la Serialización de Datos: 
Elegimos Avro debido a su fuerte soporte para la evolución de esquemas y su eficiencia en la serialización de datos. En un entorno basado en eventos de integración, es vital poder adaptar los esquemas de los eventos sin interrumpir los servicios consumidores. Avro nos permite añadir, modificar o eliminar campos en nuestros esquemas de eventos sin romper la compatibilidad hacia atrás, garantizando que los servicios puedan comunicarse sin problemas a medida que nuestro sistema crece y cambia.

## Implementación con Strawberry y GraphQL: 
La decisión de utilizar Strawberry para GraphQL se basa en la necesidad de exponer datos a nuestros clientes de una manera flexible y eficiente. Con eventos de integración llevando a cabo la comunicación interna entre servicios, GraphQL se convierte en la interfaz perfecta para que los clientes accedan a los datos que necesitan, permitiendo solicitudes específicas y minimizando el sobreenvío de datos.

## Apache Pulsar como Sistema de Mensajería: 
La elección de Apache Pulsar se justifica por su arquitectura distribuida y su capacidad para manejar grandes volúmenes de mensajes de manera eficiente. Pulsar nos permite manejar eventos de integración a gran escala, garantizando la entrega de mensajes entre servicios de forma confiable. Además, su soporte para esquemas integrados complementa nuestra elección de Avro, facilitando la gestión y evolución de esquemas en nuestro sistema de eventos.

En conclusión, la adopción de eventos de integración refleja nuestro enfoque en mantener los servicios desacoplados y escalables. Al utilizar Avro y Pulsar, aseguramos que nuestros eventos son eficientes y evolutivos, mientras que con Strawberry y GraphQL, ofrecemos una interfaz optimizada para el acceso a datos. Estas decisiones tecnológicas están diseñadas para soportar un sistema dinámico y en crecimiento, donde la facilidad de integración y la capacidad de adaptación son clave.

# Justificación topología de administración de datos

Para las bases de datos de compañias y geográficos se utilizó una administración de datos descentralizada, toda vez que cada servicio tiene su propia base de datos, haciendo uso de Docker para desplegarlas, esta decisión se tomo por el desacoplamiento, ya que si cada microservicio tiene su propia base de datos permite que no se generen inconvenientes o inconsistencias, en el dado caso que alguna falle, lo que permite una mayor disponibilidad de los servicios. Se manejo el modelo clásico CRUD para la comunicación de todos los micorservicios con sus base de datos, debido a la practicidad de esta solución.

### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

- Ejecucion DBs
```bash
 docker-compose --profile db up
```

- Ejecucion Apache Pulsar
```bash
 docker-compose --profile pulsar up
```

- Ejecucion Microservicio Compañias
```bash
flask --app src/companias/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/companias/api --debug run
```

- Ejecucion Microservicio Datos Geograficos
```bash
flask --app src/geograficos/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/geograficos/api --debug run
```

- Ejecucion Microservicio Propiedades
```bash
flask --app src/propiedades/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/propiedades/api --debug run
```

- Ejecucion Microservicio Auditoría
```bash
flask --app src/auditoria/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/auditoria/api --debug run
```

- Ejecucion Servicio BFF

```bash
cd src
uvicorn bff_web.main:app --host localhost --port 8003 --reload
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

- Contenedor servicio Compañias

```bash
docker build . -f companias.Dockerfile -t companias/flask
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 5000:5000 companias/flask
```

- Contenedor servicio Datos Geograficos

```bash
docker build . -f companias.Dockerfile -t geograficos/flask
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 5001:5000 geograficos/flask
```

# Escenarios de calidad a probar

Atributo de calidad: Escalabilidad
![image](https://github.com/albauniandes/PropAlpes/assets/98788512/3f098113-75d5-4008-b6ab-8deb5b54201c)

Atributo de calidad: Escalabilidad II
![image](https://github.com/albauniandes/PropAlpes/assets/98788512/eeaca79e-5429-4948-a1a5-cbe388fcd811)


Atributo de calidad: Disponibilidad
![image](https://github.com/albauniandes/PropAlpes/assets/98788512/3b76a4f0-2c71-4113-841b-80d85bdb4d74)


# Descripción de actividades realizada por cada miembro.

| Nombre          | Descripción de actividades         | 
|-----------------|------------------------------------|
| Alba Cardona    | Desarrollo de microservicio companias, con unidades de trabajo comandos, y API, la configuración de la base de datos de dicho microservicio y el desarrollo de algunas partes del microservicio de auditoría |
| Patrick Mykoda          | Desarrollo de microservicio BFF, con su API, las consultas que ha realizar, los esquemas, mutaciones a través de GraphQL, router, los consumidores y despachadores, asi mismo la comunicación con los microservicios de geogáficos y compañias |
| Carlos Villamil         | Implementación de Apache pulsar y asincronía en el microservicio compañias desarrollo del microservicio auditoria |
| Christian Borrás Torres | Desarrollo microservicio geográficos, con API, módulos y eventos. |
