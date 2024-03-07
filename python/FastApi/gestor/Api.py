from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from database import Cliente

headers = {"content-type": "charset=utf-8"}

app = FastAPI()


@app.get("/")
async def index():
    content = {"mensaje": "¡hola mundo!"}
    return JSONResponse(content=content, headers=headers)

@app.get('/html/')
async def html():
    content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>¡Hola, mundo!</h1>
        <p>este es un mensaje html</p>
    </body>
    </html>
    """
    return Response(content=content, media_type='text/html')


@app.get("/clientes/")
async def clientes():
    content = [
        {'dni': cliente.dni, 'nombre': cliente.nombre, 'apellido': clientes.apellido}
        for cliente in database.Clientes.lista
    ]
    return JSONResponse(content=content, headers=headers)


print('Servidor de la API...')