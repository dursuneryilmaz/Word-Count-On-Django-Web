from django.contrib import admin
from .models import WordCount


# Register your models here.
class WordCountAdmin(admin.ModelAdmin):
    list_display = ['title', 'app_name', 'timestamp', 'active']
    list_filter = ['timestamp']
    search_fields = ['title', 'comments']

    class Meta:
        model = WordCount


admin.site.register(WordCount, WordCountAdmin)
