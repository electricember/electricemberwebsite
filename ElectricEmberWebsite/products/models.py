from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image1 = models.ImageField(upload_to='product_images', blank=True,
                               null=True)
    
    # ToDo
    #category = (fk -> categories)
    #mfr = (fk -> mfrs)
    #msrp = (decimal)
    #price = (decimal)
    #is_discounted = (bool)
    #discount_pct = (0 >= x >= 1)
    #product_num = (alphanum or integer)
    #upc = (integer)
    #asin = (alphanum)
    #sku = (alphanum or integer)
    #stock_avail = (integer)
    #stock_reserved = (integer)
    #creator = (fk -> employees)
    #special_instructions = (text)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-id']
