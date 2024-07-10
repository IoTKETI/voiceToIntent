import uuid
import datetime

def transform_data(input_data):
    # in case of "stand"
    if input_data["intents"][0]["name"] == "stand":
        transformed_data = {
            "eventId": str(uuid.uuid4()),
            "eventTime": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S,%f')[:-3] + '+09:00',
            "eventIntents": [
                {
                    "text": input_data["text"],
                    "intents": [
                        {
                            "id": "intent$000000000000008",
                            "name": input_data["intents"][0]["name"],
                            "confidence": f"{input_data["intents"][0]["confidence"]:.4f}"
                        }
                    ],
                    "entities": {
                        "deviceName": [
                            {
                                "id": "entity$00000000001",
                                "name": "deviceName",
                                "value": [input_data["entities"]["deviceName:deviceName"][0]["value"]],
                                "confidence": f"{input_data["entities"]["deviceName:deviceName"][0]["confidence"]:.4f}"
                            }
                        ]
                    }
                }
            ]
        }
        return transformed_data
    # in case of "sit"
    elif input_data["intents"][0]["name"] == "sit":
        transformed_data = {
            "eventId": str(uuid.uuid4()),
            "eventTime": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S,%f')[:-3] + '+09:00',
            "eventIntents": [
                {
                    "text": input_data["text"],
                    "intents": [
                        {
                            "id": "intent$000000000000009",
                            "name": input_data["intents"][0]["name"],
                            "confidence": f"{input_data["intents"][0]["confidence"]:.4f}"
                        }
                    ],
                    "entities": {
                        "deviceName": [
                            {
                                "id": "entity$00000000001",
                                "name": "deviceName",
                                "value": [input_data["entities"]["deviceName:deviceName"][0]["value"]],
                                "confidence": f"{input_data["entities"]["deviceName:deviceName"][0]["confidence"]:.4f}"
                            }
                        ]
                    }
                }
            ]
        }
        return transformed_data
    # in case of "ready"
    elif input_data["intents"][0]["name"] == "ready":
        transformed_data = {
            "eventId": str(uuid.uuid4()),
            "eventTime": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S,%f')[:-3] + '+09:00',
            "eventIntents": [
                {
                    "text": input_data["text"],
                    "intents": [
                        {
                            "id": "intent$000000000000010",
                            "name": input_data["intents"][0]["name"],
                            "confidence": f"{input_data["intents"][0]["confidence"]:.4f}"
                        }
                    ],
                    "entities": {
                        "deviceName": [
                            {
                                "id": "entity$00000000001",
                                "name": "deviceName",
                                "value": [input_data["entities"]["deviceName:deviceName"][0]["value"]],
                                "confidence": f"{input_data["entities"]["deviceName:deviceName"][0]["confidence"]:.4f}"
                            }
                        ]
                    }
                }
            ]
        }
        return transformed_data