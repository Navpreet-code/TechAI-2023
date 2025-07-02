from django.contrib import admin
from AIapp.models import person
from AIapp.models import FAQ
from AIapp.models import MyReview
from AIapp.models import Contactus
from AIapp.models import HelpandSupport
from AIapp.models import user_register
from AIapp.models import Blog
from AIapp.models import video
from AIapp.models import category
from AIapp.models import structure
from AIapp.models import initiative


# Register your models here.
admin.site.register(person)
admin.site.register(FAQ)
admin.site.register(MyReview)
admin.site.register(Contactus)
admin.site.register(user_register)
admin.site.register(Blog)
admin.site.register(video)
admin.site.register(category)
admin.site.register(structure)
admin.site.register(initiative)



