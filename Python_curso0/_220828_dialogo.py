from _220828_dialogo_funciones import *

dialogo = [
    ("hola", shout),
    ("¿Por qué gritas?", whisper),
    ("no te oigo", shout),
    ("yo te oigo demasiado", None),
    ("es que tengo un plátano en la oreja", shout)
]

for string, mode in dialogo:
    if mode == None:
        print(string)
    else:
        print(mode(string))        