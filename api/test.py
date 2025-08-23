def handler(request, context=None):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': '{"message": "Hello from Vercel!", "status": "success", "python": "working"}'
    } 