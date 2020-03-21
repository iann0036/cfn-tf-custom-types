# Terraform::Panos::EmailServerProfile

CloudFormation equivalent of panos_email_server_profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::EmailServerProfile",
    "Properties" : {
        "<a href="#authformat" title="AuthFormat">AuthFormat</a>" : <i>String</i>,
        "<a href="#configformat" title="ConfigFormat">ConfigFormat</a>" : <i>String</i>,
        "<a href="#dataformat" title="DataFormat">DataFormat</a>" : <i>String</i>,
        "<a href="#escapecharacter" title="EscapeCharacter">EscapeCharacter</a>" : <i>String</i>,
        "<a href="#escapedcharacters" title="EscapedCharacters">EscapedCharacters</a>" : <i>String</i>,
        "<a href="#gtpformat" title="GtpFormat">GtpFormat</a>" : <i>String</i>,
        "<a href="#hipmatchformat" title="HipMatchFormat">HipMatchFormat</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#iptagformat" title="IptagFormat">IptagFormat</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sctpformat" title="SctpFormat">SctpFormat</a>" : <i>String</i>,
        "<a href="#systemformat" title="SystemFormat">SystemFormat</a>" : <i>String</i>,
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
Type: Terraform::Panos::EmailServerProfile
Properties:
    <a href="#authformat" title="AuthFormat">AuthFormat</a>: <i>String</i>
    <a href="#configformat" title="ConfigFormat">ConfigFormat</a>: <i>String</i>
    <a href="#dataformat" title="DataFormat">DataFormat</a>: <i>String</i>
    <a href="#escapecharacter" title="EscapeCharacter">EscapeCharacter</a>: <i>String</i>
    <a href="#escapedcharacters" title="EscapedCharacters">EscapedCharacters</a>: <i>String</i>
    <a href="#gtpformat" title="GtpFormat">GtpFormat</a>: <i>String</i>
    <a href="#hipmatchformat" title="HipMatchFormat">HipMatchFormat</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#iptagformat" title="IptagFormat">IptagFormat</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sctpformat" title="SctpFormat">SctpFormat</a>: <i>String</i>
    <a href="#systemformat" title="SystemFormat">SystemFormat</a>: <i>String</i>
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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscapeCharacter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscapedCharacters

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GtpFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HipMatchFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IptagFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SctpFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildfireFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailServer

_Required_: No

_Type_: List of <a href="emailserver.md">EmailServer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

