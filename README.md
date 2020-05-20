# Aplicaciones en el WEB y redes inalámbricas: Proyecto final

## Autores:
    - SANTIAGO RODRIGUEZ PENAGOS	1670706
    - JUAN CAMILO SÁNCHEZ BARREIRO	1527749
    - JUAN FELIPE OROZCO ESCOBAR	1426244

## Asignatura:
    - Aplicaciones en el WEB y redes inalámbricas
    - Universidad del Valle 2019-II

## Información:
En este repositorio se presenta la implementación del backend del proyecto

## Ejecución:
Clonar el repositorio, ingresar al directorio 'tesla-energy-api' y ejecutar las siguientes líneas en la terminal:

```
git clone https://github.com/CamiloSanchez0312/teslaenergyapi.git
cd teslaenergy
python3 -m venv env
source env/bin/activate  // Windows: env\Scripts\activate
pip install -r requirements.txt
python manage makemigrations
python manage migrate
python manage runserver
```


Dependencias:
  - Python3
