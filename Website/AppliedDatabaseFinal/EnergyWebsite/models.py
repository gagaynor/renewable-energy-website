from django.db import models

class EnergyDataset(models.Model):
    time = models.TextField(primary_key=True, blank=True, null=False)
    generation_biomass = models.FloatField(db_column='generation biomass', blank=True, null=True)  
    generation_fossil_brown_coal_lignite = models.FloatField(db_column='generation fossil brown coal/lignite', blank=True, null=True)  
    generation_fossil_coal_derived_gas = models.FloatField(db_column='generation fossil coal-derived gas', blank=True, null=True)  
    generation_fossil_gas = models.FloatField(db_column='generation fossil gas', blank=True, null=True)  
    generation_fossil_hard_coal = models.FloatField(db_column='generation fossil hard coal', blank=True, null=True)  
    generation_fossil_oil = models.FloatField(db_column='generation fossil oil', blank=True, null=True)  
    generation_fossil_oil_shale = models.FloatField(db_column='generation fossil oil shale', blank=True, null=True)  
    generation_fossil_peat = models.FloatField(db_column='generation fossil peat', blank=True, null=True)  
    generation_geothermal = models.FloatField(db_column='generation geothermal', blank=True, null=True)  
    generation_hydro_pumped_storage_aggregated = models.FloatField(db_column='generation hydro pumped storage aggregated', blank=True, null=True)  
    generation_hydro_pumped_storage_consumption = models.FloatField(db_column='generation hydro pumped storage consumption', blank=True, null=True)  
    generation_hydro_run_of_river_and_poundage = models.FloatField(db_column='generation hydro run-of-river and poundage', blank=True, null=True)  
    generation_hydro_water_reservoir = models.FloatField(db_column='generation hydro water reservoir', blank=True, null=True)  
    generation_marine = models.FloatField(db_column='generation marine', blank=True, null=True)  
    generation_nuclear = models.FloatField(db_column='generation nuclear', blank=True, null=True)  
    generation_other = models.FloatField(db_column='generation other', blank=True, null=True)  
    generation_other_renewable = models.FloatField(db_column='generation other renewable', blank=True, null=True)  
    generation_solar = models.FloatField(db_column='generation solar', blank=True, null=True)  
    generation_waste = models.FloatField(db_column='generation waste', blank=True, null=True)  
    generation_wind_offshore = models.FloatField(db_column='generation wind offshore', blank=True, null=True)  
    generation_wind_onshore = models.FloatField(db_column='generation wind onshore', blank=True, null=True)  
    forecast_solar_day_ahead = models.IntegerField(db_column='forecast solar day ahead', blank=True, null=True)  
    forecast_wind_offshore_eday_ahead = models.FloatField(db_column='forecast wind offshore eday ahead', blank=True, null=True)  
    forecast_wind_onshore_day_ahead = models.IntegerField(db_column='forecast wind onshore day ahead', blank=True, null=True)  
    total_load_forecast = models.IntegerField(blank=True, null=True)
    total_load_actual = models.FloatField(blank=True, null=True)
    price_day_ahead = models.FloatField(db_column='price day ahead', blank=True, null=True)  
    price_actual = models.FloatField(db_column='price actual', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'energy_dataset'


class FossilFuelGeneration(models.Model):
    time = models.TextField(db_column='TIME', blank=True, null=True)
    gen_brown_coal_lignite = models.FloatField(db_column='GEN_BROWN_COAL_LIGNITE', blank=True, null=True)  
    gen_gas = models.FloatField(db_column='GEN_GAS', blank=True, null=True)  
    gen_hard_coal = models.FloatField(db_column='GEN_HARD_COAL', blank=True, null=True)
    gen_oil = models.FloatField(db_column='GEN_OIL', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'fossil_fuel_generation'


class Load(models.Model):
    row_key = models.IntegerField(blank=True, null=True)
    time = models.TextField(primary_key=True, blank=True, null=False)
    forcasted_load = models.IntegerField(blank=True, null=True)
    actual_load = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load'


class TimeStamps(models.Model):
    row = models.AutoField(primary_key=True, blank=True, null=False)
    time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_stamps'