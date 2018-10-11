from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class Category_sector(models.Model):
    sector = models.CharField(max_length=30, verbose_name="Sector")

    def __str__(self):
        return self.sector

class Category_industry(models.Model):
    industry = models.CharField(max_length=30, verbose_name="Industry")

    def __str__(self):
        return self.industry

class Stock(models.Model):
    exchange = models.CharField(max_length=10, verbose_name="Stock exchange")
    symbol = models.CharField(max_length=10, verbose_name="Symbol")
    company = models.CharField(max_length=50, verbose_name="Company")
    ipoYear = models.PositiveIntegerField(validators=[MinValueValidator(1900)], verbose_name="IPO Year")
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Key in date")
    category_sector = models.ForeignKey('Category_sector', on_delete=models.CASCADE, verbose_name="Sector")
    category_industry = models.ForeignKey('Category_industry', on_delete=models.CASCADE, verbose_name="Industry")

    class Meta:
        verbose_name = "Stock data"
        ordering = ['symbol']

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.symbol

class Stock_daily(models.Model):
    symbol = models.CharField(max_length=10, verbose_name="Symbol")
    open = models.FloatField(verbose_name="Open price")
    high = models.FloatField(verbose_name="High price")
    low = models.FloatField(verbose_name="Low price")
    close = models.FloatField(verbose_name="Close price")
    volume = models.FloatField(verbose_name="Volume")
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Key in date")

    class Meta:
        verbose_name = "Stock daily"
        ordering = ['date']

    def __str__(self):
        return self.symbol
