def handler(event, context):
    if "name" not in event:
        raise ValueError("Falta el campo name")

    return {
        "statusCode": 200,
        "body": f"Hola {event['name']}"
    }

def secret_logic():
    return "no tests for me"
