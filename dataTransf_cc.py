# transform eventIntents to confirm/cancel intents

import uuid
import datetime

def transform_data_cc(input_data):
    # in case of "confirm"
        transformed_data = {
            "eventId": str(uuid.uuid4()),
            "correspondingEventId": input_data["eventId"],
            "eventTime": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S,%f')[:-3] + '+09:00',
            "eventIntents": [
                {
                    "text": "확인",
                    "intents": [
                        {
                            "id": "intent$000000000000013",
                            "name": "confirm",
                            "confidence": 0.9999
                        }
                    ]
                }
            ]
        }
        return transformed_data