from django.shortcuts import render
from django.views.generic import ListView
from .models import Branch,Semester,Paper,Notes,Syllabus,Timetable

# Create your views here.

class HomeView(ListView):
    def get(self,request):
        return render(request,'buapp/index.html')

class PaperView(ListView):
    def get(self,request):
        branch=self.request.GET.get('branch')
        sem=self.request.GET.get('sem')
        year=self.request.GET.get('year')
        result=Paper.objects.filter(
            sem__sem=sem,
            branch__branch=branch,
            year=year
        )

        opsem=Semester.objects.all()
        opbranch=Branch.objects.all()
        opyear=Paper.objects.all()
        return render(request,'buapp/paper.html',{'opsem':opsem,'opbranch':opbranch,'opyear':opyear,'result':result})

class NotesView(ListView):
    def get(self,request):
        branch=self.request.GET.get('branch')
        sem=self.request.GET.get('sem')
        notesresult=Notes.objects.filter(
            sem__sem=sem,
            branch__branch=branch
        )
        opsem=Semester.objects.all()
        opbranch=Branch.objects.all()
        return render(request,'buapp/notes.html',{'notesresult':notesresult,'opsem':opsem,'opbranch':opbranch})

class SyllabusView(ListView):
    def get(self,request):
        branch=self.request.GET.get('branch')
        sem=self.request.GET.get('sem')
        syllabusresult=Syllabus.objects.filter(
            sem__sem=sem,
            branch__branch=branch
        )
        opsem=Semester.objects.all()
        opbranch=Branch.objects.all()
        return render(request,'buapp/syllabus.html',{'syllabusresult':syllabusresult,'opsem':opsem,'opbranch':opbranch})

class TimetableView(ListView):
    def get(self,request):
        branch=self.request.GET.get('branch')
        sem=self.request.GET.get('sem')
        timetableresult=Timetable.objects.filter(
            sem__sem=sem,
            branch__branch=branch
        )
        opsem=Semester.objects.all()
        opbranch=Branch.objects.all()
        return render(request,'buapp/timetable.html',{'timetableresult':timetableresult,'opsem':opsem,'opbranch':opbranch})
 