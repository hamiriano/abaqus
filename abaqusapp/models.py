from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    initial_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Weight(models.Model):
    date = models.DateField()
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.date} - {self.asset.name} - {self.portfolio.name}"

class Price(models.Model):
    date = models.DateField()
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.asset.name}"

class InitialInvestment(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.portfolio.name} - {self.asset.name} - {self.quantity}"