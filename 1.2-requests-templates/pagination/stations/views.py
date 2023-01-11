from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus = None
    with open(BUS_STATION_CSV, encoding='UTF-8') as f:
        bus = list(csv.DictReader(f))

    current_page = int(request.GET['page'])

    page = dict()
    page['number'] = current_page

    if current_page == 1:
        page['has_previous'] = False
    else:
        page['has_previous'] = True
        page['previous_page_number'] = current_page - 1

    if current_page * 10 >= len(bus):
        page['has_next'] = False
    else:
        page['next_page_number'] = current_page + 1
        page['has_next'] = True



    context = {
         'bus_stations': bus[current_page*10-10:current_page*10],
         'page': page
    }
    return render(request, 'stations/index.html', context)
