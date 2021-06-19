# TF::FortiOS::UserSetting

Configure user authentication setting.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::UserSetting",
    "Properties" : {
        "<a href="#authblackouttime" title="AuthBlackoutTime">AuthBlackoutTime</a>" : <i>Double</i>,
        "<a href="#authcacert" title="AuthCaCert">AuthCaCert</a>" : <i>String</i>,
        "<a href="#authcert" title="AuthCert">AuthCert</a>" : <i>String</i>,
        "<a href="#authhttpbasic" title="AuthHttpBasic">AuthHttpBasic</a>" : <i>String</i>,
        "<a href="#authinvalidmax" title="AuthInvalidMax">AuthInvalidMax</a>" : <i>Double</i>,
        "<a href="#authlockoutduration" title="AuthLockoutDuration">AuthLockoutDuration</a>" : <i>Double</i>,
        "<a href="#authlockoutthreshold" title="AuthLockoutThreshold">AuthLockoutThreshold</a>" : <i>Double</i>,
        "<a href="#authondemand" title="AuthOnDemand">AuthOnDemand</a>" : <i>String</i>,
        "<a href="#authportaltimeout" title="AuthPortalTimeout">AuthPortalTimeout</a>" : <i>Double</i>,
        "<a href="#authsecurehttp" title="AuthSecureHttp">AuthSecureHttp</a>" : <i>String</i>,
        "<a href="#authsrcmac" title="AuthSrcMac">AuthSrcMac</a>" : <i>String</i>,
        "<a href="#authsslallowrenegotiation" title="AuthSslAllowRenegotiation">AuthSslAllowRenegotiation</a>" : <i>String</i>,
        "<a href="#authsslminprotoversion" title="AuthSslMinProtoVersion">AuthSslMinProtoVersion</a>" : <i>String</i>,
        "<a href="#authtimeout" title="AuthTimeout">AuthTimeout</a>" : <i>Double</i>,
        "<a href="#authtimeouttype" title="AuthTimeoutType">AuthTimeoutType</a>" : <i>String</i>,
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#perpolicydisclaimer" title="PerPolicyDisclaimer">PerPolicyDisclaimer</a>" : <i>String</i>,
        "<a href="#radiussestimeoutact" title="RadiusSesTimeoutAct">RadiusSesTimeoutAct</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#authports" title="AuthPorts">AuthPorts</a>" : <i>[ <a href="authportsdefinition.md">AuthPortsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::UserSetting
Properties:
    <a href="#authblackouttime" title="AuthBlackoutTime">AuthBlackoutTime</a>: <i>Double</i>
    <a href="#authcacert" title="AuthCaCert">AuthCaCert</a>: <i>String</i>
    <a href="#authcert" title="AuthCert">AuthCert</a>: <i>String</i>
    <a href="#authhttpbasic" title="AuthHttpBasic">AuthHttpBasic</a>: <i>String</i>
    <a href="#authinvalidmax" title="AuthInvalidMax">AuthInvalidMax</a>: <i>Double</i>
    <a href="#authlockoutduration" title="AuthLockoutDuration">AuthLockoutDuration</a>: <i>Double</i>
    <a href="#authlockoutthreshold" title="AuthLockoutThreshold">AuthLockoutThreshold</a>: <i>Double</i>
    <a href="#authondemand" title="AuthOnDemand">AuthOnDemand</a>: <i>String</i>
    <a href="#authportaltimeout" title="AuthPortalTimeout">AuthPortalTimeout</a>: <i>Double</i>
    <a href="#authsecurehttp" title="AuthSecureHttp">AuthSecureHttp</a>: <i>String</i>
    <a href="#authsrcmac" title="AuthSrcMac">AuthSrcMac</a>: <i>String</i>
    <a href="#authsslallowrenegotiation" title="AuthSslAllowRenegotiation">AuthSslAllowRenegotiation</a>: <i>String</i>
    <a href="#authsslminprotoversion" title="AuthSslMinProtoVersion">AuthSslMinProtoVersion</a>: <i>String</i>
    <a href="#authtimeout" title="AuthTimeout">AuthTimeout</a>: <i>Double</i>
    <a href="#authtimeouttype" title="AuthTimeoutType">AuthTimeoutType</a>: <i>String</i>
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#perpolicydisclaimer" title="PerPolicyDisclaimer">PerPolicyDisclaimer</a>: <i>String</i>
    <a href="#radiussestimeoutact" title="RadiusSesTimeoutAct">RadiusSesTimeoutAct</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#authports" title="AuthPorts">AuthPorts</a>: <i>
      - <a href="authportsdefinition.md">AuthPortsDefinition</a></i>
</pre>

## Properties

#### AuthBlackoutTime

Time in seconds an IP address is denied access after failing to authenticate five times within one minute.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthCaCert

HTTPS CA certificate for policy authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthCert

HTTPS server certificate for policy authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthHttpBasic

Enable/disable use of HTTP basic authentication for identity-based firewall policies. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthInvalidMax

Maximum number of failed authentication attempts before the user is blocked.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthLockoutDuration

Lockout period in seconds after too many login failures.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthLockoutThreshold

Maximum number of failed login attempts before login lockout is triggered.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthOnDemand

Always/implicitly trigger firewall authentication on demand. Valid values: `always`, `implicitly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPortalTimeout

Time in minutes before captive portal user have to re-authenticate (1 - 30 min, default 3 min).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSecureHttp

Enable/disable redirecting HTTP user authentication to more secure HTTPS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSrcMac

Enable/disable source MAC for user identity. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSslAllowRenegotiation

Allow/forbid SSL re-negotiation for HTTPS authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSslMinProtoVersion

Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). Valid values: `default`, `SSLv3`, `TLSv1`, `TLSv1-1`, `TLSv1-2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthTimeout

Time in minutes before the firewall user authentication timeout requires the user to re-authenticate.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthTimeoutType

Control if authenticated users have to login again after a hard timeout, after an idle timeout, or after a session timeout. Valid values: `idle-timeout`, `hard-timeout`, `new-session`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

Supported firewall policy authentication protocols/methods. Valid values: `http`, `https`, `ftp`, `telnet`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerPolicyDisclaimer

Enable/disable per policy disclaimer. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusSesTimeoutAct

Set the RADIUS session timeout to a hard timeout or to ignore RADIUS server session timeouts. Valid values: `hard-timeout`, `ignore-timeout`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPorts

_Required_: No

_Type_: List of <a href="authportsdefinition.md">AuthPortsDefinition</a>

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

