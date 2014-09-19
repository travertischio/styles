from django.db import models

class BeerStyle(models.Model):
	name = models.CharField(max_length=200)
	ibu = models.IntegerField(default=1)
	srm = models.IntegerField(default=1)
	abv = models.DecimalField(max_digits=4, decimal_places=2, default=1)
	country = models.CharField(max_length=200)
	similarity = models.IntegerField(default=400)
	brands = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

	def comparison(self, ibus, srms, abvs, countrys):
		difference = abs(ibus-self.ibu) + abs(srms-self.srm) + abs(abvs-self.abv)
		if countrys != self.country:
			difference += 5
		self.similarity = difference
		self.save()
		return