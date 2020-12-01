from parser import Parser

def eetlijst():
    ps = Parser()
    eaters, cook, absent, unknown = ps.eetlijst
    if len(cook) == 0:
        reply = "Er gaat nog niemand koken.\n"
    else:
        reply = ' en'.join(str(cook).replace('[','').replace('\'','').replace(']','').rsplit(',', 1))
        reply += " gaat" if len(cook) == 1 else " gaan"
        reply += " koken.\n"
    if len(eaters) > 0:
        reply += ' en'.join(str(eaters).replace('[','').replace('\'','').replace(']','').rsplit(',', 1))
        reply += " eet" if len(eaters) == 1 else " eten"
        reply += " mee.\n"
    if len(unknown) > 0:
        reply += ' en'.join(str(unknown).replace('[','').replace('\'','').replace(']','').rsplit(',', 1))
        reply += " moet" if len(unknown) == 1 else " moeten"
        reply += " zich nog inschrijven.\n"
    unknown_persons = []
    for name in unknown:
        unknown_persons.append({'name': name, 'telegram_id': ps.persons[name]})
    return {'reply': reply, 'unknown_persons': unknown_persons}

def kok():
    ps = Parser()
    cook = ps.get_cook()
    if len(cook) == 0:
        if len(ps.get_eaters() + ps.get_unknown()) == 0:
            reply = "Er eet niemand mee."
        else:
            cook_suggestion = ps.get_cook_suggestion()
            reply = f"Er gaat nog niemand koken, maar {cook_suggestion} staat het laagst qua verhouding."
    else:
        reply = ' en'.join(str(cook).replace('[','').replace('\'','').replace(']','').rsplit(',', 1))
        reply += " gaat" if len(cook) == 1 else " gaan"
        reply += " koken."
    return reply

def kookpunten():
    ps = Parser()
    zipped = str(dict(zip(ps.get_points(), ps.names)))
    reply = zipped.replace('{\'','<b>Kookpunten:</b>\n<code>').replace('\': \'','</code> (').replace('\', \'',')\n<code>').replace('\'}',')')
    return reply

def kosten():
    ps = Parser()
    zipped = str(dict(zip(ps.get_costs(), ps.names)))
    reply = zipped.replace('{\'','<b>Gemiddelde kosten:</b>\n<code>€').replace('\': \'','</code> (').replace('\', \'',')\n<code>€').replace('\'}',')')
    return reply

def verhouding():
    ps = Parser()
    zipped = str(dict(zip(ps.get_ratio(), ps.names)))
    reply = zipped.replace('{','<b>Verhouding koken/eten:</b>\n<code>').replace(': \'','</code> (').replace('\', ',')\n<code>').replace('\'}',')')
    return reply
