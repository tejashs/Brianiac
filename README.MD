This Python/Flask Application `Brainiac` acts as a liaison between the Android application and the CLOUD ML Prediction API to expose REST service to predict flower types from Images and Digit recognition from images.

This app is intended to be deployed on the App engine of the Google Cloud Platform.

This app requires an existing Prediction service running on the Google ML Engine platform.
Two services are needed. One for Flower Type prediction and one for Digit recognition.

These are the services exposed according to Google's tutorial mentioned below.
1. Flower Prediction - https://github.com/GoogleCloudPlatform/cloudml-samples/tree/master/flowers
2. Digit Prediction MNIST - https://github.com/GoogleCloudPlatform/cloudml-dist-mnist-example

It is expected that both the above services are running under the same project on the Google Cloud platform.

It is also expected that this application would be deployed under the same project on the Google Cloud platform.
If not, then necessary permissions need to be given to the project under which this application would be deployed, to be able to access the Prediction API which is deployed under a different project.
Please refer to Google's documentation if deviating from the procedure.

Changes needed to be made in the SAP HANA Database:
1. Create a table under any schema in the HANA database. Note down the schema name as `FLOWER_SCHEMA` and table name as `FLOWER_DETAILS_TABLE`.
2. Edit the `Flowers.sql` file which is part of the application and enter the schema and table name.
3. Run the `Flowers.sql` file to insert the data into the SAP HANA Database.


Changes needed to be made in the application code:
1. Changes to this application will be made in only 1 file. `util.py`
2. `CLOUD_ML_PROJECT_NAME` is the name of the project under which the prediction APIs are deployed on the Cloud ML engine
3. `FLOWER_ML_MODEL_NAME` is the name of the trained model for flower prediction. If you have followed the Google tutorial to deploy the prediction service, the value for this would be `flowers`
4. `FLOWER_ML_MODEL_VERSION` is the trained model version. It would typically be `v1`
5. `DIGIT_ML_MODEL_NAME` is the name of the trained model for digit recognition. If you have followed the Google tutorial to deploy the prediction service, the value for this would be `MNIST`
6. `DIGIT_ML_MODEL_VERSION` is the trained model version. It would typically be `v1`
7. `CLOUD_STORAGE_BUCKET` is the name of the Google Cloud bucket that is needed to store data temporarily. Please follow Google's documentation to create a cloud bucket and give its unique name as the value
8. `HANA_HOSTNAME`, `HANA_PORT`, `HANA_USERNAME`, `HANA_PASSWORD` are the system details of HANA database in which the Flower details information is stored.
9. `FLOWER_SCHEMA` and `FLOWER_DETAILS_TABLE` are the details of the table in which Flower details information is stored.

Once the changes are made, make sure GCLOUD SDK in installed in your development environment.

1. Deploy the `Brainiac` application onto the App Engine of the Google Cloud Platform by running the following commands.
2. `virtualenv env`
3. `pip install -t lib -r requirements.txt`
4. `gcloud app deploy`
5. Once the app is successfully deployed, go to the following address :
  `http://<application_address>/predict/flower` and `http://<application_address>/predict/number`.
6. You should get an error page that says `Method Not Allowed`. This means that the application is deployed successfully.
This is because the application only exposes Http POST methods and not GET methods. 
