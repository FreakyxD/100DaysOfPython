import json
import base64


def obfuscate_data(json_string):
    dummy_data = "lfFF4fk4fm0=" * 1000000
    obfuscated_string = dummy_data + json_string + dummy_data[::-1]
    return obfuscated_string


def de_obfuscate_data(obfuscated_string):
    dummy_length = len("lfFF4fk4fm0=" * 1000000)
    cleaned_string = obfuscated_string[dummy_length:-dummy_length]
    return cleaned_string


def encode_to_base64(data_dict, apply_obfuscation):
    """
    Encodes a dictionary to a Base64 string with optional obfuscation.

    Parameters:
        data_dict (dict): The dictionary to encode.
        apply_obfuscation (bool): Whether to apply obfuscation to the data.

    Returns:
        str: The encoded (and possibly obfuscated) data in Base64 string format.
    """

    # convert the dictionary to a JSON string
    json_string = json.dumps(data_dict, indent=4)

    if apply_obfuscation:
        json_string = obfuscate_data(json_string)

    # convert data to bytes
    data_bytes = json_string.encode("utf-8")

    # encode to Base64
    encoded_data = base64.b64encode(data_bytes)

    # convert encoded bytes back to string
    encoded_string = encoded_data.decode("utf-8")
    return encoded_string


def decode_from_base64(encoded_string, obfuscation_applied):
    """
    Decodes a Base64 string back to a Python dictionary, with an option to de-obfuscate the data if obfuscation was
    applied during encoding.

    Parameters:
        encoded_string (str): The Base64 encoded string to decode, which may have been obfuscated.
        obfuscation_applied (bool): Indicates whether the data was obfuscated during encoding.
        This should match the `apply_obfuscation` parameter used in `encode_to_base64`.

    Returns:
        dict: The decoded Python dictionary, with obfuscation removed if it was applied.
    """

    # convert encoded string back to bytes
    encoded_data = encoded_string.encode("utf-8")

    # decode from Base64
    decoded_data = base64.b64decode(encoded_data)

    # convert decoded bytes back to string
    decoded_string = decoded_data.decode("utf-8")

    if obfuscation_applied:
        decoded_string = de_obfuscate_data(decoded_string)

    return decoded_string
