'''
* Filename: models.py
* Author: InfraTie
* Edited by: Justin Moua
* 
* NOTES:
* 
*  
* The following models (or classes) are:
*   - Inspection(models.Model) 
*       - Subclasses models.model
*       - Contains the following attributes/columns:
*           - Unique ID (already set by MySQL)
*           - Attribute_1
*           - Attribute_2
*           - Attribute_3
*           - Attribute_4
*           - Attribute_5
*           - Attribute_6
*           - Attribute_7
*
*   - Condition(models.Model)
*       - Subclasses models.model
*       - Uses foreign key from inspection model
*       - Contains the following attributes/columns:
*           - Unique ID (already set by MySQL)
*           - Attribute_1
*           - Attribute_2
*           - Attribute_3
*           - Attribute_4
*           - Attribute_5
*           - Attribute_6
*           - Attribute_7
* 
'''
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