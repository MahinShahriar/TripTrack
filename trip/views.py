from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from django.urls import reverse_lazy
from .forms import CreateTripForm, CreateNoteForm

from .models import Trip, Note


class HomeView(TemplateView):
    template_name = "index.html"


def trips_list(request):
    trips = Trip.objects.filter(traveller=request.user)
    context = {
            'trips': trips,
        }
    return render(request, "trip/trip_list.html", context)


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip_list')
    form_class = CreateTripForm

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


@login_required
def create_note(request, trip_pk=None):
    trips = Trip.objects.filter(traveller=request.user) if trip_pk is None else Trip.objects.filter(traveller=request.user, id=trip_pk)

    if request.method == 'POST':
        print("FILES RECEIVED:", request.FILES)
        form = CreateNoteForm(request.POST, request.FILES)
        form.fields['trip'].queryset = trips

        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = CreateNoteForm()
        form.fields['trip'].queryset = trips

    return render(request, 'trip/note_form.html', {'form': form})



@login_required
def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    trips = Trip.objects.filter(traveller=request.user)
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = CreateNoteForm(instance=note)
        form.fields['trip'].queryset = trips  # show only user's trips

    return render(request, 'trip/note_form.html', {'form': form, 'note': note})

class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')


