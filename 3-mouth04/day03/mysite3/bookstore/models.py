from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField('书名', max_length=20)
    price = models.DecimalField('定价', max_digits=7, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=7, decimal_places=2, default=0.0)
    pub = models.CharField('出版社', max_length=50, default='')

    def __str__(self):
        return f'书名:{self.title}，出版社：{self.pub}\t，价格：{self.price}，市场价：{self.market_price}'
