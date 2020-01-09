# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def fill_customers_info(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')
    Order = apps.get_model('orders', 'Order')

    for order in Order.objects.all():
        if order.sender and order.sender_phone:
            customer, _c = Customer.objects.get_or_create(
                name=order.sender,
                phone=order.sender_phone
            )

            customer.email = order.sender_email
            customer.address = order.sender_address
            customer.save(update_fields=['email', 'address'])

        if order.receiver and order.receiver_phone:
            customer, _c = Customer.objects.get_or_create(
                name=order.receiver,
                phone=order.receiver_phone
            )

            customer.email = order.receiver_email
            customer.address = order.receiver_address
            customer.save(update_fields=['email', 'address'])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0001_initial'),
        ('orders', '0002_order_payment'),
    ]

    operations = [
        migrations.RunPython(fill_customers_info, reverse_code=noop)
    ]
