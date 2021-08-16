from django.contrib import admin

from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date', 'opened')
    list_display_links = ('id', 'question_text')
    search_fields = ('question_text',)
    list_editable = ('opened',)
    list_filter = ('opened', 'pub_date')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'votes')
    list_display_links = ('id', 'choice_text')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
