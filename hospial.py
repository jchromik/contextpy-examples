#!/usr/bin/python2

from contextpy import (
    base, around, before, after, activelayer, activelayers, layer, proceed)
from sys import argv

import json

diagnosis_layer = layer("Diagnosis")
medication_layer = layer("Medication")

class Patient:
    def __init__(self, name, ward, diagnosis, medication):
        self.name = name
        self.ward = ward
        self.diagnosis = diagnosis
        self.medication = medication

    @base
    def __str__(self):
        return "\n" + self.name + "\n\t Ward: " + self.ward + "\n"

    @around(diagnosis_layer)
    def __str__(self):
        return proceed() + "\t Diagnosis: " + self.diagnosis + "\n"

    @around(medication_layer)
    def __str__(self):
        return proceed() + "\t Medication: " + self.medication + "\n"


class Hospital:
    role_layers = {
        'receptionist' : [],
        'pharmacist' : [medication_layer],
        'health_department' : [diagnosis_layer],
        'medic' : [diagnosis_layer, medication_layer]}

    def __init__(self):
        self.patients = [
            Patient("Max Mustermann", "Oncology", "Lung Cancer", "Blubserizin"),
            Patient("Jane Doe", "Traumatology", "Broken Ulna Bone", "Heparin"),
            Patient("Hulk", "Psychiatry", "Hypochondriasis", "Placebo")]

    def layers(self, role):
        return self.__class__.role_layers[role]

    def roles(self):
        return self.__class__.role_layers.keys()

    def print_patients_as(self, role):
        with activelayers(*self.layers(role)):
            self.print_patients()

    @base
    def print_patients(self):
        for patient in self.patients:
            print patient

    @before(diagnosis_layer)
    def print_patients(self, *args, **kwargs):
        print "Printing patients with diagnosis."
    
    @before(medication_layer)
    def print_patients(self, *args, **kwargs):
        print "Printing patients with medication."

    @after(diagnosis_layer)
    def print_patients(self, *args, **kwargs):
        print "Printed patients with diagnosis."
    
    @after(medication_layer)
    def print_patients(self, *args, **kwargs):
        print "Printed patients with medication."


hospital = Hospital()

def print_usage():
    print "Usage: " + argv[0] + " ROLE \n"
    print "Where ROLE can be: "
    print "\n".join([" * " + key for key in hospital.roles()])

if len(argv) == 1 or argv[1] not in hospital.roles():
    print_usage()
    exit()

hospital.print_patients_as(argv[1])