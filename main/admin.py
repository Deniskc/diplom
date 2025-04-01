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
        'paid_or_free',
        'price',
    ]
    
    list_display = ['name', 'image_tag',]
    inlines = (DocumentsTabularAdmin, DisciplinesTabularAdmin, LecturersTabularAdmin)

@admin.register(Disciplines)
class DisciplinesAdmin(admin.ModelAdmin):
    inlines = (LecturersTabularAdmin,)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
        fields = [
            'last_name',
            'first_name',
            'surname',
            'birth_date',
            'curse',
            'email',
            'phone',
            'description',
            'curse_is_paid',
        ]

        list_display = [
            'last_name',
            'first_name',
            'surname',
            'curse_is_paid',
        ]

        readonly_fields = ['curse_id']
        list_editable = ['curse_is_paid',]

@admin.register(Lecturers)
class LecturersAdmin(admin.ModelAdmin):
    pass

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title','id',)}
    list_display = [
        'title',
        'date',
        'image_tag',
    ]
    inlines = (NewsTagTabularAdmin,)
