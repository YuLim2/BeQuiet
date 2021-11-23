import User
from app import db

user = User.User('3', 'kingyulim', 'good!')
db.creat_all()
db.session.add(user)
db.seccion.commit()

print(user)
print("-----------------------------")
print(user.as_dict())
