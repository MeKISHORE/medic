from django.db import models

# Create your models here.
class reg(models.Model):
    Hopital_id=models.CharField(max_length=20)
    hospital_name=models.CharField(max_length=150)
    hospital_mail=models.EmailField()
    Hopital_t_beds=models.IntegerField(default="0")
    Hopital_r_beds = models.IntegerField(default="0")
    Hopital_v_beds = models.IntegerField(default="0")
    Hospital_pass=models.CharField(max_length=30)

    def __str__(self):
        return self.hospital_name



class patient_data(models.Model):
    hospital_name=models.CharField(max_length=30)
    hospital_id=models.CharField(max_length=30)
    P_name=models.CharField(max_length=20)
    A_name=models.CharField(max_length=150)
    Mobile=models.IntegerField(default='0')
    P_address=models.CharField(max_length=30)
    process = models.CharField(default='pending', max_length=30)



    def __str__(self):
        return self.hospital_name