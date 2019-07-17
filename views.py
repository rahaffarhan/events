from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from .forms import EventUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
import json
from .models import Event, Club, EventRegistration
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import (
        DeleteView,
        UpdateView,
        CreateView,
        FormView,
)
from django.views.generic. detail import DetailView




def home(request):
    events = Event.objects.all()
    return render(request, 'events_attendance/home.html', {'events': events})


class EventListView(ListView):
    model = Event
    ordering = ['-event_date']
    template_name = 'events_attendance/event_list.html'
    context_object_name = 'event_list'
    paginate_by = 3

    def get_queryset(self):
        return Event.objects.all()


class UserEventListView(ListView, User):
    model = Event
    template_name = 'events_attendance/user_event_list.html'
    context_object_name = 'event_list'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Event.objects.filter(author=user).order_by('-event_date')


class EventDetailView(DetailView):
    model = Event
    template_name = 'events_attendance/event_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@login_required
def list_registration(request):
    registrations = EventRegistration.objects.filter(deleted=False, user=request.user)
    return render(request, 'events_attendance/list_registration.html', {'registrations': registrations})

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['event_name', 'event_date', 'content']
    queryset = Event.objects.all()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    exclude = ('author',)
    fields = ['event_name', 'event_date', 'content']
    template_name = 'events_attendance/event_update_form.html'
    success_url = reverse_lazy('events_attendance:events')

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events_attendance/event_confirm_delete.html'
    success_url = reverse_lazy('events_attendance:events')

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False


def club_events(request):
    model = Club
    return render(request, 'events_attendance/index.html', {'events': model})



