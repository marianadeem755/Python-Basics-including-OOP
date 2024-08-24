encoding_Rules=["First rule is that if the character are 3 then removes the first character and attach that character to last. Then add three ransom characters to the start and end"]
Decoding_rules=["Reverse all the Decoding rules such as firstly remove the character from last and add to the front if the characters are 3 and then removes the first 3 and last 3 characters"]
character=0
if character==3:
    print(f"Follow up the first rule: {encoding_Rules}")
else:
    print(f"Follow up the 2nd Rules: {Decoding_rules}")

def encoding_characters(characters):
    if encoding_characters<3:
        del(encoding_characters[1])
        encoding_characters.append(1)
    else:
        encoding_characters.append(1)
        del(encoding_characters[1])
    print(characters)

