from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='POST':
        pokemon_name = request.form["pokemon"]
        url = 'https://pokeapi.co/api/v2/pokemon/'+pokemon_name.lower()+'/'
        results = requests.get(url)
        id = json.loads(results.text)['id']
        image_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+str(id)+".png"
        name = (json.loads(results.text)['name']).title()
        height=str(json.loads(results.text)['height'])
        weight=str(json.loads(results.text)['weight'])
        base_experience=str(json.loads(results.text)['base_experience'])
        pokemon_type_list=[]
        length_type=len(json.loads(results.text)['types'])
        for i in range(0,length_type):
                val=(json.loads(results.text)["types"][i]["type"]["name"]).title()
                pokemon_type_list.append(val)
        pokemon_type = ",".join(pokemon_type_list)
        pokemon_abilities_list=[]
        length_abilities = len(json.loads(results.text)['abilities'])
        for i in range(0,length_abilities):
            val=(json.loads(results.text)["abilities"][i]["ability"]["name"]).title()
            pokemon_abilities_list.append(val)
        pokemon_abilities = ",".join(pokemon_abilities_list)
        speed=str(json.loads(results.text)['stats'][0]['base_stat'])
        special_defense=str(json.loads(results.text)['stats'][1]['base_stat'])
        special_attack=str(json.loads(results.text)['stats'][2]['base_stat'])
        defense=str(json.loads(results.text)['stats'][3]['base_stat'])
        attack=str(json.loads(results.text)['stats'][4]['base_stat'])
        hp=str(json.loads(results.text)['stats'][5]['base_stat'])
        return render_template("index.html",image_url=image_url,name=name,height=height,weight=weight,base_experience=base_experience,type=pokemon_type,abilities=pokemon_abilities,speed=speed,special_defense=special_defense,special_attack=special_attack,defense=defense,attack=attack,hp=hp)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
