# NetApp Cloud Volumes Service for Google Cloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/netapp-gcp**. The below arguments may be included as the key/value or JSON properties in the secret:

* `project` - (Required) This is the project number or project ID for NetApp_GCP API operations
* `service_account` - (Required) This is the path of service_account for NetApp_GCP API operations.


## Supported Resources

* [TF::NetAppGCP::ActiveDirectory](../resources/netapp-gcp/TF-NetAppGCP-ActiveDirectory/docs/README.md)
* [TF::NetAppGCP::Snapshot](../resources/netapp-gcp/TF-NetAppGCP-Snapshot/docs/README.md)
* [TF::NetAppGCP::VolumeBackup](../resources/netapp-gcp/TF-NetAppGCP-VolumeBackup/docs/README.md)
* [TF::NetAppGCP::Volume](../resources/netapp-gcp/TF-NetAppGCP-Volume/docs/README.md)