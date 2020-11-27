from parser import Parser

def array_to_string(array):
    str(array).replace('[','').replace('\'','').replace(']','')

def eetlijst():
    ps = Parser()
    eaters, cook, absent, unknown = ps.get_eetlijst()
    if len(cook) == 0:
        reply = "Er gaat nog niemand koken.\n"
    elif len(cook) == 1:
        reply = "%s gaat koken.\n" % array_to_string(cook)
    else:
        reply = "%s gaan koken.\n" % array_to_string(cook)
    if len(eaters) > 0:
        reply += f"{array_to_string(eaters)}"
        if len(eaters) == 1:
            reply += " eet mee.\n"
        else:
            reply += " eten mee.\n"
    if len(unknown) > 0:
        reply += f"{array_to_string(unknown)}"
        if len(unknown) == 1:
            reply += " moet zich nog inschrijven.\n"
        else:
            reply += " moeten zich nog inschrijven.\n"
    return reply

def kok():
    ps = Parser()
    cook = ps.get_cook()
    if len(cook) == 0:
        zipped = str(dict(zip(ps.get_ratio(), ps.get_names())))
        reply = "Er gaat nog niemand koken, maar dit is de verhouding koken/eten:\n"
        reply += zipped.replace('{','<code>').replace(': \'','</code> (').replace('\', ',')\n<code>').replace('\'}',')')
    elif len(cook) == 1:
        reply = "%s gaat koken." % array_to_string(cook)
    else:
        reply = "%s gaan koken." % array_to_string(cook)
    return reply

def kookpunten():
    ps = Parser()
    zipped = str(dict(zip(ps.get_points(), ps.get_names())))
    reply = zipped.replace('{\'','<b>Kookpunten:</b>\n<code>').replace('\': \'','</code> (').replace('\', \'',')\n<code>').replace('\'}',')')
    return reply

def kosten():
    ps = Parser()
    zipped = str(dict(zip(ps.get_costs(), ps.get_names())))
    reply = zipped.replace('{\'','<b>Gemiddelde kosten:</b>\n<code>€').replace('\': \'','</code> (').replace('\', \'',')\n<code>€').replace('\'}',')')
    return reply

def verhouding():
    ps = Parser()
    zipped = str(dict(zip(ps.get_ratio(), ps.get_names())))
    reply = zipped.replace('{','<b>Verhouding koken/eten:</b>\n<code>').replace(': \'','</code> (').replace('\', ',')\n<code>').replace('\'}',')')
    return reply
