#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def sum(sumando1, sumando2):
    return sumando1 + sumando2


def rest(sumando1, sumando2):
    return sumando1 - sumando2


def mult(sumando1, sumando2):
    return sumando1 * sumando2


def div(sumando1, sumando2):
    try:
        return sumando1 / sumando2
    except ZeroDivisionError:
        sys.exit("Error: No se puede dividir entre 0")


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("Error: python calculadora.py función operando1 operando2")

    primero = float(sys.argv[2])
    segundo = float(sys.argv[3])

    if sys.argv[1] == "sum":
        print sum(primero, segundo)
    elif sys.argv[1] == "rest":
        print rest(primero, segundo)
    elif sys.argv[1] == "mult":
        print mult(primero, segundo)
    elif sys.argv[1] == "div":
        print div(primero, segundo)
    else:
        print("Error: operandos: sum-rest-mult-div.")
