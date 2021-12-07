from reclass.models import Subject, User, Enrollment

users = User.objects.filter(is_admin=False)

for user in users:
    subject = Subject.objects.order_by('?')[0]
    try:
        e = Enrollment.objects.get(user=user, subject=subject)
        print('Already enrolled')
    except:
        enroll = Enrollment(user=user, subject=subject)
        enroll.save()
        print('enrolled')
