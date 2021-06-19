# NetApp Cloud Volumes ONTAP Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/netapp-cloudmanager**. The below arguments may be included as the key/value or JSON properties in the secret:

* `refresh_token` - (Required) This is the refresh token for NetApp Cloud Manager API operations. Get the token from [NetApp Cloud Central](https://services.cloud.netapp.com/refresh-token)


## Supported Resources

* [TF::NetAppCloudManager::Aggregate](../resources/netapp-cloudmanager/TF-NetAppCloudManager-Aggregate/docs/README.md)
* [TF::NetAppCloudManager::AnfVolume](../resources/netapp-cloudmanager/TF-NetAppCloudManager-AnfVolume/docs/README.md)
* [TF::NetAppCloudManager::CifsServer](../resources/netapp-cloudmanager/TF-NetAppCloudManager-CifsServer/docs/README.md)
* [TF::NetAppCloudManager::ConnectorAws](../resources/netapp-cloudmanager/TF-NetAppCloudManager-ConnectorAws/docs/README.md)
* [TF::NetAppCloudManager::ConnectorAzure](../resources/netapp-cloudmanager/TF-NetAppCloudManager-ConnectorAzure/docs/README.md)
* [TF::NetAppCloudManager::ConnectorGcp](../resources/netapp-cloudmanager/TF-NetAppCloudManager-ConnectorGcp/docs/README.md)
* [TF::NetAppCloudManager::CvoAws](../resources/netapp-cloudmanager/TF-NetAppCloudManager-CvoAws/docs/README.md)
* [TF::NetAppCloudManager::CvoAzure](../resources/netapp-cloudmanager/TF-NetAppCloudManager-CvoAzure/docs/README.md)
* [TF::NetAppCloudManager::CvoGcp](../resources/netapp-cloudmanager/TF-NetAppCloudManager-CvoGcp/docs/README.md)
* [TF::NetAppCloudManager::CvsGcpVolume](../resources/netapp-cloudmanager/TF-NetAppCloudManager-CvsGcpVolume/docs/README.md)
* [TF::NetAppCloudManager::NssAccount](../resources/netapp-cloudmanager/TF-NetAppCloudManager-NssAccount/docs/README.md)
* [TF::NetAppCloudManager::Snapmirror](../resources/netapp-cloudmanager/TF-NetAppCloudManager-Snapmirror/docs/README.md)
* [TF::NetAppCloudManager::Volume](../resources/netapp-cloudmanager/TF-NetAppCloudManager-Volume/docs/README.md)