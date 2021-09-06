from flask_orator import Orator
from app import factory

server = factory()
db = Orator(server)


@server.route("/")
def hello_world():
    from app.models.User import User
    user = User.create({
        "name": "Yubaraj",
        "email": "companion.krish@gmail.com",
    })
    print(user)
    return "<p>Hello, World!</p>"
