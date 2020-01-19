import requests


clinical_data = requests.get("https://www.cbioportal.org/webservice.do?cmd=getClinicalData&case_set_id=gbm_tcga_pan_can_atlas_2018_all")
genomic_data = requests.get("https://www.cbioportal.org/webservice.do?cmd=getProfileData&case_set_id=gbm_tcga_pan_can_atlas_2018_rna_seq_"
                            "v2_mrna&genetic_profile_id=gbm_tcga_pan_can_atlas_2018_rna_seq_v2_mrna_median_Zscores&gene_list=CDK1")

# print(clinical_data.text)
# print(genomic_data.text)

