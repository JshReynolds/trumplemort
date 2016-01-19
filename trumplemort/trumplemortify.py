import re

def trumplemortify(status, trumplemap):

    mortified = status

    for (regEx, trumpled) in trumplemap:
        mortified = re.sub(regEx, trumpled, mortified, flags=re.IGNORECASE)
        
    return mortified

