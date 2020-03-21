# Terraform::Panos::PanoramaHttpServerProfile

CloudFormation equivalent of panos_panorama_http_server_profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaHttpServerProfile",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#passwordenc" title="PasswordEnc">PasswordEnc</a>" : <i>[ &lt;a href=&#34;passwordenc.md&#34;&gt;PasswordEnc&lt;/a&gt;, ... ]</i>,
        "<a href="#passwordraw" title="PasswordRaw">PasswordRaw</a>" : <i>[ &lt;a href=&#34;passwordraw.md&#34;&gt;PasswordRaw&lt;/a&gt;, ... ]</i>,
        "<a href="#tagregistration" title="TagRegistration">TagRegistration</a>" : <i>Boolean</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#authformat" title="AuthFormat">AuthFormat</a>" : <i>[ &lt;a href=&#34;authformat.md&#34;&gt;AuthFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#configformat" title="ConfigFormat">ConfigFormat</a>" : <i>[ &lt;a href=&#34;configformat.md&#34;&gt;ConfigFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#dataformat" title="DataFormat">DataFormat</a>" : <i>[ &lt;a href=&#34;dataformat.md&#34;&gt;DataFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#gtpformat" title="GtpFormat">GtpFormat</a>" : <i>[ &lt;a href=&#34;gtpformat.md&#34;&gt;GtpFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#hipmatchformat" title="HipMatchFormat">HipMatchFormat</a>" : <i>[ &lt;a href=&#34;hipmatchformat.md&#34;&gt;HipMatchFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#httpserver" title="HttpServer">HttpServer</a>" : <i>[ &lt;a href=&#34;httpserver.md&#34;&gt;HttpServer&lt;/a&gt;, ... ]</i>,
        "<a href="#iptagformat" title="IptagFormat">IptagFormat</a>" : <i>[ &lt;a href=&#34;iptagformat.md&#34;&gt;IptagFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#sctpformat" title="SctpFormat">SctpFormat</a>" : <i>[ &lt;a href=&#34;sctpformat.md&#34;&gt;SctpFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#systemformat" title="SystemFormat">SystemFormat</a>" : <i>[ &lt;a href=&#34;systemformat.md&#34;&gt;SystemFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#threatformat" title="ThreatFormat">ThreatFormat</a>" : <i>[ &lt;a href=&#34;threatformat.md&#34;&gt;ThreatFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#trafficformat" title="TrafficFormat">TrafficFormat</a>" : <i>[ &lt;a href=&#34;trafficformat.md&#34;&gt;TrafficFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#tunnelformat" title="TunnelFormat">TunnelFormat</a>" : <i>[ &lt;a href=&#34;tunnelformat.md&#34;&gt;TunnelFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#urlformat" title="UrlFormat">UrlFormat</a>" : <i>[ &lt;a href=&#34;urlformat.md&#34;&gt;UrlFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#useridformat" title="UserIdFormat">UserIdFormat</a>" : <i>[ &lt;a href=&#34;useridformat.md&#34;&gt;UserIdFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#wildfireformat" title="WildfireFormat">WildfireFormat</a>" : <i>[ &lt;a href=&#34;wildfireformat.md&#34;&gt;WildfireFormat&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaHttpServerProfile
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#passwordenc" title="PasswordEnc">PasswordEnc</a>: <i>
      - &lt;a href=&#34;passwordenc.md&#34;&gt;PasswordEnc&lt;/a&gt;</i>
    <a href="#passwordraw" title="PasswordRaw">PasswordRaw</a>: <i>
      - &lt;a href=&#34;passwordraw.md&#34;&gt;PasswordRaw&lt;/a&gt;</i>
    <a href="#tagregistration" title="TagRegistration">TagRegistration</a>: <i>Boolean</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#authformat" title="AuthFormat">AuthFormat</a>: <i>
      - &lt;a href=&#34;authformat.md&#34;&gt;AuthFormat&lt;/a&gt;</i>
    <a href="#configformat" title="ConfigFormat">ConfigFormat</a>: <i>
      - &lt;a href=&#34;configformat.md&#34;&gt;ConfigFormat&lt;/a&gt;</i>
    <a href="#dataformat" title="DataFormat">DataFormat</a>: <i>
      - &lt;a href=&#34;dataformat.md&#34;&gt;DataFormat&lt;/a&gt;</i>
    <a href="#gtpformat" title="GtpFormat">GtpFormat</a>: <i>
      - &lt;a href=&#34;gtpformat.md&#34;&gt;GtpFormat&lt;/a&gt;</i>
    <a href="#hipmatchformat" title="HipMatchFormat">HipMatchFormat</a>: <i>
      - &lt;a href=&#34;hipmatchformat.md&#34;&gt;HipMatchFormat&lt;/a&gt;</i>
    <a href="#httpserver" title="HttpServer">HttpServer</a>: <i>
      - &lt;a href=&#34;httpserver.md&#34;&gt;HttpServer&lt;/a&gt;</i>
    <a href="#iptagformat" title="IptagFormat">IptagFormat</a>: <i>
      - &lt;a href=&#34;iptagformat.md&#34;&gt;IptagFormat&lt;/a&gt;</i>
    <a href="#sctpformat" title="SctpFormat">SctpFormat</a>: <i>
      - &lt;a href=&#34;sctpformat.md&#34;&gt;SctpFormat&lt;/a&gt;</i>
    <a href="#systemformat" title="SystemFormat">SystemFormat</a>: <i>
      - &lt;a href=&#34;systemformat.md&#34;&gt;SystemFormat&lt;/a&gt;</i>
    <a href="#threatformat" title="ThreatFormat">ThreatFormat</a>: <i>
      - &lt;a href=&#34;threatformat.md&#34;&gt;ThreatFormat&lt;/a&gt;</i>
    <a href="#trafficformat" title="TrafficFormat">TrafficFormat</a>: <i>
      - &lt;a href=&#34;trafficformat.md&#34;&gt;TrafficFormat&lt;/a&gt;</i>
    <a href="#tunnelformat" title="TunnelFormat">TunnelFormat</a>: <i>
      - &lt;a href=&#34;tunnelformat.md&#34;&gt;TunnelFormat&lt;/a&gt;</i>
    <a href="#urlformat" title="UrlFormat">UrlFormat</a>: <i>
      - &lt;a href=&#34;urlformat.md&#34;&gt;UrlFormat&lt;/a&gt;</i>
    <a href="#useridformat" title="UserIdFormat">UserIdFormat</a>: <i>
      - &lt;a href=&#34;useridformat.md&#34;&gt;UserIdFormat&lt;/a&gt;</i>
    <a href="#wildfireformat" title="WildfireFormat">WildfireFormat</a>: <i>
      - &lt;a href=&#34;wildfireformat.md&#34;&gt;WildfireFormat&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordEnc

_Required_: No

_Type_: List of &lt;a href=&#34;passwordenc.md&#34;&gt;PasswordEnc&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordRaw

_Required_: No

_Type_: List of &lt;a href=&#34;passwordraw.md&#34;&gt;PasswordRaw&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagRegistration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthFormat

_Required_: No

_Type_: List of &lt;a href=&#34;authformat.md&#34;&gt;AuthFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigFormat

_Required_: No

_Type_: List of &lt;a href=&#34;configformat.md&#34;&gt;ConfigFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFormat

_Required_: No

_Type_: List of &lt;a href=&#34;dataformat.md&#34;&gt;DataFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GtpFormat

_Required_: No

_Type_: List of &lt;a href=&#34;gtpformat.md&#34;&gt;GtpFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HipMatchFormat

_Required_: No

_Type_: List of &lt;a href=&#34;hipmatchformat.md&#34;&gt;HipMatchFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpServer

_Required_: No

_Type_: List of &lt;a href=&#34;httpserver.md&#34;&gt;HttpServer&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IptagFormat

_Required_: No

_Type_: List of &lt;a href=&#34;iptagformat.md&#34;&gt;IptagFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SctpFormat

_Required_: No

_Type_: List of &lt;a href=&#34;sctpformat.md&#34;&gt;SctpFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemFormat

_Required_: No

_Type_: List of &lt;a href=&#34;systemformat.md&#34;&gt;SystemFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatFormat

_Required_: No

_Type_: List of &lt;a href=&#34;threatformat.md&#34;&gt;ThreatFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficFormat

_Required_: No

_Type_: List of &lt;a href=&#34;trafficformat.md&#34;&gt;TrafficFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelFormat

_Required_: No

_Type_: List of &lt;a href=&#34;tunnelformat.md&#34;&gt;TunnelFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFormat

_Required_: No

_Type_: List of &lt;a href=&#34;urlformat.md&#34;&gt;UrlFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdFormat

_Required_: No

_Type_: List of &lt;a href=&#34;useridformat.md&#34;&gt;UserIdFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildfireFormat

_Required_: No

_Type_: List of &lt;a href=&#34;wildfireformat.md&#34;&gt;WildfireFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### PasswordEnc

Returns the &lt;code&gt;PasswordEnc&lt;/code&gt; value.

#### PasswordRaw

Returns the &lt;code&gt;PasswordRaw&lt;/code&gt; value.

