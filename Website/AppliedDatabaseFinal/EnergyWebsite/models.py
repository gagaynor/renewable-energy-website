from django.db import models

# Create your models here.

class Energy(models.Model):
    time = models.CharField(max_length=50, db_column='time',verbose_name='Date and Time')
    biomass = models.IntegerField(db_column='generation biomass',verbose_name='Biomass')
    brown_coal = models.IntegerField(db_column='generation fossil brown coal/lignite',verbose_name='Brown Coal')
    coal_derived_gas = models.IntegerField(db_column='generation fossil coal-derived gas',verbose_name='Coal-Derived Gas')
    gas = models.IntegerField(db_column='generation fossil gas',verbose_name='Gas')
    hard_coal = models.IntegerField(db_column='generation fossil hard coal',verbose_name='Hard Coal')
    oil = models.IntegerField(db_column='generation fossil oil',verbose_name='Oil')
    oil_shale = models.IntegerField(db_column='generation fossil oil shale',verbose_name='Oil Shale')
    peat = models.IntegerField(db_column='generation fossil prat',verbose_name='Peat')
    geothermal = models.IntegerField(db_column='generation geothermal',verbose_name='Geothermal')
    hydro_pumped_storage = models.IntegerField(db_column='generation hydro pumped storage consumption',verbose_name='Pumped Storage Consumption')
    hydro_ror = models.IntegerField(db_column='generation hydro run-of-river and poundage',verbose_name='Run-of-River')
    hydro_water_res = models.IntegerField(db_column='generation hydro water reservoir',verbose_name='Water Reservoir')
    marine = models.IntegerField(db_column='generation marine',verbose_name='Marine')
    nuclear = models.IntegerField(db_column='generation nuclear',verbose_name='Nuclear')
    other_renewable = models.IntegerField(db_column='generation other renewable',verbose_name='Other Renewable')
    solar = models.IntegerField(db_column='generation solar',verbose_name='Solar')
    waste = models.IntegerField(db_column='generation waste',verbose_name='Waste')
    offshore = models.IntegerField(db_column='generation wind offshore',verbose_name='Offshore Wind')
    onshore = models.IntegerField(db_column='generation wind onshore',verbose_name='Onshore Wind')
    forecast_day_ahead_solar = models.IntegerField(db_column='forecast solar day ahead',verbose_name='Solar Forecast')
    forecast_day_ahead_offshore = models.IntegerField(db_column='forecast wind offshore eday ahead',verbose_name='Offshore Wind Forecast')
    forecast_day_ahead_onshore = models.IntegerField(db_column='forecast wind onshore day ahead',verbose_name='Onshore Wind Forecast')
    forecast_total_load = models.IntegerField(db_column='total_load_forecast',verbose_name='Total Load Forecast')
    total_load_actual = models.FloatField(db_column='total_load_actual',verbose_name='Total Load Actual')
    price_day_ahead = models.FloatField(db_column='price day ahead',verbose_name='Day-Ahead Price')
    price_actual = models.FloatField(db_column='price actual',verbose_name='Price Actual')

    class Meta:
        db_table = 'energy_dataset'


class Date(models.Model):
    time = models.CharField(max_length=50, db_column='time',verbose_name='Date and Time')
    
    class Meta:
        db_table = 'time_stamps'


class Fossil(models.Model):
    time = models.CharField(max_length=50, db_column='time',verbose_name='Date and Time')
    brown_coal = models.IntegerField(db_column='generation fossil brown coal/lignite',verbose_name='Brown Coal')
    gas = models.IntegerField(db_column='generation fossil gas',verbose_name='Gas')
    hard_coal = models.IntegerField(db_column='generation fossil hard coal',verbose_name='Hard Coal')
    oil = models.IntegerField(db_column='generation fossil oil',verbose_name='Oil')

    class Meta:
        db_table = 'fossil_fuel_generation'


class Renewable(models.Model):
    time = models.CharField(max_length=50, db_column='time',verbose_name='Date and Time')
    geothermal = models.IntegerField(db_column='generation geothermal',verbose_name='Geothermal')
    hydro_pumped_storage = models.IntegerField(db_column='generation hydro pumped storage consumption',verbose_name='Pumped Storage Consumption')
    hydro_ror = models.IntegerField(db_column='generation hydro run-of-river and poundage',verbose_name='Run-of-River')
    hydro_water_res = models.IntegerField(db_column='generation hydro water reservoir',verbose_name='Water Reservoir')
    nuclear = models.IntegerField(db_column='generation nuclear',verbose_name='Nuclear')
    other_renewable = models.IntegerField(db_column='generation other renewable',verbose_name='Other Renewable')
    solar = models.IntegerField(db_column='generation solar',verbose_name='Solar')
    waste = models.IntegerField(db_column='generation waste',verbose_name='Waste')
    onshore = models.IntegerField(db_column='generation wind onshore',verbose_name='Onshore Wind')
    
    class Meta:
        db_table = 'renewable_fuel_generation'
