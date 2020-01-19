import requests
import pandas as pd
import numpy as np

clinical_data = requests.get("https://www.cbioportal.org/webservice.do?cmd=getClinicalData&case_set_id=gbm_tcga_pan_can_atlas_2018_all")
genomic_data = requests.get("https://www.cbioportal.org/webservice.do?cmd=getProfileData&case_set_id=gbm_tcga_pan_can_atlas_2018_rna_seq_v2_mrna&genetic_profile_id=gbm_tcga_pan_can_atlas_2018_rna_seq_v2_mrna_median_Zscores&gene_list=CDK1")

genomic = list(genomic_data.text)

# delete the two lines of comments on the top
del[genomic[0:134]]

genomic = "".join(genomic)


with open("clinical_data.txt","w") as file:	
	file.write(clinical_data.text)
with open("genomic_data.txt","w") as file:	
	file.write(genomic)


print(pd.read_csv("clinical_data.txt", delimiter = '\t'))
print(np.transpose(pd.read_csv("genomic_data.txt", delimiter = '\t')))


