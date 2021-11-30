from reclass.models import Enrollment, User, Subject

users = User.objects.all()

for user in users:
    subject = Subject.objects.order_by('?').first()
    try:
        enrollment = Enrollment(user=user, subject=subject)
        enrollment.save()
        print(user.email + ' got enrolled in subject ' + subject.title)
    except:
        print('Unable to enroll')
