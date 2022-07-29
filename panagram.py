alphabet=list("abcdefghijklmnopqrstuvwxyz ")
s = str(input('Enter the words:').lower())
def panagram():
    for i in alphabet:
        if i in s:
            continue
        else:
            print(i,'is not in your words!')
            return False
    return True
print(panagram())
