# MongoDB Atlas Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/mongodbatlas**. The below arguments may be included as the key/value or JSON properties in the secret:

* `public_key` - (Optional) This is the public key of your MongoDB Atlas API key pair.

* `private_key` - (Optional) This is the private key of your MongoDB Atlas key pair.

For more information on configuring and managing programmatic API Keys see the [MongoDB Atlas Documentation](https://docs.atlas.mongodb.com/tutorial/manage-programmatic-access/index.html).


## Supported Resources

* [TF::MongoDBAtlas::AlertConfiguration](../resources/mongodbatlas/TF-MongoDBAtlas-AlertConfiguration/docs/README.md)
* [TF::MongoDBAtlas::Auditing](../resources/mongodbatlas/TF-MongoDBAtlas-Auditing/docs/README.md)
* [TF::MongoDBAtlas::CloudProviderAccessAuthorization](../resources/mongodbatlas/TF-MongoDBAtlas-CloudProviderAccessAuthorization/docs/README.md)
* [TF::MongoDBAtlas::CloudProviderAccessSetup](../resources/mongodbatlas/TF-MongoDBAtlas-CloudProviderAccessSetup/docs/README.md)
* [TF::MongoDBAtlas::CloudProviderAccess](../resources/mongodbatlas/TF-MongoDBAtlas-CloudProviderAccess/docs/README.md)
* [TF::MongoDBAtlas::CloudProviderSnapshotBackupPolicy](../resources/mongodbatlas/TF-MongoDBAtlas-CloudProviderSnapshotBackupPolicy/docs/README.md)
* [TF::MongoDBAtlas::CloudProviderSnapshotRestoreJob](../resources/mongodbatlas/TF-MongoDBAtlas-CloudProviderSnapshotRestoreJob/docs/README.md)
* [TF::MongoDBAtlas::CloudProviderSnapshot](../resources/mongodbatlas/TF-MongoDBAtlas-CloudProviderSnapshot/docs/README.md)
* [TF::MongoDBAtlas::Cluster](../resources/mongodbatlas/TF-MongoDBAtlas-Cluster/docs/README.md)
* [TF::MongoDBAtlas::CustomDbRole](../resources/mongodbatlas/TF-MongoDBAtlas-CustomDbRole/docs/README.md)
* [TF::MongoDBAtlas::CustomDnsConfigurationClusterAws](../resources/mongodbatlas/TF-MongoDBAtlas-CustomDnsConfigurationClusterAws/docs/README.md)
* [TF::MongoDBAtlas::DatabaseUser](../resources/mongodbatlas/TF-MongoDBAtlas-DatabaseUser/docs/README.md)
* [TF::MongoDBAtlas::EncryptionAtRest](../resources/mongodbatlas/TF-MongoDBAtlas-EncryptionAtRest/docs/README.md)
* [TF::MongoDBAtlas::GlobalClusterConfig](../resources/mongodbatlas/TF-MongoDBAtlas-GlobalClusterConfig/docs/README.md)
* [TF::MongoDBAtlas::LdapConfiguration](../resources/mongodbatlas/TF-MongoDBAtlas-LdapConfiguration/docs/README.md)
* [TF::MongoDBAtlas::LdapVerify](../resources/mongodbatlas/TF-MongoDBAtlas-LdapVerify/docs/README.md)
* [TF::MongoDBAtlas::MaintenanceWindow](../resources/mongodbatlas/TF-MongoDBAtlas-MaintenanceWindow/docs/README.md)
* [TF::MongoDBAtlas::NetworkContainer](../resources/mongodbatlas/TF-MongoDBAtlas-NetworkContainer/docs/README.md)
* [TF::MongoDBAtlas::NetworkPeering](../resources/mongodbatlas/TF-MongoDBAtlas-NetworkPeering/docs/README.md)
* [TF::MongoDBAtlas::PrivateEndpointInterfaceLink](../resources/mongodbatlas/TF-MongoDBAtlas-PrivateEndpointInterfaceLink/docs/README.md)
* [TF::MongoDBAtlas::PrivateEndpoint](../resources/mongodbatlas/TF-MongoDBAtlas-PrivateEndpoint/docs/README.md)
* [TF::MongoDBAtlas::PrivateIpMode](../resources/mongodbatlas/TF-MongoDBAtlas-PrivateIpMode/docs/README.md)
* [TF::MongoDBAtlas::PrivatelinkEndpointService](../resources/mongodbatlas/TF-MongoDBAtlas-PrivatelinkEndpointService/docs/README.md)
* [TF::MongoDBAtlas::PrivatelinkEndpoint](../resources/mongodbatlas/TF-MongoDBAtlas-PrivatelinkEndpoint/docs/README.md)
* [TF::MongoDBAtlas::ProjectIpAccessList](../resources/mongodbatlas/TF-MongoDBAtlas-ProjectIpAccessList/docs/README.md)
* [TF::MongoDBAtlas::ProjectIpWhitelist](../resources/mongodbatlas/TF-MongoDBAtlas-ProjectIpWhitelist/docs/README.md)
* [TF::MongoDBAtlas::Project](../resources/mongodbatlas/TF-MongoDBAtlas-Project/docs/README.md)
* [TF::MongoDBAtlas::Team](../resources/mongodbatlas/TF-MongoDBAtlas-Team/docs/README.md)
* [TF::MongoDBAtlas::Teams](../resources/mongodbatlas/TF-MongoDBAtlas-Teams/docs/README.md)
* [TF::MongoDBAtlas::ThirdPartyIntegration](../resources/mongodbatlas/TF-MongoDBAtlas-ThirdPartyIntegration/docs/README.md)
* [TF::MongoDBAtlas::X509AuthenticationDatabaseUser](../resources/mongodbatlas/TF-MongoDBAtlas-X509AuthenticationDatabaseUser/docs/README.md)