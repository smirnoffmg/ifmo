# -*- coding: utf-8 -*-
import phonenumbers


def formatted_phone(phone_number):
    parsed = phonenumbers.parse(phone_number, 'RU')
    return phonenumbers.format_number(
        parsed,
        phonenumbers.PhoneNumberFormat.NATIONAL)
