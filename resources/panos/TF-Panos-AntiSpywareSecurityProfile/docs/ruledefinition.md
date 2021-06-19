# TF::Panos::AntiSpywareSecurityProfile RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#blockipduration" title="BlockIpDuration">BlockIpDuration</a>" : <i>Double</i>,
    "<a href="#blockiptrackby" title="BlockIpTrackBy">BlockIpTrackBy</a>" : <i>String</i>,
    "<a href="#category" title="Category">Category</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#packetcapture" title="PacketCapture">PacketCapture</a>" : <i>String</i>,
    "<a href="#severities" title="Severities">Severities</a>" : <i>[ String, ... ]</i>,
    "<a href="#threatname" title="ThreatName">ThreatName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#blockipduration" title="BlockIpDuration">BlockIpDuration</a>: <i>Double</i>
<a href="#blockiptrackby" title="BlockIpTrackBy">BlockIpTrackBy</a>: <i>String</i>
<a href="#category" title="Category">Category</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#packetcapture" title="PacketCapture">PacketCapture</a>: <i>String</i>
<a href="#severities" title="Severities">Severities</a>: <i>
      - String</i>
<a href="#threatname" title="ThreatName">ThreatName</a>: <i>String</i>
</pre>

## Properties

#### Action

Action.  Valid values are `default`, `allow`, `alert`, `drop`,
`reset-client`, `reset-server`, `reset-both`, or `block-ip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockIpDuration

The duration.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockIpTrackBy

The track by setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

Category.

_Required_: Yes

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

#### Severities

Severities.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatName

Threat name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

