# pokemon
pokemon python projet

# Prérequis
Installez les applications suivante:
<ul>
  <li>mysql</li>
  <li>Cmder</li>
  <li>Python 3</li>
</ul>

# Configuration
Sous Cmder, avant l'execution du projet python, installez les packages via les commandes suivantes:

  <p><code>pip3 install beautifulsoup4</code></p>
  <p><code>pip3 install mysql-connector-python</code></p>
  <p><code>pip3 install requests</code></p>
  <p><code>pip3 install hug</code></p>
  <p><code>pip3 install falcon</code></p>


# Execution
Puis ouvrir le repertoire ou ce trouve les source, et taper la commande suivante:
  <code>
    <p>python init.py</p>
  </code>

Une fois la base compiler lancez hug:
  <code>
    <p>hug -f api.py</p>
  </code>
  
# Exemple requete HTTP
<p>
 Affiche la liste de Pokemon
<ul>
  <li>
    -GET- <code>localhost:8000/Pokemon</code>
    </li>
</ul>
</P><P>
Affiche les caracteristique sur un pokemon
  <ul>
  <li>
-GET- <code>localhost:8000/pokemon/{name}/features</code>
    </li>
</ul>
</P><P>
Affiche la liste de type d'energie
  <ul>
  <li>
-GET- <code>localhost:8000/Pokemon/type</code>
        </li>
</ul>

</P><P>
Requete sur pokemon
    <ul>
  <li>

-POST Ajout-     <code>localhost:8000/pokemon?add='newpokemon'</code></li><li>
-PUT Update-     <code>localhost:8000/pokemon/{name}?nouveaunom='ooo'</code></li><li>
-Delete-         <code>localhost:8000/pokemon/{name}</code>
        </li>
</ul>

</P><P>
 Requete sur liste des caracteristiques
      <ul>
  <li>
-POST Ajout-    <code>localhost:8000/pokemon/{name}/features?transformation=''&&type1=''&&type2=''&&hp=''&&attack=''&&defense=''&&speedattack=''&&speeddefense=''&&speed=''</code></li><li>
-PUT Update-    <code>localhost:8000/pokemon/{name}/features?transformation=''&&type1=''&&type2=''&&hp=''&&attack=''&&defense=''&&speedattack=''&&speeddefense=''&&speed=''</code></li><li>
-DELETE-        <code>localhost:8000/pokemon/{name}/features?transformation=''&&type1=''&&type2=''</code>
          </li>
</ul>

</P><P>
Requete sur les types:
      <ul>
  <li>

-POST: Ajout-    <code>localhost:8000/pokemon/type?addtypedesignation=''</code> </li><li>
-PUT: Update-    <code>localhost:8000/pokemon/type{designation}</code>
          </li>
</ul>

</P>
