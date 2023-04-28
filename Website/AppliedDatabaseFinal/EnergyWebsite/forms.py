from django import forms
   

TIME_FREQ = (
    ('#1', '1H'),
    ('#2', '1D'),
    ('#3', '1W'),
    ('#4', '1M')
)
LOAD_TYPE = (
    ('Biomass'),
    ('Brown Coal'),
    ('Coal-Derived Gas'),
    ('Gas'),
    ('Hard Coal'),
    ('Oil'),
    ('Oil Shale'),
    ('Peat'),
    ('Geothermal'),
    ('Pumped Storage Consumption'),
    ('Run-of-River'),
    ('Water Reservoir'),
    ('Marine'),
    ('Nuclear'),
    ('Other Renewable'),
    ('Solar'),
    ('Waste'),
    ('Offshore Wind'),
    ('Onshore Wind'),
    ('Solar Forecast'),
    ('Offshore Wind Forecast'),
    ('Onshore Wind Forecast'),
    ('Total Load Forecast'),
    ('Total Load Actual'),
    ('Day-Ahead Price'),
    ('Price Actual')
)


class Filters(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time_frequency = forms.ChoiceField(choices=TIME_FREQ)
    load = forms.ChoiceField(choices=LOAD_TYPE)