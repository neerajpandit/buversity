from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('paper/',views.PaperView.as_view(),name='paper'),
    path('notes/',views.NotesView.as_view(),name='notes'),
    path('syllabus/',views.SyllabusView.as_view(),name='syllabus'),
    path('timetable/',views.TimetableView.as_view(),name='timetable'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
