from django.contrib import admin

# Register your models here.

from main.models import Curses, Disciplines, Students, Lecturers, Document


class DocumentsTabularAdmin(admin.TabularInline):
    model = Document
    extra = 1

@admin.register(Curses)
class CursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["image_tag"]
    fields = [
        'name',
        'edu_form',
        'slug',
        'description',
        'sertificate',
        'structure',
        'image',
        'image_tag',
    ]
    list_display = ['name']
    inlines = (DocumentsTabularAdmin,)

@admin.register(Disciplines)
class DisciplinesAdmin(admin.ModelAdmin):
    pass

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Lecturers)
class LecturersAdmin(admin.ModelAdmin):
    pass