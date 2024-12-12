FROM python:3.13-rc-slim-bookworm

# directorio de la app
WORKDIR /app

# copiar los archivos del proyecto y pegarlos en el directorio app
COPY . /app

# instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# exponer un puerto
EXPOSE 8000

# ejecutar el proyecto
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]