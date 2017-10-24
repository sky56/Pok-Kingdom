from flask import Flask, render_template, request, send_file
import requests
import json

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='POST':
        pokemon_name = request.form["pokemon"].strip()
        if len(pokemon_name) == 0:
            error_message = "Enter Pokémon Name!!"
            return render_template("index.html",error_empty_message=error_message,download_pokemon='download.html')
        else:
            url = 'https://pokeapi.co/api/v2/pokemon/'+pokemon_name.lower()+'/'
            results = requests.get(url)
            if results.status_code == 404:
                error_message = "Pokémon name is Incorrect!!"
                return render_template("index.html",error_message=error_message,download_pokemon='download.html')
            elif results.status_code == 200:
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
                return render_template("index.html",image_url=image_url,name=name,height=height,weight=weight,base_experience=base_experience,type=pokemon_type,abilities=pokemon_abilities,speed=speed,special_defense=special_defense,special_attack=special_attack,defense=defense,attack=attack,hp=hp,download_pokemon='download.html')
            else:
                error_message = "Internal error occurred. Please try later!!"
                return render_template("index.html",error_message=error_message,download_pokemon='download.html')
    return render_template("index.html",download_pokemon='download.html')

@app.route("/download/")
def download():
    return send_file("Pokemon_List.csv", attachment_filename="Your_Pokemon_List.csv", as_attachment=True)

if __name__ == "__main__":
    app.run()
