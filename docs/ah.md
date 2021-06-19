# AdvancedHosting Cloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ah**. The below arguments may be included as the key/value or JSON properties in the secret:

* `access_token` - (Required) Security token used for authentication in AdvancedHosting.
  
    **Please pay attention to the fact that the authentication method has been changed to OAuth2. If you use a deprecated `x-auth` token you should [generate](https://websa.advancedhosting.com/api) a new token.**
* `endpoint` - (Optional) Specify which API endpoint to use, can be used to override the default API Endpoint. 



## Supported Resources

* [TF::AH::CloudServerSnapshot](../resources/ah/TF-AH-CloudServerSnapshot/docs/README.md)
* [TF::AH::CloudServer](../resources/ah/TF-AH-CloudServer/docs/README.md)
* [TF::AH::IpAssignment](../resources/ah/TF-AH-IpAssignment/docs/README.md)
* [TF::AH::Ip](../resources/ah/TF-AH-Ip/docs/README.md)
* [TF::AH::PrivateNetworkConnection](../resources/ah/TF-AH-PrivateNetworkConnection/docs/README.md)
* [TF::AH::PrivateNetwork](../resources/ah/TF-AH-PrivateNetwork/docs/README.md)
* [TF::AH::SshKey](../resources/ah/TF-AH-SshKey/docs/README.md)
* [TF::AH::VolumeAttachment](../resources/ah/TF-AH-VolumeAttachment/docs/README.md)
* [TF::AH::Volume](../resources/ah/TF-AH-Volume/docs/README.md)