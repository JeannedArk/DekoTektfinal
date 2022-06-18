from django.contrib import admin
from .models import Project, ProjectGallery
import admin_thumbnails
   

@admin_thumbnails.thumbnail('image')
class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'created_date', 'modified_date', 'is_available')
    list_editable = ('is_available',)
    prepopulated_fields = {'slug':('project_name',)}
    inlines = [ProjectGalleryInline]

admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectGallery)
