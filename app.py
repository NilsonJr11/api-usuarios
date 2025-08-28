from flask import Flask, jsonify, request

app = Flask(__name__)
usuarios = []

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    novo_usuario = request.json
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

# 👇 Aqui está a rota para a página inicial
@app.route('/')
def home():
    return 'Bem-vindo à minha API!'

if __name__ == "__main__":
    app.run(debug=True)


