# Escenarios de calidad a probar

Atributo de calidad: Escalabilidad
![image](https://github.com/albauniandes/PropAlpes/assets/98656753/12c1d88f-b766-43cc-bda1-c5a72e3c1a1f)

Atributo de calidad: Modificabilidad
![image](https://github.com/albauniandes/PropAlpes/assets/98656753/c14ad867-a06a-4c7e-8160-9c54826e6360)


Atributo de calidad: Disponibilidad
![image](https://github.com/albauniandes/PropAlpes/assets/98656753/8bd9ec40-b660-4f09-9f2f-2cb30ea4027d)



# Estructura
````
├── .github/workflows
|   └── ci_pipeline.yml # Configuración del pipeline
├── component1 # Archivos de la aplicación componente 1
|   ├── src # código de la aplicación
|   ├── tests # Paquete de pruebas
|   ├── Pipfile # Dependencias de la aplicación
|   ├── Pipfile.lock # Archivo lock de dependencias
|   └── pytest.ini # Configuración de pruebas
└── README.md # Estás aquí
````

En archivo ````ci_pipeline.yml```` contiene el pipeline que ejecuta las pruebas. Se recomienda revisar como está configurado y las notas en el.

## Como ejecutar localmente las pruebas

1. Install pipenv
2. Ejecutar pruebas
```
cd component1
pipenv shell
pipenv install --dev
pipenv run pytest --cov=src -v -s --cov-fail-under=80
deactivate
```
