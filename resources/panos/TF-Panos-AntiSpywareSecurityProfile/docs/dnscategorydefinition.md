# TF::Panos::AntiSpywareSecurityProfile DnsCategoryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#loglevel" title="LogLevel">LogLevel</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#packetcapture" title="PacketCapture">PacketCapture</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#loglevel" title="LogLevel">LogLevel</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#packetcapture" title="PacketCapture">PacketCapture</a>: <i>String</i>
</pre>

## Properties

#### Action

Action to take.  Valid values are `alert`, `default`, `allow`,
`block`, or `sinkhole`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevel

Logging level.  Valid values are `default`, `none`, `low`,
`informational`, `medium`, `high`, or `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketCapture

Packet capture setting.  Valid values
are `disable`, `single-packet`, or `extended-capture`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

