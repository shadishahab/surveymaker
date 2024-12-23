# Generated by Django 5.1.2 on 2024-10-14 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptiveQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('is_required', models.BooleanField(default=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='surveys.survey')),
            ],
            options={
                'verbose_name': 'Descriptive Question',
                'verbose_name_plural': 'Descriptive Questions',
            },
        ),
        migrations.CreateModel(
            name='MatrixQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('is_required', models.BooleanField(default=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='surveys.survey')),
            ],
            options={
                'verbose_name': 'Matrix Question',
                'verbose_name_plural': 'Matrix Questions',
            },
        ),
        migrations.CreateModel(
            name='MatrixColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_text', models.CharField(max_length=255)),
                ('order', models.PositiveSmallIntegerField()),
                ('matrix_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='questions.matrixquestion')),
            ],
            options={
                'verbose_name': 'Matrix Column',
                'verbose_name_plural': 'Matrix Columns',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MatrixRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_text', models.CharField(max_length=255)),
                ('order', models.PositiveSmallIntegerField()),
                ('matrix_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='questions.matrixquestion')),
            ],
            options={
                'verbose_name': 'Matrix Row',
                'verbose_name_plural': 'Matrix Rows',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('is_required', models.BooleanField(default=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='surveys.survey')),
            ],
            options={
                'verbose_name': 'Multiple Choice Question',
                'verbose_name_plural': 'Multiple Choice Questions',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('order', models.PositiveSmallIntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='questions.multiplechoicequestion')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='NumericQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('is_required', models.BooleanField(default=True)),
                ('min_value', models.IntegerField()),
                ('max_value', models.IntegerField()),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='surveys.survey')),
            ],
            options={
                'verbose_name': 'Numeric Question',
                'verbose_name_plural': 'Numeric Questions',
            },
        ),
    ]
