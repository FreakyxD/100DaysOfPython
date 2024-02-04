import json
import base64


def encode_to_base64(data_dict):
    # convert the dictionary to a JSON string
    json_string = json.dumps(data_dict)

    # convert data to bytes
    data_bytes = json_string.encode("utf-8")

    # encode to Base64
    encoded_data = base64.b64encode(data_bytes)

    # convert encoded bytes back to string
    encoded_string = encoded_data.decode("utf-8")
    return encoded_string


def decode_from_base64():
    pass
