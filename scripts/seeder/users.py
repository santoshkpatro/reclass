from reclass.models import User
import json

f = open('users-raw.json')

data = json.load(f)

for i in data:
    user = User(**i)
    user.set_password('passsword')
    user.save()
    print('user saved to db - ', user.email)
