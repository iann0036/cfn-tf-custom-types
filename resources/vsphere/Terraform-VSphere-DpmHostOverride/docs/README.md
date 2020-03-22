# Terraform::VSphere::DpmHostOverride

The `vsphere_dpm_host_override` resource can be used to add a DPM override to a
cluster for a particular host. This allows you to control the power management
settings for individual hosts in the cluster while leaving any unspecified ones
at the default power management settings.

For more information on DPM within vSphere clusters, see [this
page][ref-vsphere-cluster-dpm].

[ref-vsphere-cluster-dpm]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-5E5E349A-4644-4C9C-B434-1C0243EBDC80.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::DpmHostOverride",
    "Properties" : {
        "<a href="#computeclusterid" title="ComputeClusterId">ComputeClusterId</a>" : <i>String</i>,
        "<a href="#dpmautomationlevel" title="DpmAutomationLevel">DpmAutomationLevel</a>" : <i>String</i>,
        "<a href="#dpmenabled" title="DpmEnabled">DpmEnabled</a>" : <i>Boolean</i>,
        "<a href="#hostsystemid" title="HostSystemId">HostSystemId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::DpmHostOverride
Properties:
    <a href="#computeclusterid" title="ComputeClusterId">ComputeClusterId</a>: <i>String</i>
    <a href="#dpmautomationlevel" title="DpmAutomationLevel">DpmAutomationLevel</a>: <i>String</i>
    <a href="#dpmenabled" title="DpmEnabled">DpmEnabled</a>: <i>Boolean</i>
    <a href="#hostsystemid" title="HostSystemId">HostSystemId</a>: <i>String</i>
</pre>

## Properties

#### ComputeClusterId

The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpmAutomationLevel

The automation level for host power
operations on this host. Can be one of `manual` or `automated`. Default:
`manual`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpmEnabled

Enable DPM support for this host. Default:
`false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostSystemId

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

