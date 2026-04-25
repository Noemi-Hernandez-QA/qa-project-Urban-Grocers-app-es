# Proyecto Urban Grocers 
Este proyecto forma parte de las pruebas de validación de la API de Urban Grocers. El objetivo principal es automatizar las pruebas del endpoint de creación de kits, enfocándose específicamente en la validación del campo name.

***Tecnologías y Herramientas***

- Lenguaje: Python 3.x

- Framework de Pruebas: Pytest

- Librerías: Requests (para peticiones HTTP)

- Entorno: PyCharm / Git

***Estructura del Proyecto***

- configuration.py: Almacena la URL base y las rutas (endpoints) de la API.

- data.py: Contiene los cuerpos de las solicitudes (payloads) y datos de prueba.

- sender_stand_request.py: Módulos para realizar las peticiones POST (creación de usuarios y kits).

- create_kit_name_kit_test.py: Suite de pruebas principal que contiene la lógica de validación y los 9 casos de prueba.

***Casos de Prueba Automatizados***

Se implementaron 9 pruebas basadas en la lista de comprobación:

- Límite inferior (1 carácter): Éxito (201).

- Límite máximo (511 caracteres): Éxito (201).

- Nombre vacío: Error (400).

- Exceso de caracteres (512): Error (400).

- Caracteres especiales: Éxito (201).

- Espacios en el nombre: Éxito (201).

- Números en el nombre: Éxito (201).

- Parámetro ausente: Error (400).

- Tipo de dato incorrecto (número en lugar de string): Error (400).

***Hallazgos (Bugs Encontrados)***

Durante la ejecución, se identificaron discrepancias entre el comportamiento del servidor y la documentación:

**Prueba 4**: El servidor acepta 512 caracteres en lugar de arrojar un error 400.

**Prueba 8**: Al no enviar el parámetro name, el servidor responde con un 201 en lugar de un 400.

**Prueba 9**: Al enviar un número como tipo de dato, el servidor arroja un Error 500 (Internal Server Error) en lugar de un 400 controlado.

***Ejecución de las pruebas***

1.- Clona este repositorio.

2.- Asegúrate de tener instalado Python y las dependencias:

```python
Bash

pip install requests pytest
```

3.- Actualiza la URL del servidor en `configuration.py.`

4.- Ejecuta el comando:

```python
Bash

pytest create_kit_name_kit_test.py
```