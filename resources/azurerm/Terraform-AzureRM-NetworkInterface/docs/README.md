# Terraform::AzureRM::NetworkInterface

Manages a Network Interface.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::NetworkInterface",
    "Properties" : {
        "<a href="#dnsservers" title="DnsServers">DnsServers</a>" : <i>[ String, ... ]</i>,
        "<a href="#enableacceleratednetworking" title="EnableAcceleratedNetworking">EnableAcceleratedNetworking</a>" : <i>Boolean</i>,
        "<a href="#enableipforwarding" title="EnableIpForwarding">EnableIpForwarding</a>" : <i>Boolean</i>,
        "<a href="#internaldnsnamelabel" title="InternalDnsNameLabel">InternalDnsNameLabel</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ <a href="ipconfiguration.md">IpConfiguration</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::NetworkInterface
Properties:
    <a href="#dnsservers" title="DnsServers">DnsServers</a>: <i>
      - String</i>
    <a href="#enableacceleratednetworking" title="EnableAcceleratedNetworking">EnableAcceleratedNetworking</a>: <i>Boolean</i>
    <a href="#enableipforwarding" title="EnableIpForwarding">EnableIpForwarding</a>: <i>Boolean</i>
    <a href="#internaldnsnamelabel" title="InternalDnsNameLabel">InternalDnsNameLabel</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - <a href="ipconfiguration.md">IpConfiguration</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DnsServers

A list of IP Addresses defining the DNS Servers which should be used for this Network Interface.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAcceleratedNetworking

Should Accelerated Networking be enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIpForwarding

Should IP Forwarding be enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalDnsNameLabel

The (relative) DNS Name used for internal communications between Virtual Machines in the same Virtual Network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location where the Network Interface should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Network Interface. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group in which to create the Network Interface. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of <a href="ipconfiguration.md">IpConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AppliedDnsServers

Returns the <code>AppliedDnsServers</code> value.

#### Id

Returns the <code>Id</code> value.

#### MacAddress

Returns the <code>MacAddress</code> value.

#### PrivateIpAddress

Returns the <code>PrivateIpAddress</code> value.

#### PrivateIpAddresses

Returns the <code>PrivateIpAddresses</code> value.

#### VirtualMachineId

Returns the <code>VirtualMachineId</code> value.

