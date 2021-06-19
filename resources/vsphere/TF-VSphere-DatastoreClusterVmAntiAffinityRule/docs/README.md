# TF::VSphere::DatastoreClusterVmAntiAffinityRule

The `vsphere_datastore_cluster_vm_anti_affinity_rule` resource can be used to
manage VM anti-affinity rules in a datastore cluster, either created by the
[`vsphere_datastore_cluster`][tf-vsphere-datastore-cluster-resource] resource or looked up
by the [`vsphere_datastore_cluster`][tf-vsphere-datastore-cluster-data-source] data source.

[tf-vsphere-datastore-cluster-resource]: /docs/providers/vsphere/r/datastore_cluster.html
[tf-vsphere-datastore-cluster-data-source]: /docs/providers/vsphere/d/datastore_cluster.html

This rule can be used to tell a set to virtual machines to run on different
datastores within a cluster, useful for preventing single points of failure in
application cluster scenarios. When configured, Storage DRS will make a best effort to
ensure that the virtual machines run on different datastores, or prevent any
operation that would keep that from happening, depending on the value of the
[`mandatory`](#mandatory) flag.

~> **NOTE:** This resource requires vCenter and is not available on d...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VSphere::DatastoreClusterVmAntiAffinityRule",
    "Properties" : {
        "<a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#mandatory" title="Mandatory">Mandatory</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#virtualmachineids" title="VirtualMachineIds">VirtualMachineIds</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VSphere::DatastoreClusterVmAntiAffinityRule
Properties:
    <a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#mandatory" title="Mandatory">Mandatory</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#virtualmachineids" title="VirtualMachineIds">VirtualMachineIds</a>: <i>
      - String</i>
</pre>

## Properties

#### DatastoreClusterId

The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the group in.  Forces
a new resource if changed.

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

The name of the rule. This must be unique in the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineIds

The UUIDs of the virtual machines to run
on different datastores from each other.

_Required_: Yes

_Type_: List of String

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

