# create the encoding and decoding app (secret code)
st=input("Enter the input or msg first: ")
words=st.split(" ")
coding=False
if (coding):
    new_word=[]
    for word in words:
        if (len(word)>=3):
           r1="gpd"
           r2="pyu"
           st_new=r1+word[1:]+word[0]+r2
           new_word.append(st_new)
        else:
            new_word.append(word[::-1])
    print(" ".join(new_word))
else:
    new_word=[]
    for word in words:
        if (len(word)>=3):
           st_new = word[3:-3]
           st_new = st_new[-1] + st_new[:-1]
           new_word.append(st_new)
        else:
           new_word.append(word[::-1])
    print(" ".join(new_word))


        



    
        
