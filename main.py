import hashlib
from itertools import permutations

def find_hash(original_hash):
    word_file = open("words.txt","r")
    word_file = list(word_file)

    anagram = "pathfoot"
    words = anagram.count(' ')
    words += 1
    print(words)

    char_list = list(set(anagram))

    if ' ' in char_list:
        char_list.remove(' ')

    final_words = []

    #Student Activity
    for i in word_file:
        Flag = False
        Tempword =i.replace('\n','')
        tempchar = list(set(Tempword))
        for i in tempchar :
            if i not in char_list:
                Flag = True
                break
        if Flag == False :
            final_words.append(Tempword)
    
    



        


    print(len(final_words))

    for elem in permutations(final_words, words):
        hash_elem = " ".join(elem)
        if len(hash_elem)!=len(anagram):
            continue
        
        #Student Activity
        
        m = hashlib.md5()
        m.update(hash_elem.encode('utf-8'))
        word_hash = m.hexdigest()

        if word_hash == original_hash:
            return hash_elem

hash = 'e4e475d01190633ae1ed52a9dd7eadd0'
answer = find_hash(hash)
print(f"Collision!  The word corresponding to the given hash is '{answer}'")