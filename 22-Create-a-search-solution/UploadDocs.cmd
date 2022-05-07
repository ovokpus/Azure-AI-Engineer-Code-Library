@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

rem Set values for your storage account
set subscription_id=8ef9d38c-cd92-4cea-b46c-0527c93d4acb
set azure_storage_account=ai102form79616945
set azure_storage_key=Cl+WtM8409FjRoiVZv/EdpczMfVlF/N5o1CneYZpSjDgZkXUhVJZkzsQrvFW7FBpNe3guU6zA7XMjBElutJ2QA==


echo Creating container...
call az storage container create --account-name !azure_storage_account! --subscription !subscription_id! --name margies --public-access blob --auth-mode key --account-key !azure_storage_key! --output none

echo Uploading files...
call az storage blob upload-batch -d margies -s data --account-name !azure_storage_account! --auth-mode key --account-key !azure_storage_key!  --output none
