# Generated by Django 4.1.3 on 2022-12-15 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='syllabus',
            old_name='paper_pdf',
            new_name='syllabus_pdf',
        ),
    ]
