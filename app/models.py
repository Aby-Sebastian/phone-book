
from django.db import models

# Create your models here.



CONTACT_CATEGORY = (
    ("Home", "Home"),
    ("Personal", "Personal"),
    ("Bussiness", "Bussiness"),
)


class Contact(models.Model):

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	country_code = models.CharField(max_length=4, blank=True, default='+91')
	phone_number = models.CharField(max_length=10)
	email_id = models.EmailField(blank=True)
	favorite = models.BooleanField(default=False)
	image = models.ImageField(upload_to='images')  
	# category = models.choices()
	category = models.CharField(
        max_length = 20,
        choices = CONTACT_CATEGORY
        )

	class Meta:
		verbose_name_plural = "Contacts"
		
	def __str__(self):
		return self.first_name + ' ' + self.last_name
