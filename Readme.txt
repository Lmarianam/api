api


Descripción
-----------
Este proyecto trata de implementar una API REST utilizando Django, diseñada para gestionar registros de empresas (modelo Company). La API permite realizar operaciones CRUD: 
crear, consultar, actualizar y eliminar empresas, utilizando peticiones HTTP estándar.

Tecnologías que se utilizaron
----------------------
- Python
- Django
- SQLite3 (base de datos por defecto por Django)
- JSON para el intercambio de datos

Estructura principal del proyecto
---------------------------------
api/              Carpeta principal del proyecto
AuthProject/      Configuración principal del proyecto
AuthAPP/          Aplicación que contiene el modelo y la API
manage.py

Modelo utilizado (Company)
--------------------------
El modelo Company contiene los siguientes elementos:
- name (str)
- website (str)
- foundation (int)

Rutas de la API
---------------
Estas son las rutas disponibles para interactuar con la API:

1. Obtener todas las empresas:
   GET /companies/

2. Obtener una empresa por ID:
   GET /companies/<id>

3. Crear una nueva empresa:
   POST /companies/
   Body JSON requerido:

   Ejemplo del formato JSON:
   {
       "name": "Nombre Empresa",
       "website": "https://ejemplo.com",
       "foundation": 1990
   }

4. Actualizar una empresa que este existente:
   PUT /companies/<id>
   Body JSON con los campos a actualizar.

5. Eliminar una empresa:
   DELETE /companies/<id>

Funcionamiento interno
----------------------
La clase CompanyView maneja las peticiones mediante los siguientes métodos:
- get()    Consulta
- post()   Creación
- put()    Actualización
- delete() Eliminación
El método dispatch se le agregó una característica extra usando @csrf_exempt para permitir peticiones desde clientes externos sin necesidad de tokens CSRF.

Cómo ejecutar el proyecto
-------------------------
1. Crear un entorno virtual (opcional pero es lo más recomendado):
   python -m venv env
   env\Scripts\activate

2. Instalar dependencias:
   pip install django

3. Ejecutar el servidor:
   python manage.py runserver

4. Acceder a la API desde el navegador o el Postman:
   http://127.0.0.1:8000/companies/

Notas finales
-------------
Este proyecto está pensado como una API de aprendizaje, creada en clase. 
Se puede ampliar con facilidad empleando Django REST Framework para lograr una API más sólida y profesional.