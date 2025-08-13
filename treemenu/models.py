from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name="Название меню",
    )
    title = models.CharField(max_length=100, verbose_name="Название")
    url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
        verbose_name="Родительский заголовок",
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.title
