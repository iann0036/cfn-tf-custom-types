# Terraform::AzureRM::WindowsVirtualMachineScaleSet NetworkInterface

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsservers" title="DnsServers">DnsServers</a>" : <i>[ String, ... ]</i>,
    "<a href="#enableacceleratednetworking" title="EnableAcceleratedNetworking">EnableAcceleratedNetworking</a>" : <i>Boolean</i>,
    "<a href="#enableipforwarding" title="EnableIpForwarding">EnableIpForwarding</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>" : <i>String</i>,
    "<a href="#primary" title="Primary">Primary</a>" : <i>Boolean</i>,
    "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ <a href="networkinterface-ipconfiguration.md">IpConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsservers" title="DnsServers">DnsServers</a>: <i>
      - String</i>
<a href="#enableacceleratednetworking" title="EnableAcceleratedNetworking">EnableAcceleratedNetworking</a>: <i>Boolean</i>
<a href="#enableipforwarding" title="EnableIpForwarding">EnableIpForwarding</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>: <i>String</i>
<a href="#primary" title="Primary">Primary</a>: <i>Boolean</i>
<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - <a href="networkinterface-ipconfiguration.md">IpConfiguration</a></i>
</pre>

## Properties

#### DnsServers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAcceleratedNetworking

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIpForwarding

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Primary

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of <a href="networkinterface-ipconfiguration.md">IpConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

