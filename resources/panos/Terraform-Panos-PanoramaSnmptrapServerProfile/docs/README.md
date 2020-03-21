# Terraform::Panos::PanoramaSnmptrapServerProfile

CloudFormation equivalent of panos_panorama_snmptrap_server_profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaSnmptrapServerProfile",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#authpasswordenc" title="AuthPasswordEnc">AuthPasswordEnc</a>" : <i>[ &lt;a href=&#34;authpasswordenc.md&#34;&gt;AuthPasswordEnc&lt;/a&gt;, ... ]</i>,
        "<a href="#authpasswordraw" title="AuthPasswordRaw">AuthPasswordRaw</a>" : <i>[ &lt;a href=&#34;authpasswordraw.md&#34;&gt;AuthPasswordRaw&lt;/a&gt;, ... ]</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privpasswordenc" title="PrivPasswordEnc">PrivPasswordEnc</a>" : <i>[ &lt;a href=&#34;privpasswordenc.md&#34;&gt;PrivPasswordEnc&lt;/a&gt;, ... ]</i>,
        "<a href="#privpasswordraw" title="PrivPasswordRaw">PrivPasswordRaw</a>" : <i>[ &lt;a href=&#34;privpasswordraw.md&#34;&gt;PrivPasswordRaw&lt;/a&gt;, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#v2cserver" title="V2cServer">V2cServer</a>" : <i>[ &lt;a href=&#34;v2cserver.md&#34;&gt;V2cServer&lt;/a&gt;, ... ]</i>,
        "<a href="#v3server" title="V3Server">V3Server</a>" : <i>[ &lt;a href=&#34;v3server.md&#34;&gt;V3Server&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaSnmptrapServerProfile
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#authpasswordenc" title="AuthPasswordEnc">AuthPasswordEnc</a>: <i>
      - &lt;a href=&#34;authpasswordenc.md&#34;&gt;AuthPasswordEnc&lt;/a&gt;</i>
    <a href="#authpasswordraw" title="AuthPasswordRaw">AuthPasswordRaw</a>: <i>
      - &lt;a href=&#34;authpasswordraw.md&#34;&gt;AuthPasswordRaw&lt;/a&gt;</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privpasswordenc" title="PrivPasswordEnc">PrivPasswordEnc</a>: <i>
      - &lt;a href=&#34;privpasswordenc.md&#34;&gt;PrivPasswordEnc&lt;/a&gt;</i>
    <a href="#privpasswordraw" title="PrivPasswordRaw">PrivPasswordRaw</a>: <i>
      - &lt;a href=&#34;privpasswordraw.md&#34;&gt;PrivPasswordRaw&lt;/a&gt;</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#v2cserver" title="V2cServer">V2cServer</a>: <i>
      - &lt;a href=&#34;v2cserver.md&#34;&gt;V2cServer&lt;/a&gt;</i>
    <a href="#v3server" title="V3Server">V3Server</a>: <i>
      - &lt;a href=&#34;v3server.md&#34;&gt;V3Server&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPasswordEnc

_Required_: No

_Type_: List of &lt;a href=&#34;authpasswordenc.md&#34;&gt;AuthPasswordEnc&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPasswordRaw

_Required_: No

_Type_: List of &lt;a href=&#34;authpasswordraw.md&#34;&gt;AuthPasswordRaw&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivPasswordEnc

_Required_: No

_Type_: List of &lt;a href=&#34;privpasswordenc.md&#34;&gt;PrivPasswordEnc&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivPasswordRaw

_Required_: No

_Type_: List of &lt;a href=&#34;privpasswordraw.md&#34;&gt;PrivPasswordRaw&lt;/a&gt;

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

#### V2cServer

_Required_: No

_Type_: List of &lt;a href=&#34;v2cserver.md&#34;&gt;V2cServer&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V3Server

_Required_: No

_Type_: List of &lt;a href=&#34;v3server.md&#34;&gt;V3Server&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AuthPasswordEnc

Returns the &lt;code&gt;AuthPasswordEnc&lt;/code&gt; value.

#### AuthPasswordRaw

Returns the &lt;code&gt;AuthPasswordRaw&lt;/code&gt; value.

#### PrivPasswordEnc

Returns the &lt;code&gt;PrivPasswordEnc&lt;/code&gt; value.

#### PrivPasswordRaw

Returns the &lt;code&gt;PrivPasswordRaw&lt;/code&gt; value.

