def cipher(st,key):
    chipher = ""
    for i in st:
        if i.isupper():
            chipher+= chr((ord(i)-ord("A")+key)%26+ord("A"))
        elif i.islower():
            chipher+=chr((ord(i)-ord("a")+key)%26 + ord('a'))
        else:
            chipher+= i
    return chipher

def cipher_to_plain(chiper,key):
    plain_text = ""
    for i in chiper:
        if i.isupper():
            plain_text+=chr((ord(i)-ord("A")-key)%26 + ord("A"))
        elif i.islower():
            plain_text+=chr((ord(i)-ord('a')-key)%26 + ord('a'))
        else:
            plain_text+=i
    return plain_text

            
st = "Nirmit Raval"
key = 3
chipher_text = cipher(st,key)
print(chipher_text)
plain_text = cipher_to_plain(chipher_text,key)
print(plain_text)