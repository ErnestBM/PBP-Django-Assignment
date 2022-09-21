from django.urls import path
from django.conf.urls import include
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_json
from mywatchlist.views import show_json_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]