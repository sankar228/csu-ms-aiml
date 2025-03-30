import base64

# User defined Function to Encode the password combining with the
# business defined secret text
def userdef_encode(free_txt) -> str:
    secret_key_text = "CsU9_O25@" +free_txt
    free_txt_bytes = secret_key_text.encode("utf-8")
    return base64.b64encode(free_txt_bytes)

# De    
def userdef_decode(encodedStr) -> str:
    secret_key = "CsU9_O25@"
    
    dstr = base64.b64decode(encodedStr)
    return dstr[len(secret_key):]
   
    
if __name__ == "__main__":
    # Assume that system is configured to allow "SanKpAsW0rd" as the password
    encoded_pass = userdef_encode("SanKpAsW0rd")
    print(encoded_pass)
    
    decoded_pass = userdef_decode(encoded_pass)
    print(decoded_pass)