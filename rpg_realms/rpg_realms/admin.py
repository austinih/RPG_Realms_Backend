from django.contrib import admin
from .models import Publisher, RPG, User, Review, Comment


admin.site.register(Publisher)
admin.site.register(RPG)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comment)