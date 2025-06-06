# Generated by Django 5.2 on 2025-04-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarboneRender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_file', models.FileField(upload_to='templates/')),
                ('json_file', models.FileField(upload_to='json/')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='pdf/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
