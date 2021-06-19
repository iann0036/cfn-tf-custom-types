# VMware Cloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vmc**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_token` - (Required) API token is used to authenticate when calling VMware Cloud Services APIs.
   This token is scoped within the organization.
*  `org_id` - (Required) Organization Identifier.
*  `vmc_url` - (Optional) VMware Cloud on AWS URL. Default : https://vmc.vmware.com
*  `csp_url` - (Optional) Cloud Service Provider URL. Default : https://console.cloud.vmware.com


## Supported Resources

* [TF::VMC::Cluster](../resources/vmc/TF-VMC-Cluster/docs/README.md)
* [TF::VMC::PublicIp](../resources/vmc/TF-VMC-PublicIp/docs/README.md)
* [TF::VMC::Sddc](../resources/vmc/TF-VMC-Sddc/docs/README.md)
* [TF::VMC::SiteRecovery](../resources/vmc/TF-VMC-SiteRecovery/docs/README.md)
* [TF::VMC::SrmNode](../resources/vmc/TF-VMC-SrmNode/docs/README.md)