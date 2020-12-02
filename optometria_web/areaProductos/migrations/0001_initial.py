# Generated by Django 3.1.3 on 2020-11-24 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armazon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armazon', models.CharField(max_length=2)),
                ('precio', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areaProductos.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Estado_del_pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Forma_de_pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lado', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.PositiveIntegerField()),
                ('detalle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='areaProductos.detalle_producto')),
                ('lado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='areaProductos.lado')),
            ],
        ),
        migrations.CreateModel(
            name='Nombre_producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_de_pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.DateTimeField()),
                ('asistencia', models.BooleanField(blank=True, null=True)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areaProductos.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='areaProductos.nombre_producto')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armazon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='areaProductos.armazon')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areaProductos.paciente')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areaProductos.estado_del_pedido')),
                ('forma_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areaProductos.forma_de_pago')),
                ('lente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='areaProductos.lente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areaProductos.producto')),
                ('tipo_de_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areaProductos.tipo_de_pedido')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areaProductos.empleado')),
            ],
        ),
    ]
