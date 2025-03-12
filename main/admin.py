from django.contrib import admin

from main.models import Curses, Disciplines, News, NewsTag, Students, Lecturers, Documents


class NewsTagTabularAdmin(admin.TabularInline):
    model = NewsTag
    extra = 0

class LecturersTabularAdmin(admin.TabularInline):
    model = Lecturers
    extra = 0
    classes = ['collapse']

class DocumentsTabularAdmin(admin.TabularInline):
    model = Documents
    extra = 0
    classes = ['collapse']


class DisciplinesTabularAdmin(admin.TabularInline):
    model = Disciplines
    extra = 0
    classes = ['collapse']


@admin.register(Curses)
class CursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['image_tag']
    fields = [
        'name',
        'edu_form',
        'slug',
        'description',
        'sertificate',
        'structure',
        'image',
        'image_tag',
        'hours',
    ]
    
    list_display = ['name', 'image_tag',]
    inlines = (DocumentsTabularAdmin, DisciplinesTabularAdmin, LecturersTabularAdmin)

@admin.register(Disciplines)
class DisciplinesAdmin(admin.ModelAdmin):
    inlines = (LecturersTabularAdmin,)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Lecturers)
class LecturersAdmin(admin.ModelAdmin):
    pass

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = (NewsTagTabularAdmin,)
