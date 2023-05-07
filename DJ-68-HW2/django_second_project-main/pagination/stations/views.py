from csv import DictReader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

import pagination.settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(pagination.settings.BUS_STATION_CSV, mode="r", encoding="utf8") as f:
        reader = list(DictReader(f))

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(reader, 10)
    page = paginator.get_page(page_number)
    print(page)
    context = {
                "page": page,
                "bus_stations": page.object_list,
              }
    return render(request, 'stations/index.html', context)
