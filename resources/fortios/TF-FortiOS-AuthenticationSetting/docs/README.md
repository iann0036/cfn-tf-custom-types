# TF::FortiOS::AuthenticationSetting

Configure authentication setting.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::AuthenticationSetting",
    "Properties" : {
        "<a href="#activeauthscheme" title="ActiveAuthScheme">ActiveAuthScheme</a>" : <i>String</i>,
        "<a href="#authhttps" title="AuthHttps">AuthHttps</a>" : <i>String</i>,
        "<a href="#captiveportal" title="CaptivePortal">CaptivePortal</a>" : <i>String</i>,
        "<a href="#captiveportal6" title="CaptivePortal6">CaptivePortal6</a>" : <i>String</i>,
        "<a href="#captiveportalip" title="CaptivePortalIp">CaptivePortalIp</a>" : <i>String</i>,
        "<a href="#captiveportalip6" title="CaptivePortalIp6">CaptivePortalIp6</a>" : <i>String</i>,
        "<a href="#captiveportalport" title="CaptivePortalPort">CaptivePortalPort</a>" : <i>Double</i>,
        "<a href="#captiveportalsslport" title="CaptivePortalSslPort">CaptivePortalSslPort</a>" : <i>Double</i>,
        "<a href="#captiveportaltype" title="CaptivePortalType">CaptivePortalType</a>" : <i>String</i>,
        "<a href="#ssoauthscheme" title="SsoAuthScheme">SsoAuthScheme</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::AuthenticationSetting
Properties:
    <a href="#activeauthscheme" title="ActiveAuthScheme">ActiveAuthScheme</a>: <i>String</i>
    <a href="#authhttps" title="AuthHttps">AuthHttps</a>: <i>String</i>
    <a href="#captiveportal" title="CaptivePortal">CaptivePortal</a>: <i>String</i>
    <a href="#captiveportal6" title="CaptivePortal6">CaptivePortal6</a>: <i>String</i>
    <a href="#captiveportalip" title="CaptivePortalIp">CaptivePortalIp</a>: <i>String</i>
    <a href="#captiveportalip6" title="CaptivePortalIp6">CaptivePortalIp6</a>: <i>String</i>
    <a href="#captiveportalport" title="CaptivePortalPort">CaptivePortalPort</a>: <i>Double</i>
    <a href="#captiveportalsslport" title="CaptivePortalSslPort">CaptivePortalSslPort</a>: <i>Double</i>
    <a href="#captiveportaltype" title="CaptivePortalType">CaptivePortalType</a>: <i>String</i>
    <a href="#ssoauthscheme" title="SsoAuthScheme">SsoAuthScheme</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### ActiveAuthScheme

Active authentication method (scheme name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthHttps

Enable/disable redirecting HTTP user authentication to HTTPS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortal

Captive portal host name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortal6

IPv6 captive portal host name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalIp

Captive portal IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalIp6

Captive portal IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalPort

Captive portal port number (1 - 65535, default = 7830).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalSslPort

Captive portal SSL port number (1 - 65535, default = 7831).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalType

Captive portal type. Valid values: `fqdn`, `ip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoAuthScheme

Single-Sign-On authentication method (scheme name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

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

