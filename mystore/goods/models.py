from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'
        ordering = ("id",)

    def __str__(self):
        return self.name
    



class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Зображення')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Ціна')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Знижка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категорія')
    rootstock = models.CharField(max_length=200, verbose_name='Підвой')
    ripening_period = models.CharField(max_length=200, verbose_name='Терміни дозрівання')
    fruit_weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Маса плодів у грамах')
    pollinators = models.CharField(max_length=200, blank=True, null=True, verbose_name='Опилювачі')  
    frost_resistance = models.CharField(max_length=200, blank=True, null=True, verbose_name='Морозостійкість')  
    disease_resistance = models.CharField(max_length=200, blank=True, null=True, verbose_name='Стійкість до захворювань')  
    transportability = models.CharField(max_length=200, blank=True, null=True, verbose_name='Транспортабельність')


    class Meta:
        db_table = 'product'
        verbose_name = 'Саджанець'
        verbose_name_plural = 'Саджанці'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name} Кількість - {self.quantity}'

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    

    def display_id(self):
        return f"{self.id:05}"


    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price


