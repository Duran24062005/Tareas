# FastApi

1. Instale el paquete virtualenv si aún no lo ha hecho. Puede instalarlo usando pip: `pip install virtualenv`.

2. Una vez que tenga virtualenv instalado, navegue hasta su directorio de proyecto y cree un nuevo entorno virtual usando el siguiente comando: `virtualenv venv`.
Esto creará un nuevo directorio llamado venv en su carpeta de proyecto, que contiene el entorno virtual.

3. Para activar el entorno virtual, use los siguientes comandos:

En Windows: `venv\Scripts\activate`

En Unix o MacOS: `source venv/bin/activate`

4.Una vez que el entorno virtual esté activado, puede instalar FastAPI y cualquier otro paquete requerido en el entorno aislado. Por ejemplo, para instalar FastAPI y sus dependencias, puede ejecutar: `pip install fastapi uvicorn`.


Ahora tiene un entorno virtual configurado para su proyecto FastAPI, y puede instalar y administrar paquetes sin afectar su entorno Python global. Recuerde activar el entorno virtual cada vez que trabaje en el proyecto.