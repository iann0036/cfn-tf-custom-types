# VMware vSphere Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vsphere**. The below arguments may be included as the key/value or JSON properties in the secret:

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
* `api_timeout` - (Optional) Sets the number of minutes to wait for operations
  to complete. The default timeout is 5 minutes. Currently it will override
  the timeout for all VM creation operations.


## Supported Resources

* [TF::VSphere::ComputeClusterHostGroup](../resources/vsphere/TF-VSphere-ComputeClusterHostGroup/docs/README.md)
* [TF::VSphere::ComputeClusterVmAffinityRule](../resources/vsphere/TF-VSphere-ComputeClusterVmAffinityRule/docs/README.md)
* [TF::VSphere::ComputeClusterVmAntiAffinityRule](../resources/vsphere/TF-VSphere-ComputeClusterVmAntiAffinityRule/docs/README.md)
* [TF::VSphere::ComputeClusterVmDependencyRule](../resources/vsphere/TF-VSphere-ComputeClusterVmDependencyRule/docs/README.md)
* [TF::VSphere::ComputeClusterVmGroup](../resources/vsphere/TF-VSphere-ComputeClusterVmGroup/docs/README.md)
* [TF::VSphere::ComputeClusterVmHostRule](../resources/vsphere/TF-VSphere-ComputeClusterVmHostRule/docs/README.md)
* [TF::VSphere::ComputeCluster](../resources/vsphere/TF-VSphere-ComputeCluster/docs/README.md)
* [TF::VSphere::ContentLibraryItem](../resources/vsphere/TF-VSphere-ContentLibraryItem/docs/README.md)
* [TF::VSphere::ContentLibrary](../resources/vsphere/TF-VSphere-ContentLibrary/docs/README.md)
* [TF::VSphere::CustomAttribute](../resources/vsphere/TF-VSphere-CustomAttribute/docs/README.md)
* [TF::VSphere::Datacenter](../resources/vsphere/TF-VSphere-Datacenter/docs/README.md)
* [TF::VSphere::DatastoreClusterVmAntiAffinityRule](../resources/vsphere/TF-VSphere-DatastoreClusterVmAntiAffinityRule/docs/README.md)
* [TF::VSphere::DatastoreCluster](../resources/vsphere/TF-VSphere-DatastoreCluster/docs/README.md)
* [TF::VSphere::DistributedPortGroup](../resources/vsphere/TF-VSphere-DistributedPortGroup/docs/README.md)
* [TF::VSphere::DistributedVirtualSwitch](../resources/vsphere/TF-VSphere-DistributedVirtualSwitch/docs/README.md)
* [TF::VSphere::DpmHostOverride](../resources/vsphere/TF-VSphere-DpmHostOverride/docs/README.md)
* [TF::VSphere::DrsVmOverride](../resources/vsphere/TF-VSphere-DrsVmOverride/docs/README.md)
* [TF::VSphere::EntityPermissions](../resources/vsphere/TF-VSphere-EntityPermissions/docs/README.md)
* [TF::VSphere::File](../resources/vsphere/TF-VSphere-File/docs/README.md)
* [TF::VSphere::Folder](../resources/vsphere/TF-VSphere-Folder/docs/README.md)
* [TF::VSphere::HaVmOverride](../resources/vsphere/TF-VSphere-HaVmOverride/docs/README.md)
* [TF::VSphere::HostPortGroup](../resources/vsphere/TF-VSphere-HostPortGroup/docs/README.md)
* [TF::VSphere::HostVirtualSwitch](../resources/vsphere/TF-VSphere-HostVirtualSwitch/docs/README.md)
* [TF::VSphere::Host](../resources/vsphere/TF-VSphere-Host/docs/README.md)
* [TF::VSphere::License](../resources/vsphere/TF-VSphere-License/docs/README.md)
* [TF::VSphere::NasDatastore](../resources/vsphere/TF-VSphere-NasDatastore/docs/README.md)
* [TF::VSphere::ResourcePool](../resources/vsphere/TF-VSphere-ResourcePool/docs/README.md)
* [TF::VSphere::Role](../resources/vsphere/TF-VSphere-Role/docs/README.md)
* [TF::VSphere::StorageDrsVmOverride](../resources/vsphere/TF-VSphere-StorageDrsVmOverride/docs/README.md)
* [TF::VSphere::TagCategory](../resources/vsphere/TF-VSphere-TagCategory/docs/README.md)
* [TF::VSphere::Tag](../resources/vsphere/TF-VSphere-Tag/docs/README.md)
* [TF::VSphere::VappContainer](../resources/vsphere/TF-VSphere-VappContainer/docs/README.md)
* [TF::VSphere::VappEntity](../resources/vsphere/TF-VSphere-VappEntity/docs/README.md)
* [TF::VSphere::VirtualDisk](../resources/vsphere/TF-VSphere-VirtualDisk/docs/README.md)
* [TF::VSphere::VirtualMachineSnapshot](../resources/vsphere/TF-VSphere-VirtualMachineSnapshot/docs/README.md)
* [TF::VSphere::VirtualMachine](../resources/vsphere/TF-VSphere-VirtualMachine/docs/README.md)
* [TF::VSphere::VmStoragePolicy](../resources/vsphere/TF-VSphere-VmStoragePolicy/docs/README.md)
* [TF::VSphere::VmfsDatastore](../resources/vsphere/TF-VSphere-VmfsDatastore/docs/README.md)
* [TF::VSphere::Vnic](../resources/vsphere/TF-VSphere-Vnic/docs/README.md)