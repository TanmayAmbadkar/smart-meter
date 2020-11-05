from django.db import models

# Create your models here.

class Meter(models.Model):

    device_id = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.device_id


class Reading(models.Model):

    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    clk = models.DateTimeField(auto_now_add=True)
    current = models.FloatField()
    voltage = models.FloatField()
    signal_strength = models.FloatField()

    def __str__(self):
        return f"{self.meter.device_id} {self.clk}"
