def shout(string):
    return string.upper() + "!!!"

def whisper(string):
    return chr(129323) + string.lower()


def saludar(string, mode=None):
    print("*" * len(string))
    if mode==None:
        print(string)
    else:
        print(mode(string))
    print("!" * len(string))

silence=whisper

