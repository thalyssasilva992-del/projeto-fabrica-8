from flask import Flask, jsonify, request

app = Flask (__name__)

musicas = [
    {
        "id": 1,
         "titulo": "Astronomia",
         "artista": "Tony Igy",
         "duracao": 236,
         "url": "https://example.com/tony-igy-astronomia"
    }
]

@app.route("/tacks", methods=["GET"])
def listar_musicas():
    return jsonify(musicas)

@app.route("/tracks/<id>", methods=["GET"])
def buscar_musica(id):
    musica = next((m for m in musicas if m["id"] == id), None)
    if not musica:
        return jsonify({"erro": "Musica nao encontrada!"}), 404
    
    return jsonify(musica) 

@app.route("/tracks", methods=["POST"])
def add_musica():
    dados = request.get_json()
    nova_musica = {
        "id": len(musicas) + 1,
        "titulo": dados["titulo"],
        "artista": dados["artista"],
        "duracao": dados["duracao"],
        "url": dados["url"]
    }
    musicas.append(nova_musica)
    return jsonify(nova_musica), 201

@app.route("/tracks/<id>", methods=["POST"])
def atualizar_musica(id):
    musica = next((m for m in musicas if m["id"] == id), None)
    if not musica:
        return jsonify({"erro": "Musica nao encontrada. "}), 404
    
    dados = request.get_json()
    musica["titulo"] = dados.get('titulo', dados["titulo"])
    musica["artista"] = dados.get('artista', dados["artista"])
    musica["duracao"] = dados.get('duracao', dados["duracao"])
    musica["url"] = dados.get('url', dados["url"])
    return musica

@app.route("/tracks/<id>", methods=["DELETE"])
def excluir_musica(id):
   global musicas
   musica = next((m for m in musicas if m["id"] == id), None)
   if not musica:
       return jsonify({"erro": "Musica nao encontrada."}), 404
   
   musicas = [m for m in musicas if m['id'] != id]
   return jsonify({"mensage": "Musica excluida com sucesso."})