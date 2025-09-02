# file-transfer-lambda-function

#STEPS TO COMPILE AND GENERATE THE ZIP FOLDER FOR LAMBDA FUNCTION 

# Install dependencies to 'package' folder
pip install google-cloud-storage -t package
pip install -r requirements.txt -t package

# Copy your lambda function code into the package folder
Copy-Item .\src\lambda_function.py .\package\lambda_function.py

# Copy the GCP service account JSON file into the package folder
Copy-Item .\bh-dev-411516-bf8718f6dde5.json .\package\bh-dev-411516-bf8718f6dde5.json
Copy-Item .\jenny1-1-aglley-c693e3454b7b.json .\package\jenny1-1-aglley-c693e3454b7b.json
# Change to the package directory
cd package

# Create a ZIP file of all contents in the package folder
Compress-Archive -Path * -DestinationPath ..\lambda_deploy.zip

# Go back to the project root
cd ..
