import json
import random

def lambda_handler(event, context):

    mensajes = [
        "Hola desde Lambda",
        "Microservicio activo",
        "Mensaje aleatorio",
        "AWS funcionando",
        "API correcta"
    ]

    respuesta = random.choice(mensajes)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensaje': respuesta
        })
    }
