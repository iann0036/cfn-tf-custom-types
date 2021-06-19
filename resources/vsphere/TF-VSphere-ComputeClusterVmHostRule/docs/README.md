# TF::VSphere::ComputeClusterVmHostRule

The `vsphere_compute_cluster_vm_host_rule` resource can be used to manage
VM-to-host rules in a cluster, either created by the
[`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

This resource can create both _affinity rules_, where virtual machines run on
specified hosts, or _anti-affinity_ rules, where virtual machines run on hosts
outside of the ones specified in the rule. Virtual machines and hosts are
supplied via groups, which can be managed via the
[`vsphere_compute_cluster_vm_group`][tf-vsphere-cluster-vm-group-resource] and
[`vsphere_compute_cluster_host_group`][tf-vsphere-cluster-host-group-resource]
resources.

[tf-vsphere-cluster-vm-group-resource]: /docs/providers/vsphere/r/compute_cluster_vm_group.html
[tf-vsphere-cluster-host-g...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VSphere::ComputeClusterVmHostRule",
    "Properties" : {
        "<a href="#affinityhostgroupname" title="AffinityHostGroupName">AffinityHostGroupName</a>" : <i>String</i>,
        "<a href="#antiaffinityhostgroupname" title="AntiAffinityHostGroupName">AntiAffinityHostGroupName</a>" : <i>String</i>,
        "<a href="#computeclusterid" title="ComputeClusterId">ComputeClusterId</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#mandatory" title="Mandatory">Mandatory</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vmgroupname" title="VmGroupName">VmGroupName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VSphere::ComputeClusterVmHostRule
Properties:
    <a href="#affinityhostgroupname" title="AffinityHostGroupName">AffinityHostGroupName</a>: <i>String</i>
    <a href="#antiaffinityhostgroupname" title="AntiAffinityHostGroupName">AntiAffinityHostGroupName</a>: <i>String</i>
    <a href="#computeclusterid" title="ComputeClusterId">ComputeClusterId</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#mandatory" title="Mandatory">Mandatory</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vmgroupname" title="VmGroupName">VmGroupName</a>: <i>String</i>
</pre>

## Properties

#### AffinityHostGroupName

When this field is used, the virtual
machines defined in [`vm_group_name`](#vm_group_name) will be run on the
hosts defined in this host group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiAffinityHostGroupName

When this field is used, the
virtual machines defined in [`vm_group_name`](#vm_group_name) will _not_ be
run on the hosts defined in this host group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeClusterId

The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

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

The name of the virtual machine group to use
with this rule.

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

#### Id

Returns the <code>Id</code> value.

