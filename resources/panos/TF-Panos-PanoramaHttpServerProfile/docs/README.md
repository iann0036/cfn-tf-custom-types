# TF::Panos::PanoramaHttpServerProfile

This resource allows you to add/update/delete Panorama HTTP server profiles.

**Minimum PAN-OS version**:  7.1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::PanoramaHttpServerProfile",
    "Properties" : {
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tagregistration" title="TagRegistration">TagRegistration</a>" : <i>Boolean</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#authformat" title="AuthFormat">AuthFormat</a>" : <i>[ <a href="authformatdefinition.md">AuthFormatDefinition</a>, ... ]</i>,
        "<a href="#configformat" title="ConfigFormat">ConfigFormat</a>" : <i>[ <a href="configformatdefinition.md">ConfigFormatDefinition</a>, ... ]</i>,
        "<a href="#dataformat" title="DataFormat">DataFormat</a>" : <i>[ <a href="dataformatdefinition.md">DataFormatDefinition</a>, ... ]</i>,
        "<a href="#gtpformat" title="GtpFormat">GtpFormat</a>" : <i>[ <a href="gtpformatdefinition.md">GtpFormatDefinition</a>, ... ]</i>,
        "<a href="#hipmatchformat" title="HipMatchFormat">HipMatchFormat</a>" : <i>[ <a href="hipmatchformatdefinition.md">HipMatchFormatDefinition</a>, ... ]</i>,
        "<a href="#httpserver" title="HttpServer">HttpServer</a>" : <i>[ <a href="httpserverdefinition.md">HttpServerDefinition</a>, ... ]</i>,
        "<a href="#iptagformat" title="IptagFormat">IptagFormat</a>" : <i>[ <a href="iptagformatdefinition.md">IptagFormatDefinition</a>, ... ]</i>,
        "<a href="#sctpformat" title="SctpFormat">SctpFormat</a>" : <i>[ <a href="sctpformatdefinition.md">SctpFormatDefinition</a>, ... ]</i>,
        "<a href="#systemformat" title="SystemFormat">SystemFormat</a>" : <i>[ <a href="systemformatdefinition.md">SystemFormatDefinition</a>, ... ]</i>,
        "<a href="#threatformat" title="ThreatFormat">ThreatFormat</a>" : <i>[ <a href="threatformatdefinition.md">ThreatFormatDefinition</a>, ... ]</i>,
        "<a href="#trafficformat" title="TrafficFormat">TrafficFormat</a>" : <i>[ <a href="trafficformatdefinition.md">TrafficFormatDefinition</a>, ... ]</i>,
        "<a href="#tunnelformat" title="TunnelFormat">TunnelFormat</a>" : <i>[ <a href="tunnelformatdefinition.md">TunnelFormatDefinition</a>, ... ]</i>,
        "<a href="#urlformat" title="UrlFormat">UrlFormat</a>" : <i>[ <a href="urlformatdefinition.md">UrlFormatDefinition</a>, ... ]</i>,
        "<a href="#useridformat" title="UserIdFormat">UserIdFormat</a>" : <i>[ <a href="useridformatdefinition.md">UserIdFormatDefinition</a>, ... ]</i>,
        "<a href="#wildfireformat" title="WildfireFormat">WildfireFormat</a>" : <i>[ <a href="wildfireformatdefinition.md">WildfireFormatDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::PanoramaHttpServerProfile
Properties:
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tagregistration" title="TagRegistration">TagRegistration</a>: <i>Boolean</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#authformat" title="AuthFormat">AuthFormat</a>: <i>
      - <a href="authformatdefinition.md">AuthFormatDefinition</a></i>
    <a href="#configformat" title="ConfigFormat">ConfigFormat</a>: <i>
      - <a href="configformatdefinition.md">ConfigFormatDefinition</a></i>
    <a href="#dataformat" title="DataFormat">DataFormat</a>: <i>
      - <a href="dataformatdefinition.md">DataFormatDefinition</a></i>
    <a href="#gtpformat" title="GtpFormat">GtpFormat</a>: <i>
      - <a href="gtpformatdefinition.md">GtpFormatDefinition</a></i>
    <a href="#hipmatchformat" title="HipMatchFormat">HipMatchFormat</a>: <i>
      - <a href="hipmatchformatdefinition.md">HipMatchFormatDefinition</a></i>
    <a href="#httpserver" title="HttpServer">HttpServer</a>: <i>
      - <a href="httpserverdefinition.md">HttpServerDefinition</a></i>
    <a href="#iptagformat" title="IptagFormat">IptagFormat</a>: <i>
      - <a href="iptagformatdefinition.md">IptagFormatDefinition</a></i>
    <a href="#sctpformat" title="SctpFormat">SctpFormat</a>: <i>
      - <a href="sctpformatdefinition.md">SctpFormatDefinition</a></i>
    <a href="#systemformat" title="SystemFormat">SystemFormat</a>: <i>
      - <a href="systemformatdefinition.md">SystemFormatDefinition</a></i>
    <a href="#threatformat" title="ThreatFormat">ThreatFormat</a>: <i>
      - <a href="threatformatdefinition.md">ThreatFormatDefinition</a></i>
    <a href="#trafficformat" title="TrafficFormat">TrafficFormat</a>: <i>
      - <a href="trafficformatdefinition.md">TrafficFormatDefinition</a></i>
    <a href="#tunnelformat" title="TunnelFormat">TunnelFormat</a>: <i>
      - <a href="tunnelformatdefinition.md">TunnelFormatDefinition</a></i>
    <a href="#urlformat" title="UrlFormat">UrlFormat</a>: <i>
      - <a href="urlformatdefinition.md">UrlFormatDefinition</a></i>
    <a href="#useridformat" title="UserIdFormat">UserIdFormat</a>: <i>
      - <a href="useridformatdefinition.md">UserIdFormatDefinition</a></i>
    <a href="#wildfireformat" title="WildfireFormat">WildfireFormat</a>: <i>
      - <a href="wildfireformatdefinition.md">WildfireFormatDefinition</a></i>
</pre>

## Properties

#### DeviceGroup

The device group location.  Mutually exclusive with
`template` and `template_stack`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Vsys

The vsys.  This will likely be `shared`, and it should be
defined if you specified either `template` or `template_stack`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthFormat

_Required_: No

_Type_: List of <a href="authformatdefinition.md">AuthFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigFormat

_Required_: No

_Type_: List of <a href="configformatdefinition.md">ConfigFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFormat

_Required_: No

_Type_: List of <a href="dataformatdefinition.md">DataFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GtpFormat

_Required_: No

_Type_: List of <a href="gtpformatdefinition.md">GtpFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HipMatchFormat

_Required_: No

_Type_: List of <a href="hipmatchformatdefinition.md">HipMatchFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpServer

_Required_: No

_Type_: List of <a href="httpserverdefinition.md">HttpServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IptagFormat

_Required_: No

_Type_: List of <a href="iptagformatdefinition.md">IptagFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SctpFormat

_Required_: No

_Type_: List of <a href="sctpformatdefinition.md">SctpFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemFormat

_Required_: No

_Type_: List of <a href="systemformatdefinition.md">SystemFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatFormat

_Required_: No

_Type_: List of <a href="threatformatdefinition.md">ThreatFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficFormat

_Required_: No

_Type_: List of <a href="trafficformatdefinition.md">TrafficFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelFormat

_Required_: No

_Type_: List of <a href="tunnelformatdefinition.md">TunnelFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFormat

_Required_: No

_Type_: List of <a href="urlformatdefinition.md">UrlFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdFormat

_Required_: No

_Type_: List of <a href="useridformatdefinition.md">UserIdFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildfireFormat

_Required_: No

_Type_: List of <a href="wildfireformatdefinition.md">WildfireFormatDefinition</a>

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

