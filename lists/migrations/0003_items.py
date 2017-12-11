# Generated by Django 2.0 on 2017-12-10 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20171210_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('store', models.TextField(blank=True, max_length=50, null=True)),
                ('url', models.TextField(blank=True, max_length=150, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.WishList')),
            ],
        ),
    ]
