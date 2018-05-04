# Generated by Django 2.0.3 on 2018-05-04 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emisora', '0003_category_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='ctg_created_by',
            field=models.CharField(editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='ctg_created_date',
            field=models.DateTimeField(editable=False, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='category',
            name='ctg_modified_by',
            field=models.CharField(editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='ctg_modified_date',
            field=models.DateTimeField(editable=False, verbose_name='Editado'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sct_created_by',
            field=models.CharField(editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sct_created_date',
            field=models.DateTimeField(editable=False, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sct_modified_by',
            field=models.CharField(editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sct_modified_date',
            field=models.DateTimeField(editable=False, verbose_name='Editado'),
        ),
        migrations.AlterField(
            model_name='user',
            name='usr_created_by',
            field=models.CharField(editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='usr_created_date',
            field=models.DateTimeField(editable=False, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='user',
            name='usr_modified_by',
            field=models.CharField(editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='usr_modified_date',
            field=models.DateTimeField(editable=False, verbose_name='Editado'),
        ),
    ]
