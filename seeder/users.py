from reclass.models import User
import json

f = open('users.json')

data = json.load(f)

for i in data:
    user = User(**i)
    user.set_password('12345')
    user.save()
    print('User saved - ' + user.email)


# for i in range(10):
#     user = User.objects.order_by('?').first()
#     user.is_instructor = True
#     user.save()
#     print('User marked as instructor - ' + user.email)
