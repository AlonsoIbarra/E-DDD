# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, to='compras.Entity', parent_link=True)),
                ('idCarrito', models.AutoField(primary_key=True, serialize=False)),
                ('idCliente', models.IntegerField()),
                ('listaProductos', models.TextField()),
                ('fechaCarrito', models.DateField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            bases=('compras.entity',),
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, to='compras.Entity', parent_link=True)),
                ('idOrdenCompra', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCompra', models.DateField(auto_now_add=True)),
                ('idCliente', models.IntegerField()),
                ('listaProductosOrden', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Pagada'), (1, 'Pendiente'), (2, 'Cancelada')])),
            ],
            bases=('compras.entity',),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, to='compras.Entity', parent_link=True)),
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.CharField(null=True, max_length=255)),
            ],
            bases=('compras.entity',),
        ),
    ]
