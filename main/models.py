from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class Curses(models.Model): 
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    edu_form = models.CharField(max_length=15, verbose_name='Форма обучения')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    sertificate = models.URLField(max_length=150, unique=True, verbose_name='Сертификат об окончании (URL)')
    structure = models.TextField(max_length=150, unique=True, verbose_name='Структура программы')
    image = models.ImageField(upload_to='curse_images', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'curse'
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name

    def get_image(self):
        if not self.image:
            return '/static/images/no_photo.png'
        return self.image.url

    def image_tag(self):
        return mark_safe('<img src="%s" width="70" height="70" />' % self.get_image())

    image_tag.short_description = 'Фото'


class Disciplines(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    curse = models.ForeignKey(to=Curses, on_delete=models.CASCADE, verbose_name='Направление')

    class Meta:
        db_table = 'discipline'
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return self.name


class Students(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    surname = models.CharField(max_length=150, blank=True, null=True, verbose_name='Отчество')
    # birth_date = 
    curse = models.ForeignKey(to=Curses, on_delete=models.CASCADE, verbose_name='Направление')

    class Meta:
        # unique_together = ('first_name','last_name')
        db_table = 'student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Lecturers(models.Model):
    first_name = models.CharField(max_length=150, unique=True, verbose_name='Имя')
    last_name = models.CharField(max_length=150, unique=True, verbose_name='Фамилия')
    surname = models.CharField(max_length=150, unique=True, verbose_name='Отчество')
    discipline = models.ForeignKey(to=Disciplines, on_delete=models.CASCADE, verbose_name='Дисциплина')
    
    class Meta:
        db_table = 'lecturer'
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Document(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    url = models.URLField(max_length=150, unique=True, verbose_name='Ссылка на документ')
    curse = models.ForeignKey(to=Curses, on_delete=models.CASCADE, verbose_name='Направление')

    class Meta:
        db_table = 'document'
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


