from reclass.models import Subject
import json

f = open('subjects.json')

data = json.load(f)

for i in data:
    subject = Subject(**i)
    subject.save()
    print('subject save' + subject.title)
