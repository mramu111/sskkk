import binascii
import os
from django.contrib.auth.models import User
from django.db import models
from django.db import models


class Token(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=40, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        return super(Token, self).save(*args, **kwargs)

    def generate_token(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __unicode__(self):
        return self.token



class Member(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    extension = models.CharField(max_length = 20)
    #roles = models.ForeignKey(ManagerModels.Roles)
    #modules = models.ForeignKey(ManagerModels.Modules)
    #added_by = models.ForeignKey('self', null=True, blank=True, related_name='member_added_by')
    #modified_by = models.ForeignKey('self', null=True, blank=True, related_name='member_modified_by')
    #reports_to = models.ForeignKey('self', null=True, blank=True, related_name='member_reports_to')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "%s-%s" % (self.name, self.email)
    def __str__(self):
        return "%s-%s" % (self.name, self.email)
