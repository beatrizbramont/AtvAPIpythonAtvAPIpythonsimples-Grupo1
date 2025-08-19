from flask import Flask, request, jsonify

app = Flask(__name__)


users = []
increment_id = 1  


#CREATE
@app.route("/users", methods=["POST"])
def create_user():
    global increment_id

    data = request.json
    if not data or "nome" not in data or "email" not in data:
        return jsonify({"error": "Campos 'nome' e 'email' são obrigatórios"}), 400

    new_user = {
        "id": increment_id,
        "nome": data["nome"],
        "email": data["email"]
    }
    users.append(new_user)
    increment_id += 1

    return jsonify(new_user), 201


#READ ALL-tudo
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


#READ-por ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Usuario nao foi encontrado."}), 404


#UPDATE 
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "Usuario nao foi encontrado."}), 404

    if "nome" in data:
        user["nome"] = data["nome"]
    if "email" in data:
        user["email"] = data["email"]

    return jsonify(user), 200


#DELETE 
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "Usuario nao encontrado"}), 404

    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "Usuario excluido com sucesso"}), 200


if __name__ == "__main__":
    app.run(debug=True)
