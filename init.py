from WebExtract import ExtractWEB
from db import DBPokemon

def transferdatafromdatabase(dbp, lstType, lstPokemon):
    for typ in lstType:
        v = dbp.callinserttype(typ)
        if v == 900:
            print('Type deja inseré: ' + typ)

    for pk in lstPokemon:
        nom = pk[1][0]
        v = dbp.callinsertpokemon(nom)
        if v == 900:
            print('Pokemon deja inseré: ' + nom)

    for pk in lstPokemon:
        identifiant = pk[0]

        if len(pk[1]) == 1:
            nom = pk[1][0]
            trans = ''
        else:
            nom = pk[1][0]
            trans = pk[1][1]

        if len(pk[2]) == 1:
            type1 = pk[2][0]
            type2 = ''
        else:
            type1 = pk[2][0]
            type2 = pk[2][1]

        total = pk[3]
        hp = pk[4]
        attack = pk[5]
        defense = pk[6]
        speedattack = pk[7]
        speeddefense = pk[8]
        speed = pk[9]

        v = dbp.callinsertfeature(nom, trans, type1, type2, hp, attack, defense, speedattack, speeddefense, speed)
        if v == 900:
            print('Caracteristique pokemon deja inseré: ' + nom + ' -> ' + trans + ' -> ' + type1 + ' -> ' + type2)
        elif v == 800:
            print('ERREUR REFERENCE caracteristique pokemon: ' + nom + ' -> ' + trans + ' -> ' + type1 + ' -> ' + type2)

if __name__ == '__main__':


    dbp = DBPokemon("root", "pokemon")
    dbp.initdb()

    v = ExtractWEB("datapokemon.html", "https://pokemondb.net/pokedex/all")

    lstType = v.extracttypefromhtml()
    lstPokemon = v.extractpokemonfromhtml()

    transferdatafromdatabase(dbp, lstType, lstPokemon)
