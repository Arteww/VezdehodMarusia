import json


def webhook(event, context):
    request_message = json.loads(event['body'])
    if ' '.join(request_message['request']['nlu']['tokens']) in ["шишки вездеход", "вездеход шишки"]:
        derived_session_fields = ['session_id', 'user_id', 'message_id']
        response_message = {
            "response": {
                "text": "Привет вездекодерам!",
                "tts": "Привет вездекодерам!",
                "end_session": False
            },
            "session": {derived_key: request_message['session'][derived_key] for derived_key in derived_session_fields},
            "version": request_message['version']
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response_message)
        }
