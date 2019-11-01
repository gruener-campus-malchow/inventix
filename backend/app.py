from sanic import Sanic, response
from sanic_cors import CORS

app = Sanic()
CORS(app)


@app.route("/login", methods=["POST"])
async def login(request):
    print(request.args)
    if request.json["username"] == "testuser" and request.json["password"] == "password":
        return response.json({"logged_in": True})
    else:
        return response.json({"logged_in": False})


@app.route("/items")
async def items(request):
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
