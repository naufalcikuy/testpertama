from django.contrib import admin
from .models import Post
from .models import Knowledge
from .models import BabyBio

admin.site.register(Post)
admin.site.register(Knowledge)
admin.site.register(BabyBio)

# Register your models here.
