#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:41:53 2020

@author: eddieguo
"""

import pandas as pd
import numpy as np


def get_clinical_data(csv_clinical):
    """Description: returns patient data as a dictionary and a set of patient
    IDs that don't have data in Overall Survival (Months) and Overall Survival
    Status.

    Arguments:
        csv_clinical (pandas object): the data object to read.
    Returns:
        patient_data (dict): key = Sample ID, values = [Overall Survival
            Status (Months), Overall Survival Status]
        null_patients (set): all the sample IDs which have no data for Overall
            Survival Status (Months) or Overal Survival Statuts.
    """
    patient_data = dict()
    null_patients = set()

    i = 0
    while i < len(csv_clinical):
        patient_id = csv_clinical['Sample ID'][i]
        survival_months = csv_clinical['Overall Survival (Months)'][i]
        survival_status = csv_clinical['Overall Survival Status'][i]

        # don't add patient which have NA for any categories
        if (pd.isna(survival_months)) or (pd.isna(survival_status)):
            null_patients.add(patient_id)
        else:
            patient_data[patient_id] = [survival_months, survival_status]
        i += 1

    return patient_data, null_patients


def get_mrna_expression(csv_expression):
    """Description: returns a dictionary of mRNA expression and quartiles based
    on mRNA expression.

    Arguments:
        csv_clinical (pandas object): the data object to read.
    Returns:
        patient_mrna (dict): key = Sample ID, values = [expression, quartile]
    """
    patient_mrna = dict()

    i = 0
    while i < len(csv_expression):
        pass   


    return patient_mrna



if __name__ == '__main__':
    PATH_EXPRESSION = 'gene_samples/cdk1.txt'
    PATH_CLINICAL = 'gene_samples/cdk1_clinical.tsv'

    CSV_CLINICAL = pd.read_csv(PATH_CLINICAL, delimiter = '\t')
    CSV_EXPRESSION = pd.read_csv(PATH_CLINICAL, delimiter = '\t')

    # trial script
    patient_data, null_patients = get_clinical_data(CSV_EXPRESSION)

