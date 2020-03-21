# Terraform::Cloudflare::ZoneSettingsOverride

CloudFormation equivalent of cloudflare_zone_settings_override

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::ZoneSettingsOverride",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#initialsettings" title="InitialSettings">InitialSettings</a>" : <i>[ &lt;a href=&#34;initialsettings.md&#34;&gt;InitialSettings&lt;/a&gt;, ... ]</i>,
        "<a href="#initialsettingsreadat" title="InitialSettingsReadAt">InitialSettingsReadAt</a>" : <i>String</i>,
        "<a href="#readonlysettings" title="ReadonlySettings">ReadonlySettings</a>" : <i>[ String, ... ]</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#zonestatus" title="ZoneStatus">ZoneStatus</a>" : <i>String</i>,
        "<a href="#zonetype" title="ZoneType">ZoneType</a>" : <i>String</i>,
        "<a href="#settings" title="Settings">Settings</a>" : <i>[ &lt;a href=&#34;settings.md&#34;&gt;Settings&lt;/a&gt;, ... ]</i>,
        "<a href="#minify" title="Minify">Minify</a>" : <i>[ &lt;a href=&#34;minify.md&#34;&gt;Minify&lt;/a&gt;, ... ]</i>,
        "<a href="#mobileredirect" title="MobileRedirect">MobileRedirect</a>" : <i>[ &lt;a href=&#34;mobileredirect.md&#34;&gt;MobileRedirect&lt;/a&gt;, ... ]</i>,
        "<a href="#securityheader" title="SecurityHeader">SecurityHeader</a>" : <i>[ &lt;a href=&#34;securityheader.md&#34;&gt;SecurityHeader&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::ZoneSettingsOverride
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#initialsettings" title="InitialSettings">InitialSettings</a>: <i>
      - &lt;a href=&#34;initialsettings.md&#34;&gt;InitialSettings&lt;/a&gt;</i>
    <a href="#initialsettingsreadat" title="InitialSettingsReadAt">InitialSettingsReadAt</a>: <i>String</i>
    <a href="#readonlysettings" title="ReadonlySettings">ReadonlySettings</a>: <i>
      - String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#zonestatus" title="ZoneStatus">ZoneStatus</a>: <i>String</i>
    <a href="#zonetype" title="ZoneType">ZoneType</a>: <i>String</i>
    <a href="#settings" title="Settings">Settings</a>: <i>
      - &lt;a href=&#34;settings.md&#34;&gt;Settings&lt;/a&gt;</i>
    <a href="#minify" title="Minify">Minify</a>: <i>
      - &lt;a href=&#34;minify.md&#34;&gt;Minify&lt;/a&gt;</i>
    <a href="#mobileredirect" title="MobileRedirect">MobileRedirect</a>: <i>
      - &lt;a href=&#34;mobileredirect.md&#34;&gt;MobileRedirect&lt;/a&gt;</i>
    <a href="#securityheader" title="SecurityHeader">SecurityHeader</a>: <i>
      - &lt;a href=&#34;securityheader.md&#34;&gt;SecurityHeader&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialSettings

_Required_: No

_Type_: List of &lt;a href=&#34;initialsettings.md&#34;&gt;InitialSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialSettingsReadAt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadonlySettings

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

_Required_: No

_Type_: List of &lt;a href=&#34;settings.md&#34;&gt;Settings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Minify

_Required_: No

_Type_: List of &lt;a href=&#34;minify.md&#34;&gt;Minify&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MobileRedirect

_Required_: No

_Type_: List of &lt;a href=&#34;mobileredirect.md&#34;&gt;MobileRedirect&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityHeader

_Required_: No

_Type_: List of &lt;a href=&#34;securityheader.md&#34;&gt;SecurityHeader&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### InitialSettings

Returns the &lt;code&gt;InitialSettings&lt;/code&gt; value.

#### InitialSettingsReadAt

Returns the &lt;code&gt;InitialSettingsReadAt&lt;/code&gt; value.

#### ReadonlySettings

Returns the &lt;code&gt;ReadonlySettings&lt;/code&gt; value.

#### ZoneStatus

Returns the &lt;code&gt;ZoneStatus&lt;/code&gt; value.

#### ZoneType

Returns the &lt;code&gt;ZoneType&lt;/code&gt; value.

