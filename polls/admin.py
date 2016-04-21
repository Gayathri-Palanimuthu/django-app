from polls.models import Poll, Choice
from django.contrib import admin



class ChoiceInline(admin.TabularInline): # Rather registering 'Choice' model in admin, give it as Poll inline to make it feasible
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question'] # To order fields
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question'] #Search box
    date_hierarchy = 'pub_date'  # Date filter tabs
    fieldsets = [
        ('Poll Question',               {'fields': ['question']}), # fieldset to give title to each fields
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), # 'collapse' class to show/hide fieldset
    ]
    inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)
