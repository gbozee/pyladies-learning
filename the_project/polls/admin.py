from django.contrib import admin
# from polls.models import Person
from .models import Person, Doll
# Register your models here.


class DollInline(admin.TabularInline):
    model = Doll


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'name_of_dolls', 'n_length',
                    'no_of_dolls'
                    ]
    search_fields = ['first_name', 'last_name']
    inlines = [
        DollInline,
    ]

    def no_of_dolls(self, obj):
        return obj.f_count
        # return obj.dolls.count()

    def name_of_dolls(self, obj):
        return [x.name for x in obj.dolls.all()]

    def get_queryset(self, request):
        queryset = super(PersonAdmin, self).get_queryset(request)
        return queryset.first_name_count().prefetch_related('dolls')
