from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание', max_length=200)
    text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Дата публикации')
    user = models.CharField('Имя пользователя', max_length=50)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title