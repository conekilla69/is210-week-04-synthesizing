#!/usr.bin/env pythin
# -*- coding: utf-8 -*-
"Temperature conversions"""

import decimal

ABSOLUTE_DIFFERENCE = (273.15)


def fahrenheit_to_celsius(degrees):
    """fahrenheit to celsius conversion

    Args:
    degee (int): Arg to be converted from fahrenheit to celsius.

    Return:
    int: Value expressed in three decimal places.

    Examples:
    >>> fahrenheit_to_celsius(212)
    '100.000'
    >>> fahrenheit_to_celsius(300)
    '148.889'
    >>> fahrenheit_to_celsius(O)
    fahrenheit_to_celsius(20)
    '-6.667'
    """
    degrees = decimal.Decimal((degrees-32) * 5)/9
    return '{0:4.3f}'.format(degrees)


def celsius_to_kelvin(degrees):
    """Celsius to Kelvin conversion

    Args:
    degree (int): Arg to be converted from celsius to Kelvin.

    Return:
    int : Value to be expressed in two decimal places.

    Examples:
    >>> celsius_to_kelvin(100)
    '373.15'
    >>> celsius_to_kelvin(-20)
    '253.15'
    """
    degrees = (degrees + ABSOLUTE_DIFFERENCE)
    return'{0:4.2f}'.format(degrees)


def fahrenheit_to_kelvin(degrees):
    """Fahrenheit conversion to Kelvin.

    Args:
    degree (int): Arg to be converted from fahrenheit to Kelvin.

    Return:
    int : Arg to give a value converted from fahrenheit to Kelvin.

    Examples:
    >>> fahrenheit_to_kelvin(212)
    '373.15'
    >>> fahrenheit_to_kelvin(100)
    '310.93'
    >>> fahrenheit_to_kelvin(-20)
    '244.26'
    """
    degrees = ((degrees + 459.67) * 5/9)
    return '{0:4.2f}'.format(degrees)
