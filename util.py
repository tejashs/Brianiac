
# Cloud ML Service related parameters
CLOUD_ML_PROJECT_NAME="<YOUR_CLOUD_ML_PROJECT_NAME>" # Can be found from the Google Cloud Console
# Same project is assumed for both Flowers and Digits prediction service
# eg :'steam-airfoil-169600'

FLOWER_ML_MODEL_NAME="flowers" #"<YOUR_CLOUD_ML_FLOWER_ML_MODEL_NAME>" # Usually "flowers"
FLOWER_ML_MODEL_VERSION="v1" #"<YOUR_CLOUD_ML_FLOWER_ML_MODEL_VERSION>" # Usually "v1"

DIGIT_ML_MODEL_NAME="MNIST" #"<YOUR_CLOUD_ML_FLOWER_ML_MODEL_NAME>" # Usually "MNIST"
DIGIT_ML_MODEL_VERSION="v1" #"<YOUR_CLOUD_ML_FLOWER_ML_MODEL_VERSION>" # Usually "v1"


# Google Cloud Storage parameters
CLOUD_STORAGE_BUCKET="<YOUR_CLOUD_STORAGE_BUCKET_NAME>"  #eg:   "brainiac-bucket"


# HANA Database related parameters
HANA_HOSTNAME="<YOUR_IP_ADDRESS_FOR_HANA>"
HANA_PORT="<YOUR_PORT_NUMBER_FOR_HANA>"
# 39013 is the systemDB port for HXE on the default instance of 90.
# Replace 90 with your instance number as needed (e.g. 30013 for instance 00)
# 39013 for Tenant DB
HANA_USERNAME="<YOUR_HANA_USERNAME>"
HANA_PASSWORD="<YOUR_HANA_PASSWORD>"

FLOWER_SCHEMA="<YOUR_FLOWER_SCHEMA_NAME>"
FLOWER_DETAILS_TABLE="<YOUR_FLOWER_DETAILS_TABLE_NAME>"
