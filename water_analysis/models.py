from django.db import models

class pHReading(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2) 

    def __str__(self):
        return f'pH: {self.value}'

class HardnessMeasurement(models.Model):
    edta_volume = models.DecimalField(max_digits=20, decimal_places=5)
    edta_molarity = models.DecimalField(max_digits=10, decimal_places=5, default=0.01)
    znso4_volume = models.DecimalField(max_digits=10, decimal_places=5)
    znso4_concentration = models.DecimalField(max_digits=10, decimal_places=5, default=0.01)  # Default value

    def __str__(self):
        return f'Hardness Measurement (EDTA Volume: {self.edta_volume} mL)'

class AlkalinityMeasurement(models.Model):
    volume_hcl_phenolphthalein = models.DecimalField(max_digits=10, decimal_places=5)
    volume_hcl_methyl_orange = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return f'Alkalinity Measurement (Phenolphthalein Volume: {self.volume_hcl_phenolphthalein} mL, Methyl Orange Volume: {self.volume_hcl_methyl_orange} mL)'

class TDSMeasurement(models.Model):
    weight_dish_filtrate = models.DecimalField(max_digits=10, decimal_places=5)
    weight_dish = models.DecimalField(max_digits=10, decimal_places=5)
    volume_sample = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return f'TDS Measurement (Weight Dish + Filtrate: {self.weight_dish_filtrate} g)'

class TurbidityMeasurement(models.Model):
    depth_cm = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Turbidity Measurement (Depth: {self.depth_cm} cm)'

class CalculatedParameter(models.Model):
    parameter_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return f'{self.parameter_name}: {self.value}'

    def within_standard(self):
        # The logic to check if the parameter value is within the standard
        if self.parameter_name == 'pH':
            return 6.5 <= self.value <= 8.5
        elif self.parameter_name == 'hardness':
            return self.value <= 200
        elif self.parameter_name == 'alkalinity':
            return self.value <= 200
        elif self.parameter_name == 'turbidity':
            return self.value <= 1
        elif self.parameter_name == 'tds':
            return self.value <= 500
        else:
            return False
