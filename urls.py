from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'events_attendance'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^events/$', views.EventListView.as_view(), name='events'),
    url(r'^user/$', views.UserEventListView.as_view(), name='user-events'),
    url(r'^(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='event-detail'),
    url(r'^events/new/$', views.EventCreateView.as_view(), name='new-event'),
    url(r'^(?P<pk>\d+)/update/$', views.EventUpdateView.as_view(), name='update-event'),
    url(r'^(?P<pk>\d+)/delete/$', views.EventDeleteView.as_view(), name='delete-event'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
