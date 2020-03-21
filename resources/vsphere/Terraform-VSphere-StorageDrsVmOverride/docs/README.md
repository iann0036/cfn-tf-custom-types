# Terraform::VSphere::StorageDrsVmOverride

The `vsphere_storage_drs_vm_override` resource can be used to add a Storage DRS
override to a datastore cluster for a specific virtual machine. With this
resource, one can enable or disable Storage DRS, and control the automation
level and disk affinity for a single virtual machine without affecting the rest
of the datastore cluster.

For more information on vSphere datastore clusters and Storage DRS, see [this
page][ref-vsphere-datastore-clusters].

[ref-vsphere-datastore-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-598DF695-107E-406B-9C95-0AF961FC227A.html

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::StorageDrsVmOverride",
    "Properties" : {
        "<a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>" : <i>String</i>,
        "<a href="#sdrsautomationlevel" title="SdrsAutomationLevel">SdrsAutomationLevel</a>" : <i>String</i>,
        "<a href="#sdrsenabled" title="SdrsEnabled">SdrsEnabled</a>" : <i>String</i>,
        "<a href="#sdrsintravmaffinity" title="SdrsIntraVmAffinity">SdrsIntraVmAffinity</a>" : <i>String</i>,
        "<a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::StorageDrsVmOverride
Properties:
    <a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>: <i>String</i>
    <a href="#sdrsautomationlevel" title="SdrsAutomationLevel">SdrsAutomationLevel</a>: <i>String</i>
    <a href="#sdrsenabled" title="SdrsEnabled">SdrsEnabled</a>: <i>String</i>
    <a href="#sdrsintravmaffinity" title="SdrsIntraVmAffinity">SdrsIntraVmAffinity</a>: <i>String</i>
    <a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>: <i>String</i>
</pre>

## Properties

#### DatastoreClusterId

The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsAutomationLevel

Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsEnabled

Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsIntraVmAffinity

Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineId

The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

