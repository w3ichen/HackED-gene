# import numpy as np
import pandas as pd
import gene_preprocessing as gp
import sklearn.metrics as metrics
import numpy as np


# perform ROC analysis
def get_mrna_list(merged_data, time_cutoff):
    """Description: given mRNA expression for high expression (quartile 4) and
    low expression (quartile 1), compare the two groups on survival months
    using an ROC curve.

    Arguments:
        merged_data (dict): the merged mRNA expression and clinical data.
    Returns:
        high_expression (list): [Sample ID, overall survival months, overall
            survival status, mRNA expression]
        low_expression (list): [Sample ID, overall survival, overall survival
            status, mRNA expression]
    Notes: 0 means deceased, 1 means alive.
    """
    high_expression = list()
    low_expression = list()

    # if quartile 4, high expression
    for k, v in merged_data.items():
        # v[1] contains patient survival status
        if v[1] == 'DECEASED':
            survival_status = 0
        else:
            survival_status = 1

        if v[0] > time_cutoff:
            # v[0] contains patient survival month
            # v[2] contains mRNA expression
            high_expression.append([k, v[0], survival_status, v[2]])
        else:
            low_expression.append([k, v[0], survival_status, v[2]])
    return high_expression, low_expression


def get_single_gene_roc(expression_data):
    """Description: returns the point of maximum sum of true positive and false
    positive rate.

    Arguments:
        expression_data (dict): key = sample ID, value = [overall survival, mRNA
            expression]
    Returns:
        insert here
    """
    pass


if __name__ == '__main__':
    PATH_EXPRESSION = 'gene_samples/cdk1.txt'
    PATH_CLINICAL = 'gene_samples/cdk1_clinical.tsv'

    CSV_CLINICAL = pd.read_csv(PATH_CLINICAL, delimiter = '\t')
    CSV_EXPRESSION = pd.read_csv(PATH_EXPRESSION, delimiter = '\t')

    # trial script
    patient_data, null_patients = gp.get_clinical_data(CSV_CLINICAL)
    patient_mrna = gp.get_mrna_expression('CDK1', CSV_EXPRESSION)
    merged_data = gp.merge(patient_data, patient_mrna)

    # roc stuff
    high_expression, low_expression = get_mrna_list(merged_data, 36)
