from django.db import models
from django.db.models import *
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Categ(models.Model):

    class Meta:
        verbose_name_plural = 'Categorii de produse'

    name = CharField(max_length=128)

    def __str__(self):
        return self.name

class Produs(models.Model):

    class Meta:
        verbose_name_plural = 'Produse'

    denumire = CharField(max_length=128)

    garantie_luni = IntegerField()
    lansat = DateField()
    descriere = TextField()
    categ = ForeignKey(Categ, on_delete=DO_NOTHING)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.denumire}'

class Magazin(models.Model):

    class Meta:
        verbose_name_plural = 'Magazine'

    magazin = CharField(max_length=128)
    retea = CharField(max_length=128)
    judet = CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f'{self.magazin} ({self.judet})'


class OperatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    judet = models.CharField(max_length=128, blank=True, null=True)  # Câmp pentru județ

    def __str__(self):
        return f"{self.user.username} - {self.judet or 'Fără județ'}"


class Cerere(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cereri')
    data_cerere = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cerere de la {self.client.username} din {self.data_cerere}"


class Preturi(models.Model):
    cerere = models.ForeignKey(Cerere, on_delete=models.CASCADE, related_name='preturi')
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    magazin = models.ForeignKey(Magazin, on_delete=models.CASCADE)
    pret = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produs.denumire} - {self.magazin.magazin}: {self.pret} lei"

class SelectedData(models.Model):
    product = models.ForeignKey(Produs, on_delete=models.CASCADE)
    store = models.ForeignKey(Magazin, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Prețul, inițial NULL
    created_at = models.DateTimeField(default=now, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Selected Data'

    def __str__(self):
        return f'{self.product.denumire} - {self.store.magazin}'

class SavedPrices(models.Model):
    product = models.ForeignKey(Produs, on_delete=models.CASCADE)
    store = models.ForeignKey(Magazin, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilizatorul care a salvat datele
    date_saved = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Saved Prices'

    def __str__(self):
        return f'{self.product.denumire} - {self.store.magazin} - {self.price}'

# Extindere model utilizator pentru puncte
class OperatorPoints(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="points")
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}: {self.points} puncte"

# Model pentru produse din sectiunea "Incentive"
class IncentiveProduct(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()  # Pret in puncte
    image = models.ImageField(upload_to="incentive_products/", blank=True, null=True)

    def __str__(self):
        return self.name

# Model pentru istoricul achizitiilor
class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchase_history")
    product = models.ForeignKey(IncentiveProduct, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} a cumparat {self.product.name} pe {self.purchase_date}"