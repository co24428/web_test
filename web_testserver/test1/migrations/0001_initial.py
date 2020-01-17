# Generated by Django 3.0.2 on 2020-01-17 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=70)),
                ('thumbnail', models.BinaryField(null=True)),
                ('report', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='cctv_data',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('big_addr', models.CharField(max_length=30)),
                ('small_addr', models.CharField(max_length=30)),
                ('cctv_yn', models.CharField(max_length=5)),
                ('cctv_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('user_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('home', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='favorite',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('region_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.cctv_data')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.user_table')),
            ],
        ),
        migrations.CreateModel(
            name='article_scrap',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('scrap_date', models.DateField()),
                ('article_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.article')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.user_table')),
            ],
        ),
    ]
