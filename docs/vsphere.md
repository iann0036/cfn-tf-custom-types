# VMware vSphere Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vsphere**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `user` - (Required) This is the username for vSphere API operations.
* `password` - (Required) This is the password for vSphere API operations.
* `vsphere_server` - (Required) This is the vCenter server name for vSphere API
  operations. Can also be specified with the `VSPHERE_SERVER` environment
  variable.
* `allow_unverified_ssl` - (Optional) Boolean that can be set to true to
  disable SSL certificate verification. This should be used with care as it
  could allow an attacker to intercept your auth token. If omitted, default
  value is `false`.
* `vim_keep_alive` - (Optional) Keep alive interval in minutes for the VIM
  session. Standard session timeout in vSphere is 30 minutes. This defaults to
  10 minutes to ensure that operations that take a longer than 30 minutes
  without API interaction do not result in a session timeout.


## Supported Resources

* [Terraform::VSphere::ComputeClusterHostGroup](../resources/vsphere/Terraform-VSphere-ComputeClusterHostGroup/docs/README.md)
* [Terraform::VSphere::ComputeClusterVmAffinityRule](../resources/vsphere/Terraform-VSphere-ComputeClusterVmAffinityRule/docs/README.md)
* [Terraform::VSphere::ComputeClusterVmAntiAffinityRule](../resources/vsphere/Terraform-VSphere-ComputeClusterVmAntiAffinityRule/docs/README.md)
* [Terraform::VSphere::ComputeClusterVmDependencyRule](../resources/vsphere/Terraform-VSphere-ComputeClusterVmDependencyRule/docs/README.md)
* [Terraform::VSphere::ComputeClusterVmGroup](../resources/vsphere/Terraform-VSphere-ComputeClusterVmGroup/docs/README.md)
* [Terraform::VSphere::ComputeClusterVmHostRule](../resources/vsphere/Terraform-VSphere-ComputeClusterVmHostRule/docs/README.md)
* [Terraform::VSphere::ComputeCluster](../resources/vsphere/Terraform-VSphere-ComputeCluster/docs/README.md)
* [Terraform::VSphere::ContentLibraryItem](../resources/vsphere/Terraform-VSphere-ContentLibraryItem/docs/README.md)
* [Terraform::VSphere::ContentLibrary](../resources/vsphere/Terraform-VSphere-ContentLibrary/docs/README.md)
* [Terraform::VSphere::CustomAttribute](../resources/vsphere/Terraform-VSphere-CustomAttribute/docs/README.md)
* [Terraform::VSphere::Datacenter](../resources/vsphere/Terraform-VSphere-Datacenter/docs/README.md)
* [Terraform::VSphere::DatastoreClusterVmAntiAffinityRule](../resources/vsphere/Terraform-VSphere-DatastoreClusterVmAntiAffinityRule/docs/README.md)
* [Terraform::VSphere::DatastoreCluster](../resources/vsphere/Terraform-VSphere-DatastoreCluster/docs/README.md)
* [Terraform::VSphere::DistributedPortGroup](../resources/vsphere/Terraform-VSphere-DistributedPortGroup/docs/README.md)
* [Terraform::VSphere::DistributedVirtualSwitch](../resources/vsphere/Terraform-VSphere-DistributedVirtualSwitch/docs/README.md)
* [Terraform::VSphere::DpmHostOverride](../resources/vsphere/Terraform-VSphere-DpmHostOverride/docs/README.md)
* [Terraform::VSphere::DrsVmOverride](../resources/vsphere/Terraform-VSphere-DrsVmOverride/docs/README.md)
* [Terraform::VSphere::File](../resources/vsphere/Terraform-VSphere-File/docs/README.md)
* [Terraform::VSphere::Folder](../resources/vsphere/Terraform-VSphere-Folder/docs/README.md)
* [Terraform::VSphere::HaVmOverride](../resources/vsphere/Terraform-VSphere-HaVmOverride/docs/README.md)
* [Terraform::VSphere::HostPortGroup](../resources/vsphere/Terraform-VSphere-HostPortGroup/docs/README.md)
* [Terraform::VSphere::HostVirtualSwitch](../resources/vsphere/Terraform-VSphere-HostVirtualSwitch/docs/README.md)
* [Terraform::VSphere::Host](../resources/vsphere/Terraform-VSphere-Host/docs/README.md)
* [Terraform::VSphere::License](../resources/vsphere/Terraform-VSphere-License/docs/README.md)
* [Terraform::VSphere::NasDatastore](../resources/vsphere/Terraform-VSphere-NasDatastore/docs/README.md)
* [Terraform::VSphere::ResourcePool](../resources/vsphere/Terraform-VSphere-ResourcePool/docs/README.md)
* [Terraform::VSphere::StorageDrsVmOverride](../resources/vsphere/Terraform-VSphere-StorageDrsVmOverride/docs/README.md)
* [Terraform::VSphere::TagCategory](../resources/vsphere/Terraform-VSphere-TagCategory/docs/README.md)
* [Terraform::VSphere::Tag](../resources/vsphere/Terraform-VSphere-Tag/docs/README.md)
* [Terraform::VSphere::VappContainer](../resources/vsphere/Terraform-VSphere-VappContainer/docs/README.md)
* [Terraform::VSphere::VappEntity](../resources/vsphere/Terraform-VSphere-VappEntity/docs/README.md)
* [Terraform::VSphere::VirtualDisk](../resources/vsphere/Terraform-VSphere-VirtualDisk/docs/README.md)
* [Terraform::VSphere::VirtualMachineSnapshot](../resources/vsphere/Terraform-VSphere-VirtualMachineSnapshot/docs/README.md)
* [Terraform::VSphere::VirtualMachine](../resources/vsphere/Terraform-VSphere-VirtualMachine/docs/README.md)
* [Terraform::VSphere::VmfsDatastore](../resources/vsphere/Terraform-VSphere-VmfsDatastore/docs/README.md)
* [Terraform::VSphere::Vnic](../resources/vsphere/Terraform-VSphere-Vnic/docs/README.md)