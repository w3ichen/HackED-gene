import requests
from bs4 import BeautifulSoup as soup
import json
import bs4

headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}


# clinical_data = requests.get("https://www.cbioportal.org/webservice.do?cmd=getClinicalData&case_set_id=gbm_tcga_pan_can_atlas_2018_all",headers=headers)
# genomic_data = requests.get("https://www.cbioportal.org/webservice.do?cmd=getProfileData&case_set_id=gbm_tcga_pan_can_atlas_2018_rna_seq_"
#                             "v2_mrna&genetic_profile_id=gbm_tcga_pan_can_atlas_2018_rna_seq_v2_mrna_median_Zscores&gene_list=CDK1")
r= requests.get("https://www.cbioportal.org/webservice.do?cmd=getClinicalData&case_set_id=gbm_tcga_pan_can_atlas_2018_all",headers=headers)
print(r)

# page_Soup=soup(clinical_data.text,'xml')
# print(page_Soup,json())

