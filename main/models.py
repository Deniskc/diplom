from django.db import models
from django.utils.safestring import mark_safe

from users.models import User


class Curses(models.Model): 
    name = models.CharField(max_length=256, unique=True, verbose_name='Название')
    edu_form = models.CharField(max_length=15, verbose_name='Форма обучения')
    slug = models.SlugField(max_length=256, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание', default='Описание программы еще не добавлено')
    sertificate = models.URLField(blank=True, null=True, verbose_name='Сертификат об окончании (URL)')
    structure = models.TextField(blank=True, null=True, verbose_name='Структура программы', default='Структура программы еще не добавлена')
    hours = models.IntegerField(blank=True, null=True,verbose_name='Количество часов')
    image = models.ImageField(upload_to='curse_image', blank=True, null=True, verbose_name='Изображение')

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
        return mark_safe('<img src="%s" width=150px height=150px />' % self.get_image())

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
    birth_date = models.DateField(max_length=10, blank=True, null=True, verbose_name='Дата рождения')
    curse = models.ForeignKey(to=Curses, on_delete=models.CASCADE, verbose_name='Направление', blank=True, null=True,)
    email = models.EmailField(blank=True, null=True,verbose_name='Email')
    phone = models.CharField(blank=True, null=True,verbose_name='Номер телефона')
    description = models.TextField(verbose_name='Примечания', null=True, blank=True)
    curse_is_paid = models.BooleanField(verbose_name='Оплачено?', default=False)


    class Meta:
        db_table = 'student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Lecturers(models.Model):
    first_name = models.CharField(max_length=150, unique=True, verbose_name='Имя')
    last_name = models.CharField(max_length=150, unique=True, verbose_name='Фамилия')
    surname = models.CharField(max_length=150, unique=True, verbose_name='Отчество')
    education = models.CharField(max_length=150, unique=True, verbose_name='Образование', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    discipline = models.ForeignKey(to=Disciplines, on_delete=models.CASCADE, verbose_name='Дисциплина')
    image = models.ImageField(upload_to='lecturer_image', blank=True, null=True, verbose_name='Изображение')
    curse = models.ForeignKey(to=Curses, on_delete=models.CASCADE, verbose_name='Направление', null=True, blank=True)

    
    class Meta:
        db_table = 'lecturer'
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Documents(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    url = models.URLField(max_length=150, unique=True, verbose_name='Ссылка на документ')
    curse = models.ForeignKey(to=Curses, on_delete=models.CASCADE, verbose_name='Направление')

    class Meta:
        db_table = 'document'
        verbose_name = 'Документ'
        verbose_name_plural = 'Добавить документы'

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', default='Why Lead Generation is Key for Business Growth')
    subtitle = models.TextField(verbose_name='Подзаголовок', default='A small river named Duden flows by their place and supplies it with the necessary regelialia.')
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст новости', blank=True, null=True)
    image = models.ImageField(upload_to='news_image', blank=True, null=True, verbose_name='Изображение', default='static/images/person-default.png')
    slug = models.SlugField(max_length=256, unique=True, blank=True, null=True, verbose_name='URL')


    class Meta:
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class NewsTag(models.Model):
    tag = models.CharField(max_length=50, verbose_name='Тег')
    new = models.ForeignKey(to=News, on_delete=models.CASCADE, verbose_name='Новость', blank=True, null=True,)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    