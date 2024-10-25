from unicodedata import category
from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        params = {
            'ttbkey' : 'ttbbabyms9991353001',
            'start' : '1',
            'QueryType' : 'ItemNewSpecial',
            'MaxResults': '10',
            'SearchTarget' : 'book',
            'output' : 'js',
            'Version' : '20131101',
        }
        response = requests.get('https://www.aladin.co.kr/ttb/api/ItemList.aspx', params=params)
        data = response.json()

        for item in data['item']:
            my_model = cls(isbn=item['isbn'], author=item['author'], title=item['title'], category_name=item['categoryName'],
                           category_id=item['categoryId'], price=item['priceStandard'], fixed_price=item['fixedPrice'], pub_date=item['pubDate'])
            my_model.save()
