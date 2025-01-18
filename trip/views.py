from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Trip, Note


class HomeView(TemplateView):
    template_name = "index.html"


def trips_list(request):
    trips = Trip.objects.filter(traveller=request.user)
    context = {
            'trips': trips,
        }

    # except:
    #     context = {
    #         'error': "You haven't any Trip."
    #     }

    return render(request, "trip/trip_list.html", context)


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'trip/signup.html'


class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip_list')
    fields = ['city', 'country', 'start_date', 'end_date']

    def form_valid(self, form):
        form.instance.traveller = self.request.user
        return super().form_valid(form)


class TripDetailView(DetailView):
    model = Trip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes

        return context


class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip_list')


class NoteDetailView(DetailView):
    model = Note


class NoteListView(ListView):
    model = Note

    def get_queryset(self):
        queryset = Note.objects.filter(trip__traveller=self.request.user)
        return queryset



class CreateNoteView(CreateView):
    model = Note
    success_url = reverse_lazy('note_list')
    fields = ['trip', 'title', 'description', 'type', 'img', ]

    def get_form(self):
        form = super(CreateNoteView, self).get_form()
        trips = Trip.objects.filter(traveller=self.request.user)
        form.fields['trip'].queryset = trips

        return form

class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy('note_list')
    fields = ['trip', 'title', 'description', 'type', 'img', ]

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(traveller=self.request.user)
        form.fields['trip'].queryset = trips

        return form

class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')


