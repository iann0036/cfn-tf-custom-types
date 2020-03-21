# Terraform::VSphere::ComputeClusterVmDependencyRule

The `vsphere_compute_cluster_vm_dependency_rule` resource can be used to manage
VM dependency rules in a cluster, either created by the
[`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

A virtual machine dependency rule applies to vSphere HA, and allows
user-defined startup orders for virtual machines in the case of host failure.
Virtual machines are supplied via groups, which can be managed via the
[`vsphere_compute_cluster_vm_group`][tf-vsphere-cluster-vm-group-resource]
resource.

[tf-vsphere-cluster-vm-group-resource]: /docs/providers/vsphere/r/compute_cluster_vm_group.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::ComputeClusterVmDependencyRule",
    "Properties" : {
        "<a href="#computeclusterid" title="ComputeClusterId">ComputeClusterId</a>" : <i>String</i>,
        "<a href="#dependencyvmgroupname" title="DependencyVmGroupName">DependencyVmGroupName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#mandatory" title="Mandatory">Mandatory</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vmgroupname" title="VmGroupName">VmGroupName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::ComputeClusterVmDependencyRule
Properties:
    <a href="#computeclusterid" title="ComputeClusterId">ComputeClusterId</a>: <i>String</i>
    <a href="#dependencyvmgroupname" title="DependencyVmGroupName">DependencyVmGroupName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#mandatory" title="Mandatory">Mandatory</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vmgroupname" title="VmGroupName">VmGroupName</a>: <i>String</i>
</pre>

## Properties

#### ComputeClusterId

The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DependencyVmGroupName

The name of the VM group that this
rule depends on. The VMs defined in the group specified by
[`vm_group_name`](#vm_group_name) will not be started until the VMs in this
group are started.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enable this rule in the cluster. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mandatory

When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the rule. This must be unique in the
cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmGroupName

The name of the VM group that is the subject of
this rule. The VMs defined in this group will not be started until the VMs in
the group specified by
[`dependency_vm_group_name`](#dependency_vm_group_name) are started.

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

