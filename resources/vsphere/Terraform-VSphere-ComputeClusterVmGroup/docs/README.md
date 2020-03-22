# Terraform::VSphere::ComputeClusterVmGroup

The `vsphere_compute_cluster_vm_group` resource can be used to manage groups of
virtual machines in a cluster, either created by the
[`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

This resource mainly serves as an input to the
[`vsphere_compute_cluster_vm_dependency_rule`][tf-vsphere-cluster-vm-dependency-rule-resource]
and
[`vsphere_compute_cluster_vm_host_rule`][tf-vsphere-cluster-vm-host-rule-resource]
resources. See the individual resource documentation pages for more information.

[tf-vsphere-cluster-vm-dependency-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_dependency_rule.html
[tf-vsphere-cluster-vm-host-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_host_rule.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::ComputeClusterVmGroup",
    "Properties" : {
        "<a href="#computeclusterid" title="ComputeClusterId">ComputeClusterId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#virtualmachineids" title="VirtualMachineIds">VirtualMachineIds</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::ComputeClusterVmGroup
Properties:
    <a href="#computeclusterid" title="ComputeClusterId">ComputeClusterId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#virtualmachineids" title="VirtualMachineIds">VirtualMachineIds</a>: <i>
      - String</i>
</pre>

## Properties

#### ComputeClusterId

The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the VM group. This must be unique in the
cluster. Forces a new resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineIds

The UUIDs of the virtual machines in this
group.

_Required_: No

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

