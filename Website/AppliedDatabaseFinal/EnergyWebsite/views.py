from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import Filters
from .models import EnergyDataset
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from django.template import loader
from django.contrib import messages
from django.db import connections
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from plotly.offline import plot
from plotly.graph_objs import Scatter
import numpy as np
from datetime import datetime

# @require_http_methods(['GET','POST'])
# def home(request):
#     """
#     View for the home page of the Django application.
#     """
#     if request.method == 'POST':
#         form = Filters(request.POST)
#         if form.is_valid():
#             start_dt = form.cleaned_data.get('start_date')
#             end_dt = form.cleaned_data.get('end_date')
#             time_freq = form.cleaned_data.get('time_frequency')
#             load = form.cleaned_data.get('load')
#             data = process_filters(start_dt,end_dt,time_freq,load)
#             fig, ax = plt.subplots()
#             ax.plot(data)
#             buffer = io.BytesIO()
#             plt.savefig(buffer, format='png')
#             buffer.seek(0)
#             response = HttpResponse(buffer, content_type='image/png')
#             response['Content-Disposition'] = 'attachment; filename="graph.png"'
#             return response
#     else:
#         form = Filters()
#     return render(request, 'home.html', {'form': form})
        
    # filters = Filters(request.POST or None)
    # context = {
    #     'filters': filters
    # }

    # response = matplotlib_graph(context)

    # return render(request, 'home.html', context, response)

def about(request):
    """
    View for the about page of the Django application.
    """
    return render(request, 'about.html')

def home(request):
    y_axis = request.GET.get('y-axis', 'total_load_actual')
    print('y_axis:', y_axis)
    energy_query = EnergyDataset.objects.all().using('renewables')
    energy_df = pd.DataFrame.from_records(energy_query.values())
    data = datetime_transform(energy_df)

    # time_values = np.array(list(data.values_list('time', flat=True)))
    time_values = pd.Series(list(EnergyDataset.objects.using('renewables').values_list('time', flat=True)))
    y_axis_values = pd.Series(list(EnergyDataset.objects.using('renewables').values_list(y_axis, flat=True)))
    #total_load = pd.Series(list(EnergyDataset.objects.using('renewables').values_list('total_load_actual', flat=True)))

    plot_div = plot([Scatter(x=time_values, y=y_axis_values,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='forestgreen')],
               output_type='div')
    return render(request, "home.html", context={'plot_div': plot_div})


# def process_filters(start_dt, end_dt, time_freq, load):
#     energy_query = EnergyDataset.objects.all().using('renewables')
#     energy_df = pd.DataFrame.from_records(energy_query.values())
#     graph_df = datetime_transform(energy_df)
#     start_date = timezone.make_aware(start_dt.time, timezone.utc)
#     end_date = timezone.make_aware(end_dt.time, timezone.utc)
#     df_filtered = graph_df.loc[start_dt.time:end_dt.time]
    
#     return df_filtered
#     # df_filtered[load].resample(time_freq).mean().plot()
#     # plt.title(load)

    

def datetime_transform(df):
    df['time'] = pd.to_datetime(df['time'], utc=True)
    df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['time'] = pd.to_datetime(df['time'], utc=False)
    df = df.set_index('time', drop=True)
    return df

# def plot_data(plot_df,start_date, end_date, time_freq, column):
#     #filter dataframe to only show data between the start and end date
#     start_date = timezone.make_aware(start_date.time, timezone.utc)
#     end_date = timezone.make_aware(end_date.time, timezone.utc)
#     df_filtered = plot_df.loc[start_date.time:end_date.time]
    
#     #plot the data
#     df_filtered[column].resample(time_freq).mean().plot()
#     plt.title(column)


# def matplotlib_graph(request):
#     # Generate the graph using Matplotlib
#     energy_query = EnergyDataset.objects.all().using('renewables')
#     energy_df = pd.DataFrame.from_records(energy_query.values())
#     graph_df = datetime_transform(energy_df)
#     filter_form = Filters(request.POST or None)

#     if request.method == 'POST':
#         start_date = request.POST.get('start_date')
#         end_date = request.POST.get('end_date')
#         time_freq = request.POST.get('time_frequency')
#         column = request.POST.get('load')

#         plot_data(graph_df,start_date,end_date,time_freq,column)

#     else:
#         cursor = connections['renewables'].cursor()
#         cursor.execute('SELECT time  FROM energy_dataset LIMIT 1')
#         time_data = cursor.fetchall()
#         start_date = EnergyDataset.objects.using('renewables').order_by('time').first()
#         end_date = EnergyDataset.objects.using('renewables').latest('time')
#         time_freq = '#3'
#         column = 'Total Load Actual'

#         plot_data(graph_df,start_date,end_date,time_freq,column)
#             # messages.warning(request, "No data selected")

#     # Save the graph to a buffer
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
#     buf.seek(0)
#     plt.close()

#     # Convert the buffer to a base64 encoded string
#     graph_data = base64.b64encode(buf.read()).decode('utf-8')

#     # Render the HTML page with the graph embedded
#     context = {'graph_data': graph_data}
#     html = loader.render_to_string('matplotlib_graph.html', context)
#     return HttpResponse(html)

# def energy_plot(request):
#     # Get start and end times from request parameters
#     start_time = request.GET.get('start_time')
#     end_time = request.GET.get('end_time')

#     # Get energy type from request parameters
#     energy_type = request.GET.get('total_load_forcast')

#     # Filter energy dataset based on start time, end time, and energy type
#     energy_data = EnergyDataset.objects.using('renewables').filter(
#         timestamp__range=[start_time, end_time],
#         total_load_actual=energy_type
#     )

#     # Extract x and y values from filtered dataset
#     x_values = [data.time for data in energy_data]
#     y_values = [data.time for data in energy_data]

#     # Create plot
#     fig, ax = plt.subplots()
#     ax.plot(x_values, y_values)

#     # Set plot title and axis labels
#     ax.set_title('Energy Data')
#     ax.set_xlabel('Time')
#     ax.set_ylabel('Energy Value')

#     # Convert plot to HTML and return as response
#     html = fig_to_html(fig)
#     return render(request, 'energy_plot.html', {'plot': html})