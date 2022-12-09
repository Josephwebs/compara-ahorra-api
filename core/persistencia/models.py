# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=90, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    compare_at_price = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'compare_at_price': self.compare_at_price,
            'image': self.image,
        }