# Generated by Django 2.2.2 on 2019-06-10 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tunr_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('episode_number', models.IntegerField(max_length=4)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=250)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='tunr_app.Episode')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='tunr_app.Season'),
        ),
    ]
