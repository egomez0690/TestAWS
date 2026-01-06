def handler(event, context):
    x = 10
    y = 0
    z = x / y

    if "name" not in event:
        raise ValueError("Falta el campo name")

    return {
        "statusCode": 200,
        "body": f"Hola {event['name']}"
    }