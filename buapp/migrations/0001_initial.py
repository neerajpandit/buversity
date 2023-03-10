# Generated by Django 4.1.3 on 2022-12-15 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timetable_pdf', models.FileField(default=None, null=True, upload_to='AllPdf/Timetable/')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buapp.branch')),
                ('sem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buapp.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_pdf', models.FileField(default=None, null=True, upload_to='AllPdf/Syllabus/')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buapp.branch')),
                ('sem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buapp.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_name', models.CharField(max_length=20, null=True)),
                ('paper_pdf', models.FileField(default=None, null=True, upload_to='AllPdf/Paper/')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buapp.branch')),
                ('sem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buapp.semester')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buapp.year')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes_name', models.CharField(max_length=20, null=True)),
                ('notes_pdf', models.FileField(default=None, null=True, upload_to='AllPdf/Notes/')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buapp.branch')),
                ('sem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buapp.semester')),
            ],
        ),
    ]
