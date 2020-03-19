from django.db import models

class School(models.Model):
    full_name = models.CharField(max_length=512, null=True, blank=True)
    ruian_code = models.CharField(max_length=512, null=True, blank=True)
    address_1 = models.CharField(max_length=256, null=True, blank=True)
    address_2 = models.CharField(max_length=256, null=True, blank=True)
    address_3 = models.CharField(max_length=256, null=True, blank=True)
    principal_name = models.CharField(max_length=256, null=True, blank=True)
    legal_form = models.CharField(max_length=10, null=True, blank=True) # Pravní Forma
    company_id = models.CharField(max_length=10, null=True, blank=True) # IČO