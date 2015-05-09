from django.contrib import admin
from mainsite.models import Testimonial, Problem, ExtendedFlatPage
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
        model = ExtendedFlatPage


class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'language', 'sites')}),
    )


admin.site.unregister(FlatPage)
admin.site.register(ExtendedFlatPage, ExtendedFlatPageAdmin)
admin.site.register(Testimonial)
admin.site.register(Problem)
