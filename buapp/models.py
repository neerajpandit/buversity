from django.db import models

# Create your models here.
class Semester(models.Model):
    sem=models.CharField(max_length=1,null=True)
    def __str__ (self):
        return self.sem

class Branch(models.Model):
    branch=models.CharField(max_length=15,null=True)
    def __str__ (self):
        return self.branch

# class Year(models.Model):
#     year=models.CharField(max_length=4,null=True)
#     def __str__ (self):
#         return self.year

class Paper(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    sem=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    year=models.CharField(max_length=4,null=True)
    paper_name=models.CharField(max_length=20,null=True)
    paper_pdf=models.FileField(upload_to="AllPdf/Paper/",null=True,default=None)

class Notes(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    sem=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    notes_name=models.CharField(max_length=20,null=True)
    notes_pdf=models.FileField(upload_to="AllPdf/Notes/",null=True,default=None)

class Timetable(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    sem=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    timetable_pdf=models.FileField(upload_to="AllPdf/Timetable/",null=True,default=None)

class Syllabus(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    sem=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    syllabus_pdf=models.FileField(upload_to="AllPdf/Syllabus/",null=True,default=None)
