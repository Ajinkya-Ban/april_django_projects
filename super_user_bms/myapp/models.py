from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Vendor(models.Model):
    full_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="media/vendor/")
    address = models.TextField()
    mobile = models.CharField(max_length=11)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '1.Vendor'

    def __str__(self):
        return self.full_name

class Unit(models.Model):
    title = models.CharField(max_length = 15)
    short_name = models.CharField(max_length = 10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '2.Unit'
    

class Product(models.Model):
    title = models.CharField(max_length = 100)
    details = models.CharField(max_length = 150)
    unit =  models.ForeignKey(Unit, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/prod_imgs/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = '3.Product'

    
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    qty = models.FloatField()
    price = models.FloatField()
    total_amt = models.FloatField(default=0)
    pur_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='4.Purchase'

    def save(self, *args,**kwargs):
        self.total_amt = self.qty * self.price
        super(Purchase,self).save(*args,**kwargs)
        inventory = Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
            totalBal = inventory.total_bal_qty + self.qty
        else:
            totalBal = self.qty
        Inventory.objects.create(
            product = self.product,
            purchase=self,
            sale = None,
            pur_qty = self.qty,
            sale_qty=None,
            total_bal_qty=totalBal
        )

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.FloatField()
    price = models.FloatField()
    total_amt = models.FloatField(editable=False)
    sale_date = models.DateTimeField(auto_now_add=True)

    customer_name = models.CharField(max_length = 50)
    cutomer_mob = models.CharField(max_length = 10)
    customer_add = models.CharField(max_length = 150)

    class Meta:
        verbose_name_plural="5.Sale"
    def save(self, *args,**kwargs):
        self.total_amt = self.qty * self.price
        inventory = Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
            totalBal = inventory.total_bal_qty - self.qty
            if totalBal < 0:
                raise ValidationError('Not enough inventory to complete this sale.')
        else:
            totalBal = -self.qty
            if totalBal < 0:
                raise ValidationError('Not enough inventory to complete this sale.')
        super(Sale,self).save(*args,**kwargs)

        Inventory.objects.create(
            product = self.product,
            purchase=None,
            sale = self,
            pur_qty = None,
            sale_qty=self.qty,
            total_bal_qty=totalBal
        )
    
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE,default=0,null=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE,default=0,null=True)
    pur_qty = models.FloatField(default=0,null=True)
    sale_qty = models.FloatField(default=0,null=True)
    total_bal_qty = models.FloatField()

    class Meta:
        verbose_name_plural="6.Inventory"
    
    
    
    
    
    
    
    
    
    
    
    
    
    