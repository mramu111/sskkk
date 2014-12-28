from django.contrib import admin
# Register your models here.
from itaas.apps.aws.models import Member,Token
admin.site.register(Member)
admin.site.register(Token)
