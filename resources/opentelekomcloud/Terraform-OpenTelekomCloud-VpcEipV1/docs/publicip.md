# Terraform::OpenTelekomCloud::VpcEipV1 Publicip

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#portid" title="PortId">PortId</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#portid" title="PortId">PortId</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### IpAddress

The value must be a valid IP address in the available
IP address segment. Changing this creates a new eip.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortId

The port id which this eip will associate with. If the value
is "" or this not specified, the eip will be in unbind state.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The value must be a type supported by the system. Only
`5_bgp` supported now. Changing this creates a new eip.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

