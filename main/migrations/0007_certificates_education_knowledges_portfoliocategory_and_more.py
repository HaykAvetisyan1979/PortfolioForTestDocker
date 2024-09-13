# Generated by Django 5.1 on 2024-08-16 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_client_funfacts_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='certificates/', verbose_name='Certificates')),
                ('certification', models.CharField(max_length=255, verbose_name='certification')),
                ('membership_id', models.CharField(max_length=255, verbose_name='Membership ID')),
                ('date', models.DateField(verbose_name='Certification Date')),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Graduation Year')),
                ('institution', models.CharField(max_length=255, verbose_name='institution')),
                ('specialization', models.CharField(max_length=255, verbose_name='specialization')),
                ('about', models.TextField(verbose_name='About(skills and etc.)')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='Knowledges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge', models.CharField(max_length=255, verbose_name='Knowledge')),
            ],
            options={
                'verbose_name': 'Knowledge',
                'verbose_name_plural': 'Knowledges',
            },
        ),
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Portfolio Category')),
            ],
            options={
                'verbose_name': 'Portfolio Category',
                'verbose_name_plural': 'Portfolio Categories',
            },
        ),
        migrations.CreateModel(
            name='SkillType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Skill Type(Coding, Design and etc.)')),
            ],
            options={
                'verbose_name': 'Skill Type',
                'verbose_name_plural': 'Skill Types',
            },
        ),
        migrations.CreateModel(
            name='WorkingExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.DateField(verbose_name='Start Year')),
                ('end_year', models.DateField(verbose_name='End Year')),
                ('company', models.CharField(max_length=255, verbose_name='Company')),
                ('role', models.CharField(max_length=255, verbose_name='Role')),
                ('text', models.TextField(verbose_name='About company and your role in it.')),
            ],
            options={
                'verbose_name': 'Working Experience',
                'verbose_name_plural': 'Working Experience',
            },
        ),
        migrations.AlterModelOptions(
            name='funfacts',
            options={'verbose_name': 'Fun Fact', 'verbose_name_plural': 'Fun Facts'},
        ),
        migrations.CreateModel(
            name='PortfolioItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('media', models.FileField(upload_to='portfolioItems/', verbose_name='Media file, or full size file')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_categ', to='main.portfoliocategory')),
            ],
            options={
                'verbose_name': 'Portfolio Item',
                'verbose_name_plural': 'Portfolio Items',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255, verbose_name='Skill')),
                ('level', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Level With Percentage')),
                ('skill_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sk_type', to='main.skilltype')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
    ]