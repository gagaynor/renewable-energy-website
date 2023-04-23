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

def home(request):
    """
    View for the home page of the Django application.
    """

    return render(request, 'home.html')

def about(request):
    """
    View for the about page of the Django application.
    """
    filters = Filters(request.POST or None)
    context = {
        'filters': filters
    }

    response = matplotlib_graph(request)

    return render(request, 'about.html', context, response)


def datetime_transform(df):
    df['time'] = pd.to_datetime(df['time'], utc=True)
    df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['time'] = pd.to_datetime(df['time'], utc=False)
    df = df.set_index('time', drop=True)
    return df

def plot_data(plot_df,start_date, end_date, time_freq, column):
    #filter dataframe to only show data between the start and end date
    df_filtered = plot_df.loc[start_date:end_date]
    
    #plot the data
    df_filtered[column].resample(time_freq).mean().plot()
    plt.title(column)

    
def matplotlib_graph(request):
    # Generate the graph using Matplotlib
    energy_query = EnergyDataset.objects.all()
    energy_df = pd.DataFrame.from_records(energy_query.values())
    graph_df = datetime_transform(energy_df)
    filter_form = Filters(request.POST or None)

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        time_freq = request.POST.get('time_frequency')
        column = request.POST.get('load')

        plot_data(graph_df,start_date,end_date,time_freq,column)

    else:
            messages.warning(request, "No data selected")

    # Save the graph to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Convert the buffer to a base64 encoded string
    graph_data = base64.b64encode(buf.read()).decode('utf-8')

    # Render the HTML page with the graph embedded
    context = {'graph_data': graph_data}
    html = loader.render_to_string('matplotlib_graph.html', context)
    return HttpResponse(html)
