# Terraform::Panos::HttpServerProfile

This resource allows you to add/update/delete HTTP server profiles.

**Minimum PAN-OS version**:  7.1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::HttpServerProfile",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tagregistration" title="TagRegistration">TagRegistration</a>" : <i>Boolean</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#authformat" title="AuthFormat">AuthFormat</a>" : <i>[ <a href="authformat.md">AuthFormat</a>, ... ]</i>,
        "<a href="#configformat" title="ConfigFormat">ConfigFormat</a>" : <i>[ <a href="configformat.md">ConfigFormat</a>, ... ]</i>,
        "<a href="#dataformat" title="DataFormat">DataFormat</a>" : <i>[ <a href="dataformat.md">DataFormat</a>, ... ]</i>,
        "<a href="#gtpformat" title="GtpFormat">GtpFormat</a>" : <i>[ <a href="gtpformat.md">GtpFormat</a>, ... ]</i>,
        "<a href="#hipmatchformat" title="HipMatchFormat">HipMatchFormat</a>" : <i>[ <a href="hipmatchformat.md">HipMatchFormat</a>, ... ]</i>,
        "<a href="#httpserver" title="HttpServer">HttpServer</a>" : <i>[ <a href="httpserver.md">HttpServer</a>, ... ]</i>,
        "<a href="#iptagformat" title="IptagFormat">IptagFormat</a>" : <i>[ <a href="iptagformat.md">IptagFormat</a>, ... ]</i>,
        "<a href="#sctpformat" title="SctpFormat">SctpFormat</a>" : <i>[ <a href="sctpformat.md">SctpFormat</a>, ... ]</i>,
        "<a href="#systemformat" title="SystemFormat">SystemFormat</a>" : <i>[ <a href="systemformat.md">SystemFormat</a>, ... ]</i>,
        "<a href="#threatformat" title="ThreatFormat">ThreatFormat</a>" : <i>[ <a href="threatformat.md">ThreatFormat</a>, ... ]</i>,
        "<a href="#trafficformat" title="TrafficFormat">TrafficFormat</a>" : <i>[ <a href="trafficformat.md">TrafficFormat</a>, ... ]</i>,
        "<a href="#tunnelformat" title="TunnelFormat">TunnelFormat</a>" : <i>[ <a href="tunnelformat.md">TunnelFormat</a>, ... ]</i>,
        "<a href="#urlformat" title="UrlFormat">UrlFormat</a>" : <i>[ <a href="urlformat.md">UrlFormat</a>, ... ]</i>,
        "<a href="#useridformat" title="UserIdFormat">UserIdFormat</a>" : <i>[ <a href="useridformat.md">UserIdFormat</a>, ... ]</i>,
        "<a href="#wildfireformat" title="WildfireFormat">WildfireFormat</a>" : <i>[ <a href="wildfireformat.md">WildfireFormat</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::HttpServerProfile
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tagregistration" title="TagRegistration">TagRegistration</a>: <i>Boolean</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#authformat" title="AuthFormat">AuthFormat</a>: <i>
      - <a href="authformat.md">AuthFormat</a></i>
    <a href="#configformat" title="ConfigFormat">ConfigFormat</a>: <i>
      - <a href="configformat.md">ConfigFormat</a></i>
    <a href="#dataformat" title="DataFormat">DataFormat</a>: <i>
      - <a href="dataformat.md">DataFormat</a></i>
    <a href="#gtpformat" title="GtpFormat">GtpFormat</a>: <i>
      - <a href="gtpformat.md">GtpFormat</a></i>
    <a href="#hipmatchformat" title="HipMatchFormat">HipMatchFormat</a>: <i>
      - <a href="hipmatchformat.md">HipMatchFormat</a></i>
    <a href="#httpserver" title="HttpServer">HttpServer</a>: <i>
      - <a href="httpserver.md">HttpServer</a></i>
    <a href="#iptagformat" title="IptagFormat">IptagFormat</a>: <i>
      - <a href="iptagformat.md">IptagFormat</a></i>
    <a href="#sctpformat" title="SctpFormat">SctpFormat</a>: <i>
      - <a href="sctpformat.md">SctpFormat</a></i>
    <a href="#systemformat" title="SystemFormat">SystemFormat</a>: <i>
      - <a href="systemformat.md">SystemFormat</a></i>
    <a href="#threatformat" title="ThreatFormat">ThreatFormat</a>: <i>
      - <a href="threatformat.md">ThreatFormat</a></i>
    <a href="#trafficformat" title="TrafficFormat">TrafficFormat</a>: <i>
      - <a href="trafficformat.md">TrafficFormat</a></i>
    <a href="#tunnelformat" title="TunnelFormat">TunnelFormat</a>: <i>
      - <a href="tunnelformat.md">TunnelFormat</a></i>
    <a href="#urlformat" title="UrlFormat">UrlFormat</a>: <i>
      - <a href="urlformat.md">UrlFormat</a></i>
    <a href="#useridformat" title="UserIdFormat">UserIdFormat</a>: <i>
      - <a href="useridformat.md">UserIdFormat</a></i>
    <a href="#wildfireformat" title="WildfireFormat">WildfireFormat</a>: <i>
      - <a href="wildfireformat.md">WildfireFormat</a></i>
</pre>

## Properties

#### Name

The name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagRegistration

Perform tag registration.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys (default: `shared`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthFormat

_Required_: No

_Type_: List of <a href="authformat.md">AuthFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigFormat

_Required_: No

_Type_: List of <a href="configformat.md">ConfigFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFormat

_Required_: No

_Type_: List of <a href="dataformat.md">DataFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GtpFormat

_Required_: No

_Type_: List of <a href="gtpformat.md">GtpFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HipMatchFormat

_Required_: No

_Type_: List of <a href="hipmatchformat.md">HipMatchFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpServer

_Required_: No

_Type_: List of <a href="httpserver.md">HttpServer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IptagFormat

_Required_: No

_Type_: List of <a href="iptagformat.md">IptagFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SctpFormat

_Required_: No

_Type_: List of <a href="sctpformat.md">SctpFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemFormat

_Required_: No

_Type_: List of <a href="systemformat.md">SystemFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatFormat

_Required_: No

_Type_: List of <a href="threatformat.md">ThreatFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficFormat

_Required_: No

_Type_: List of <a href="trafficformat.md">TrafficFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelFormat

_Required_: No

_Type_: List of <a href="tunnelformat.md">TunnelFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFormat

_Required_: No

_Type_: List of <a href="urlformat.md">UrlFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdFormat

_Required_: No

_Type_: List of <a href="useridformat.md">UserIdFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildfireFormat

_Required_: No

_Type_: List of <a href="wildfireformat.md">WildfireFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### PasswordEnc

Returns the <code>PasswordEnc</code> value.

#### PasswordRaw

Returns the <code>PasswordRaw</code> value.

