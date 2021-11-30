from reclass.models import Notification, Subject, User, notification
import json
import random

f = open('notifications.json')

data = json.load(f)

tags_collection = ['important', 'compulsory', 'simple',
                   'easy', 'event', 'finance', 'payment', 'fest', 'assignment']

for e in data:
    user = User.objects.filter(is_instructor=True).order_by('?').first()
    subject = Subject.active_objects.filter(
        enrollments__user=user).order_by('?').first()

    # print(user)
    # print(subject)

    # print(random.choice(tags_collection))

    tags = []
    t = random.randint(0, 4)
    for i in range(t):
        tags.append(random.choice(tags_collection))

    print(tags)

    notification = Notification(**e, notifier=user, subject=subject,
                                tags=tags, is_published=True)
    notification.save()

    print('Notification saved - ' + notification.title)
