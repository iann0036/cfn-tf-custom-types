# TF::ECL::SecurityNetworkBasedDeviceHaV2 HaLink2Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#host1ipaddress" title="Host1IpAddress">Host1IpAddress</a>" : <i>String</i>,
    "<a href="#host2ipaddress" title="Host2IpAddress">Host2IpAddress</a>" : <i>String</i>,
    "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#host1ipaddress" title="Host1IpAddress">Host1IpAddress</a>: <i>String</i>
<a href="#host2ipaddress" title="Host2IpAddress">Host2IpAddress</a>: <i>String</i>
<a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### Host1IpAddress

Set IPv4 address for as HA Host 1 in this HA link.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host2IpAddress

Set IPv4 address for as HA Host 2 in this HA link.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

Set the Network ID to be used for HA line.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Set the Subnet ID to be used for HA line.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

