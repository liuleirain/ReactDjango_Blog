from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost
from django.contrib import admin


class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'category', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    summernote_fields = ('content', )


admin.site.register(BlogPost, BlogPostAdmin)
