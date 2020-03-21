# Terraform::Cloudflare::ZoneSettingsOverride

CloudFormation equivalent of cloudflare_zone_settings_override

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::ZoneSettingsOverride",
    "Properties" : {
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#settings" title="Settings">Settings</a>" : <i>[ <a href="settings.md">Settings</a>, ... ]</i>,
        "<a href="#minify" title="Minify">Minify</a>" : <i>[ <a href="minify.md">Minify</a>, ... ]</i>,
        "<a href="#mobileredirect" title="MobileRedirect">MobileRedirect</a>" : <i>[ <a href="mobileredirect.md">MobileRedirect</a>, ... ]</i>,
        "<a href="#securityheader" title="SecurityHeader">SecurityHeader</a>" : <i>[ <a href="securityheader.md">SecurityHeader</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::ZoneSettingsOverride
Properties:
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#settings" title="Settings">Settings</a>: <i>
      - <a href="settings.md">Settings</a></i>
    <a href="#minify" title="Minify">Minify</a>: <i>
      - <a href="minify.md">Minify</a></i>
    <a href="#mobileredirect" title="MobileRedirect">MobileRedirect</a>: <i>
      - <a href="mobileredirect.md">MobileRedirect</a></i>
    <a href="#securityheader" title="SecurityHeader">SecurityHeader</a>: <i>
      - <a href="securityheader.md">SecurityHeader</a></i>
</pre>

## Properties

#### ZoneId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

_Required_: No

_Type_: List of <a href="settings.md">Settings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Minify

_Required_: No

_Type_: List of <a href="minify.md">Minify</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MobileRedirect

_Required_: No

_Type_: List of <a href="mobileredirect.md">MobileRedirect</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityHeader

_Required_: No

_Type_: List of <a href="securityheader.md">SecurityHeader</a>

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

Returns the <code>InitialSettings</code> value.

#### InitialSettingsReadAt

Returns the <code>InitialSettingsReadAt</code> value.

#### ReadonlySettings

Returns the <code>ReadonlySettings</code> value.

#### ZoneStatus

Returns the <code>ZoneStatus</code> value.

#### ZoneType

Returns the <code>ZoneType</code> value.

