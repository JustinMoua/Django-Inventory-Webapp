from django.db import models

class Inspection(models.Model):
    Attribute_1 = models.CharField(max_length=50)
    Attribute_2 = models.CharField(max_length=50)
    Attribute_3 = models.CharField(max_length=50)
    Attribute_4 = models.CharField(max_length=50)
    Attribute_5 = models.CharField(max_length=50)
    Attribute_6 = models.CharField(max_length=50)
    Attribute_7 = models.CharField(max_length=50)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "Inspection"

class Condition(models.Model):
    Inspection = models.ForeignKey( #foreign key is here. So, there is a column of "inspection_id" that ties in with the inspection table's ids.
        Inspection,                 #https://docs.djangoproject.com/en/5.2/topics/db/examples/many_to_one/
        on_delete=models.CASCADE
    )
    Attribute_1 = models.CharField(max_length=50)
    Attribute_2 = models.CharField(max_length=50)
    Attribute_3 = models.CharField(max_length=50)
    Attribute_4 = models.CharField(max_length=50)
    Attribute_5 = models.CharField(max_length=50)
    Attribute_6 = models.CharField(max_length=50)
    Attribute_7 = models.CharField(max_length=50)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = "Condition"