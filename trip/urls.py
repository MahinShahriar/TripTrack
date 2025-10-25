from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
        path('', views.HomeView.as_view(), name='home'),
        path('trips', views.trips_list, name='trip_list'),
        path('create_trip', views.TripCreateView.as_view(), name='trip_form'),
        path('trip/<int:pk>', views.TripDetailView.as_view(), name='trip_detail'),
        path('trip/delete/<int:pk>', views.TripDeleteView.as_view(), name='trip_delete'),

        path('notes', views.NoteListView.as_view(), name='note_list'),
        path('create_note/', views.create_note, name='note_form'),
        path('create_note/<int:trip_pk>/', views.create_note, name='note_form_trip'),
        path('trip/note/<int:pk>', views.NoteDetailView.as_view(), name='note_detail'),
        path('note/update/<int:pk>', views.update_note, name='note_update'),
        path('note/delete/<int:pk>', views.NoteDeleteView.as_view(), name='note_delete'),

]