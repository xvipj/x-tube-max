![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

# Enlace a la aplicación en producción

¡Prueba la aplicación en producción! Haz clic en el siguiente enlace para explorarla:

[🔗 Prueba la aplicación aquí]()

![ui](image/ui.png)

👉 **Clonar el proyecto desde el repositorio:**

Primero, asegúrate de tener Git instalado en tu sistema. Luego, ejecuta el siguiente comando en tu terminal para clonar el repositorio de tu proyecto Django:

```bash
git clone git@github.com:xvipj/x-tube-max.git
```

👉 **Instalar los paquetes del archivo `requirements.txt`:**

Una vez que hayas clonado el proyecto, navega hasta el directorio del proyecto en tu terminal. Luego, instala los paquetes necesarios utilizando pip y el archivo `requirements.txt`. Ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

Esto instalará todas las dependencias necesarias para tu proyecto Django.

👉 **Ejecutar el proyecto sin aplicar migraciones:**

Después de instalar los paquetes, puedes ejecutar tu proyecto sin aplicar migraciones. Utiliza el siguiente comando para arrancar el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Esto iniciará el servidor de desarrollo en tu máquina local. Puedes acceder a tu proyecto en un navegador web visitando `http://localhost:8000/`.

Recuerda que al no aplicar migraciones, es posible que ciertas funcionalidades de tu proyecto no estén disponibles o funcionen correctamente. Este enfoque es útil en situaciones donde necesitas ejecutar rápidamente el proyecto sin preocuparte por la base de datos.