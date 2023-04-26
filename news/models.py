from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Nomi")
    content = models.TextField(blank=True, verbose_name="Kontent")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Publikatsiyta vaqti")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    is_published = models.BooleanField(default=True, verbose_name="Nashr etilgan")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Kategoriya")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-time_created']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Kategoriya")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
