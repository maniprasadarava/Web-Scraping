from django.db import models





class csvdatamodel(models.Model):
    name=models.CharField(max_length=450)
    rating=models.CharField(max_length=400)
    reviews=models.CharField(max_length=400)
    type=models.CharField(max_length=400)
    hq=models.CharField(max_length=400)
    employees=models.CharField(max_length=400)

    def __str__(self):
        return self.name, self.rating, self.reviews, self.type, self.hq, self.employees

    class Meta:
        db_table = 'csvdatamodel'





