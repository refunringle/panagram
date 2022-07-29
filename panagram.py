def panagram(s):
    alphabet=list("abcdefghijklmnopqrstuvwxyz")
    for i in alphabet:
        if i in s:
            continue
        else:
            print(i,'is not in your words!')
            return False
    return True
s = str(input('Enter the words:').lower())
print(panagram(s))
