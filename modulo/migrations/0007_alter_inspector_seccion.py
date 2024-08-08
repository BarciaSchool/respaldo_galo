# Generated by Django 5.0 on 2024-01-29 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0006_inspector_activo_alter_inspector_seccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspector',
            name='seccion',
            field=models.CharField(choices=[('', 'Seleccione una Sección'), ('INICIAL', 'INICIAL'), ('BASICA', 'BASICA'), ('BASICA ELEMENTAL', 'BASICA ELEMENTAL'), ('BASICA SUPERIOR', 'BASICA SUPERIOR'), ('BACHILLERATO', 'BACHILLERATO')], default='Ninguna', max_length=50),
        ),
    ]