# TF::CheckPoint::ManagementSimpleGateway InterfacesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#antispoofing" title="AntiSpoofing">AntiSpoofing</a>" : <i>Boolean</i>,
    "<a href="#antispoofingsettings" title="AntiSpoofingSettings">AntiSpoofingSettings</a>" : <i>[ <a href="antispoofingsettingsdefinition.md">AntiSpoofingSettingsDefinition</a>, ... ]</i>,
    "<a href="#color" title="Color">Color</a>" : <i>String</i>,
    "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
    "<a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>" : <i>String</i>,
    "<a href="#ipv4masklength" title="Ipv4MaskLength">Ipv4MaskLength</a>" : <i>String</i>,
    "<a href="#ipv4networkmask" title="Ipv4NetworkMask">Ipv4NetworkMask</a>" : <i>String</i>,
    "<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>" : <i>String</i>,
    "<a href="#ipv6masklength" title="Ipv6MaskLength">Ipv6MaskLength</a>" : <i>String</i>,
    "<a href="#ipv6networkmask" title="Ipv6NetworkMask">Ipv6NetworkMask</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#securityzone" title="SecurityZone">SecurityZone</a>" : <i>Boolean</i>,
    "<a href="#securityzonesettings" title="SecurityZoneSettings">SecurityZoneSettings</a>" : <i>[ <a href="securityzonesettingsdefinition.md">SecurityZoneSettingsDefinition</a>, ... ]</i>,
    "<a href="#topology" title="Topology">Topology</a>" : <i>String</i>,
    "<a href="#topologysettings" title="TopologySettings">TopologySettings</a>" : <i>[ <a href="topologysettingsdefinition.md">TopologySettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#antispoofing" title="AntiSpoofing">AntiSpoofing</a>: <i>Boolean</i>
<a href="#antispoofingsettings" title="AntiSpoofingSettings">AntiSpoofingSettings</a>: <i>
      - <a href="antispoofingsettingsdefinition.md">AntiSpoofingSettingsDefinition</a></i>
<a href="#color" title="Color">Color</a>: <i>String</i>
<a href="#comments" title="Comments">Comments</a>: <i>String</i>
<a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>: <i>String</i>
<a href="#ipv4masklength" title="Ipv4MaskLength">Ipv4MaskLength</a>: <i>String</i>
<a href="#ipv4networkmask" title="Ipv4NetworkMask">Ipv4NetworkMask</a>: <i>String</i>
<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>: <i>String</i>
<a href="#ipv6masklength" title="Ipv6MaskLength">Ipv6MaskLength</a>: <i>String</i>
<a href="#ipv6networkmask" title="Ipv6NetworkMask">Ipv6NetworkMask</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#securityzone" title="SecurityZone">SecurityZone</a>: <i>Boolean</i>
<a href="#securityzonesettings" title="SecurityZoneSettings">SecurityZoneSettings</a>: <i>
      - <a href="securityzonesettingsdefinition.md">SecurityZoneSettingsDefinition</a></i>
<a href="#topology" title="Topology">Topology</a>: <i>String</i>
<a href="#topologysettings" title="TopologySettings">TopologySettings</a>: <i>
      - <a href="topologysettingsdefinition.md">TopologySettingsDefinition</a></i>
</pre>

## Properties

#### AntiSpoofing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiSpoofingSettings

_Required_: No

_Type_: List of <a href="antispoofingsettingsdefinition.md">AntiSpoofingSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4MaskLength

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4NetworkMask

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6MaskLength

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6NetworkMask

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityZone

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityZoneSettings

_Required_: No

_Type_: List of <a href="securityzonesettingsdefinition.md">SecurityZoneSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topology

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologySettings

_Required_: No

_Type_: List of <a href="topologysettingsdefinition.md">TopologySettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

