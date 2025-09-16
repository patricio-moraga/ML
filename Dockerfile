# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que se ejecuta Flask
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

# Comando para ejecutar la aplicación, usando la variable de entorno $PORT
CMD uvicorn app:app --host 0.0.0.0 --port 8000
