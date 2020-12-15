# Generated by Django 3.1.3 on 2020-12-15 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0005_auto_20201214_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='DodatkoweInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czas_trwania', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('gatunek', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Inny'), (1, 'Horror'), (4, 'Dramat'), (3, 'Sci-Fy'), (2, 'Komedia')], null=True)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='dodatkowe',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='filmyweb.dodatkoweinfo'),
        ),
    ]