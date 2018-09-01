from django.db import models
from django.utils import timezone 

class Temp_user(models.Model):
    uname = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    token = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return self.uname

    def varify_time(self, now):
        result = True
        time_delta = now - self.time
        if time_delta.days > 0:
            result = False
        elif time_delta.seconds > 1800:
            result = False
        return result

    def now_plus_30(): 
        return datetime.now() + datetime.timedelta(hours = 2)

    def migrate(self):
        user = User.objects.create_user(self.uname, password=self.password, email=self.email)
        return redirect('index')