# Generated by Django 2.1.1 on 2020-08-10 13:58

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('image', models.ImageField(upload_to='uploads/home/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Bjnewsapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
                ('Name', models.CharField(default=1, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
        ),
        migrations.CreateModel(
            name='videocategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=1, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='videocategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Bjnewsapp.videocategory'),
        ),
    ]
