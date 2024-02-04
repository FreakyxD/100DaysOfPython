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


def decode_from_base64(encoded_string):
    # convert encoded string back to bytes
    encoded_data = encoded_string.encode("utf-8")

    # decode from Base64
    decoded_data = base64.b64decode(encoded_data)

    # convert decoded bytes back to string
    decoded_string = decoded_data.decode("utf-8")
    return decoded_string
