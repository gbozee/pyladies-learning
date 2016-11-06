from __future__ import unicode_literals

from django.db import models
from django.db.models.functions import Length

# Create your models here.


class PersonQuerySet(models.QuerySet):

    def only_9_length(self, number):
        return self.first_name_count().filter(f_count=number)

    def first_name_count(self):
        return self.annotate(
            f_count=Length('first_name'))


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    objects = PersonQuerySet.as_manager()
    # username = models.Char

    @property
    def n_length(self):
        return len(self.first_name)

    def __repr__(self):
        return "<Person: %s %s>" % (self.first_name, self.last_name)

    def __str__(self):
        return self.first_name


class Doll(models.Model):
    person = models.ForeignKey(Person, related_name='dolls')
    name = models.CharField(max_length=10, blank=True, null=True)
