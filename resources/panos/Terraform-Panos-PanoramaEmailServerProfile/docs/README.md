# Terraform::Panos::PanoramaEmailServerProfile

This resource allows you to add/update/delete Panorama email server profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaEmailServerProfile",
    "Properties" : {
        "<a href="#authformat" title="AuthFormat">AuthFormat</a>" : <i>String</i>,
        "<a href="#configformat" title="ConfigFormat">ConfigFormat</a>" : <i>String</i>,
        "<a href="#dataformat" title="DataFormat">DataFormat</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#escapecharacter" title="EscapeCharacter">EscapeCharacter</a>" : <i>String</i>,
        "<a href="#escapedcharacters" title="EscapedCharacters">EscapedCharacters</a>" : <i>String</i>,
        "<a href="#gtpformat" title="GtpFormat">GtpFormat</a>" : <i>String</i>,
        "<a href="#hipmatchformat" title="HipMatchFormat">HipMatchFormat</a>" : <i>String</i>,
        "<a href="#iptagformat" title="IptagFormat">IptagFormat</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sctpformat" title="SctpFormat">SctpFormat</a>" : <i>String</i>,
        "<a href="#systemformat" title="SystemFormat">SystemFormat</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#threatformat" title="ThreatFormat">ThreatFormat</a>" : <i>String</i>,
        "<a href="#trafficformat" title="TrafficFormat">TrafficFormat</a>" : <i>String</i>,
        "<a href="#tunnelformat" title="TunnelFormat">TunnelFormat</a>" : <i>String</i>,
        "<a href="#urlformat" title="UrlFormat">UrlFormat</a>" : <i>String</i>,
        "<a href="#useridformat" title="UserIdFormat">UserIdFormat</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#wildfireformat" title="WildfireFormat">WildfireFormat</a>" : <i>String</i>,
        "<a href="#emailserver" title="EmailServer">EmailServer</a>" : <i>[ <a href="emailserver.md">EmailServer</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaEmailServerProfile
Properties:
    <a href="#authformat" title="AuthFormat">AuthFormat</a>: <i>String</i>
    <a href="#configformat" title="ConfigFormat">ConfigFormat</a>: <i>String</i>
    <a href="#dataformat" title="DataFormat">DataFormat</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#escapecharacter" title="EscapeCharacter">EscapeCharacter</a>: <i>String</i>
    <a href="#escapedcharacters" title="EscapedCharacters">EscapedCharacters</a>: <i>String</i>
    <a href="#gtpformat" title="GtpFormat">GtpFormat</a>: <i>String</i>
    <a href="#hipmatchformat" title="HipMatchFormat">HipMatchFormat</a>: <i>String</i>
    <a href="#iptagformat" title="IptagFormat">IptagFormat</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sctpformat" title="SctpFormat">SctpFormat</a>: <i>String</i>
    <a href="#systemformat" title="SystemFormat">SystemFormat</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#threatformat" title="ThreatFormat">ThreatFormat</a>: <i>String</i>
    <a href="#trafficformat" title="TrafficFormat">TrafficFormat</a>: <i>String</i>
    <a href="#tunnelformat" title="TunnelFormat">TunnelFormat</a>: <i>String</i>
    <a href="#urlformat" title="UrlFormat">UrlFormat</a>: <i>String</i>
    <a href="#useridformat" title="UserIdFormat">UserIdFormat</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#wildfireformat" title="WildfireFormat">WildfireFormat</a>: <i>String</i>
    <a href="#emailserver" title="EmailServer">EmailServer</a>: <i>
      - <a href="emailserver.md">EmailServer</a></i>
</pre>

## Properties

#### AuthFormat

Auth format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigFormat

Config format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFormat

Data format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

The device group location.  Mutually exclusive with
`template` and `template_stack`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscapeCharacter

The escape character.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscapedCharacters

The escaped characters (as a string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GtpFormat

GTP format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HipMatchFormat

HIP match format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IptagFormat

IP tag format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The group's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SctpFormat

SCTP format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemFormat

System format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template location.  Mutually exclusive with
`template_stack` and `device_group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

The template stack location.  Mutually exclusive
with `template` and `device_group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatFormat

Threat format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficFormat

Traffic format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelFormat

Tunnel format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFormat

URL format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdFormat

UserID format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys.  This will likely be `shared`, and it should be
defined if you specified either `template` or `template_stack`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildfireFormat

Wildfire format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailServer

_Required_: No

_Type_: List of <a href="emailserver.md">EmailServer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

