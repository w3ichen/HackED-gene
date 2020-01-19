import numpy as np
import pandas as pd
import gene_preprocessing as gp


# perform ROC analysis
def get_mrna_roc(merged_data):
    """Description: given mRNA expression for high expression (quartile 4) and
    low expression (quartile 1), compare the two groups on survival months
    using an ROC curve.

    Arguments:
        merged_data (dict): the merged mRNA expression and clinical data.
    Returns:
        high_expression (dict): key = Sample ID, value = [overall survival,
            mRNA expression]
        low_expression (dict): key = Sample ID, value = [overall survival,
            mRNA expression]
    """
    high_expression = dict()
    low_expression = dict()

    # if quartile 4, high expression ()
    for k, v in merged_data.items():
        # v[1] contains patient survival status
        if v[1] == 'DECEASED':
            survival_status = 0
        else:
            survival_status = 1

        # v[3] contains quartile based on mRNA expression
        if v[3] == 4:
            # v[0] contains patient survival month
            high_expression[k] = [v[0], survival_status]
        elif v[3] == 1:
            low_expression[k] = [v[0], survival_status]
    return high_expression, low_expression


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
    high_expression, low_expression = get_mrna_roc(merged_data)
