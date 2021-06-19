# Artifactory Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/artifactory**. The below arguments may be included as the key/value or JSON properties in the secret:

* `url` - (Required) URL of Artifactory.
* `username` - (Optional) Username for basic auth. Requires `password` to be set. 
    Conflicts with `api_key`, and `access_token`.
* `password` - (Optional) Password for basic auth. Requires `username` to be set. 
    Conflicts with `api_key`, and `access_token`.
* `api_key` - (Optional) API key for api auth. Uses `X-JFrog-Art-Api` header. 
    Conflicts with `username`, `password`, and `access_token`.
* `access_token` - (Optional) API key for token auth. Uses `Authorization: Bearer` header. 
    Conflicts with `username` and `password`, and `api_key`.


## Supported Resources

* [TF::Artifactory::AccessToken](../resources/artifactory/TF-Artifactory-AccessToken/docs/README.md)
* [TF::Artifactory::ApiKey](../resources/artifactory/TF-Artifactory-ApiKey/docs/README.md)
* [TF::Artifactory::Certificate](../resources/artifactory/TF-Artifactory-Certificate/docs/README.md)
* [TF::Artifactory::Group](../resources/artifactory/TF-Artifactory-Group/docs/README.md)
* [TF::Artifactory::LocalRepository](../resources/artifactory/TF-Artifactory-LocalRepository/docs/README.md)
* [TF::Artifactory::PermissionTarget](../resources/artifactory/TF-Artifactory-PermissionTarget/docs/README.md)
* [TF::Artifactory::PermissionTargets](../resources/artifactory/TF-Artifactory-PermissionTargets/docs/README.md)
* [TF::Artifactory::RemoteRepository](../resources/artifactory/TF-Artifactory-RemoteRepository/docs/README.md)
* [TF::Artifactory::ReplicationConfig](../resources/artifactory/TF-Artifactory-ReplicationConfig/docs/README.md)
* [TF::Artifactory::SingleReplicationConfig](../resources/artifactory/TF-Artifactory-SingleReplicationConfig/docs/README.md)
* [TF::Artifactory::User](../resources/artifactory/TF-Artifactory-User/docs/README.md)
* [TF::Artifactory::VirtualRepository](../resources/artifactory/TF-Artifactory-VirtualRepository/docs/README.md)
* [TF::Artifactory::XrayPolicy](../resources/artifactory/TF-Artifactory-XrayPolicy/docs/README.md)
* [TF::Artifactory::XrayWatch](../resources/artifactory/TF-Artifactory-XrayWatch/docs/README.md)