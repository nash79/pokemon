import hug
from falcon import *
from db import DBPokemon


@hug.get('/pokemon')
def pokemonlist(response):
    dbp = DBPokemon("root", "pokemon")
    v = dbp.callfindallpokemon()
    if v == []:
        response.status = HTTP_404
        return 'Donnee vide'
    else:
        response.status = HTTP_200
        return str(v)


@hug.post('/pokemon')
def pokemon_add(add: hug.types.text, response):
    dbp = DBPokemon("root", "pokemon")
    v = dbp.callinsertpokemon(add)
    if v == 900:
        response.status = HTTP_400
        return 'Donnee invalide'
    elif v == None:
        response.status = HTTP_200
        return 'Donnee enregistré'


@hug.put('/pokemon/{name}')
def pokemon_update(name: hug.types.text, nouveaunom: hug.types.text, response):
    dbp = DBPokemon("root", "pokemon")
    v = dbp.callupdatepokemon(name, nouveaunom)
    if v == 900:
        response.status = HTTP_400
        return 'Donnee invalide'
    elif v == None:
        response.status = HTTP_200
        return str('Donnee modifié')


@hug.delete('/pokemon/{name}')
def pokemon_delete(name: hug.types.text, response):
    dbp = DBPokemon("root", "pokemon")
    dbp.calldeletepokemon(name)
    response.status = HTTP_200


@hug.get('/pokemon/{name}/features')
def pokemonlistcaracteristique(name: hug.types.text, response):
    dbp = DBPokemon("root", "pokemon")
    v = dbp.callfindfeature(name)
    if v == []:
        response.status = HTTP_404
        return 'Donnee vide'
    else:
        response.status = HTTP_200
        return str(v)


@hug.post('/pokemon/{name}/features')
def pokemoncaracteristique_add(name: hug.types.text, transformation: hug.types.text, type1: hug.types.text, type2: hug.types.text, hp: hug.types.number, attack: hug.types.number, defense: hug.types.number, speedattack: hug.types.number, speeddefense: hug.types.number, speed: hug.types.number, response):
    dbp = DBPokemon("root", "pokemon")
    v = dbp.callinsertfeature(name, transformation, type1, type2, hp, attack, defense, speedattack, speeddefense, speed)
    if v == 900:
        response.status = HTTP_400
        return 'Donnee invalide'
    elif v == 800:
        response.status = HTTP_400
        return 'Donnee invalide'
    elif v == None:
        response.status = HTTP_200
        return 'Donnee enregistré'


@hug.put('/pokemon/{name}/features')
def pokemoncaracteristique_update(name: hug.types.text, transformation: hug.types.text, type1: hug.types.text, type2: hug.types.text, hp: hug.types.number, attack: hug.types.number, defense: hug.types.number, speedattack: hug.types.number, speeddefense: hug.types.number, speed: hug.types.number, response):
    dbp = DBPokemon("root", "pokemon")
    v = dbp.callupdatefeature(name, transformation, type1, type2, hp, attack, defense, speedattack, speeddefense, speed)
    if v == 900:
        response.status = HTTP_400
        return 'Donnee invalide'
    elif v == None:
        response.status = HTTP_200
        return 'Donnee modifié'


@hug.delete('/pokemon/{name}/features')
def pokemoncaracteristique_delete(name: hug.types.text, transformation: hug.types.text, type1: hug.types.text, type2: hug.types.text, response):
    dbp = DBPokemon("root", "pokemon")
    dbp.calldeletefeature(name, transformation, type1, type2)
    response.status = HTTP_200




@hug.get('/pokemon/type')
def listtype(response):
    dbp = DBPokemon("root", "pokemon")
    v = dbp.callfindalltype()
    if v == []:
        response.status = HTTP_404
        return 'Donnee vide'
    else:
        response.status = HTTP_200
        return str(v)


@hug.post('/pokemon/type')
def type_add(addtypedesignation: hug.types.text, response):
    dbp = DBPokemon("root", "pokemon")
    v = dbp.callinserttype(addtypedesignation)
    if v == 900:
        response.status = HTTP_400
        return 'Donnee invalide'
    elif v == None:
        response.status = HTTP_200
        return 'Donnee enregistré'


@hug.put('/pokemon/type/{designation}')
def type_update(designation: hug.types.text, response):
    dbp = DBPokemon("root", "pokemon")
    v = dbp.calldeletetype(designation)
    if v == 900:
        response.status = HTTP_400
        return 'Donnee invalide'
    elif v == None:
        response.status = HTTP_200
        return 'Donnee modifié'

