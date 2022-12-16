from django.contrib import admin
from .models import Semester,Syllabus,Timetable,Branch,Notes,Paper
# Register your models here.
@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display=['sem']

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display=['branch']

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display=['branch','sem','year','paper_name','paper_pdf']

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display=['branch','sem','notes_name','notes_pdf']

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display=['branch','sem','syllabus_pdf']

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display=['branch','sem','timetable_pdf']