# TF::FortiOS::SystemAccprofile NetgrpPermissionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cfg" title="Cfg">Cfg</a>" : <i>String</i>,
    "<a href="#packetcapture" title="PacketCapture">PacketCapture</a>" : <i>String</i>,
    "<a href="#routecfg" title="RouteCfg">RouteCfg</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cfg" title="Cfg">Cfg</a>: <i>String</i>
<a href="#packetcapture" title="PacketCapture">PacketCapture</a>: <i>String</i>
<a href="#routecfg" title="RouteCfg">RouteCfg</a>: <i>String</i>
</pre>

## Properties

#### Cfg

Network Configuration. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketCapture

Packet Capture Configuration. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteCfg

Router Configuration. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

