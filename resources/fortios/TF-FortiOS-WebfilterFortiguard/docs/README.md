# TF::FortiOS::WebfilterFortiguard

Configure FortiGuard Web Filter service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WebfilterFortiguard",
    "Properties" : {
        "<a href="#cachemempercent" title="CacheMemPercent">CacheMemPercent</a>" : <i>Double</i>,
        "<a href="#cachemode" title="CacheMode">CacheMode</a>" : <i>String</i>,
        "<a href="#cacheprefixmatch" title="CachePrefixMatch">CachePrefixMatch</a>" : <i>String</i>,
        "<a href="#closeports" title="ClosePorts">ClosePorts</a>" : <i>String</i>,
        "<a href="#ovrdauthhttps" title="OvrdAuthHttps">OvrdAuthHttps</a>" : <i>String</i>,
        "<a href="#ovrdauthport" title="OvrdAuthPort">OvrdAuthPort</a>" : <i>Double</i>,
        "<a href="#ovrdauthporthttp" title="OvrdAuthPortHttp">OvrdAuthPortHttp</a>" : <i>Double</i>,
        "<a href="#ovrdauthporthttps" title="OvrdAuthPortHttps">OvrdAuthPortHttps</a>" : <i>Double</i>,
        "<a href="#ovrdauthporthttpsflow" title="OvrdAuthPortHttpsFlow">OvrdAuthPortHttpsFlow</a>" : <i>Double</i>,
        "<a href="#ovrdauthportwarning" title="OvrdAuthPortWarning">OvrdAuthPortWarning</a>" : <i>Double</i>,
        "<a href="#requestpacketsizelimit" title="RequestPacketSizeLimit">RequestPacketSizeLimit</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#warnauthhttps" title="WarnAuthHttps">WarnAuthHttps</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WebfilterFortiguard
Properties:
    <a href="#cachemempercent" title="CacheMemPercent">CacheMemPercent</a>: <i>Double</i>
    <a href="#cachemode" title="CacheMode">CacheMode</a>: <i>String</i>
    <a href="#cacheprefixmatch" title="CachePrefixMatch">CachePrefixMatch</a>: <i>String</i>
    <a href="#closeports" title="ClosePorts">ClosePorts</a>: <i>String</i>
    <a href="#ovrdauthhttps" title="OvrdAuthHttps">OvrdAuthHttps</a>: <i>String</i>
    <a href="#ovrdauthport" title="OvrdAuthPort">OvrdAuthPort</a>: <i>Double</i>
    <a href="#ovrdauthporthttp" title="OvrdAuthPortHttp">OvrdAuthPortHttp</a>: <i>Double</i>
    <a href="#ovrdauthporthttps" title="OvrdAuthPortHttps">OvrdAuthPortHttps</a>: <i>Double</i>
    <a href="#ovrdauthporthttpsflow" title="OvrdAuthPortHttpsFlow">OvrdAuthPortHttpsFlow</a>: <i>Double</i>
    <a href="#ovrdauthportwarning" title="OvrdAuthPortWarning">OvrdAuthPortWarning</a>: <i>Double</i>
    <a href="#requestpacketsizelimit" title="RequestPacketSizeLimit">RequestPacketSizeLimit</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#warnauthhttps" title="WarnAuthHttps">WarnAuthHttps</a>: <i>String</i>
</pre>

## Properties

#### CacheMemPercent

Maximum percentage of available memory allocated to caching (1 - 15%).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheMode

Cache entry expiration mode. Valid values: `ttl`, `db-ver`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CachePrefixMatch

Enable/disable prefix matching in the cache. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClosePorts

Close ports used for HTTP/HTTPS override authentication and disable user overrides. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdAuthHttps

Enable/disable use of HTTPS for override authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdAuthPort

Port to use for FortiGuard Web Filter override authentication.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdAuthPortHttp

Port to use for FortiGuard Web Filter HTTP override authentication.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdAuthPortHttps

Port to use for FortiGuard Web Filter HTTPS override authentication in proxy mode.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdAuthPortHttpsFlow

Port to use for FortiGuard Web Filter HTTPS override authentication in flow mode.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdAuthPortWarning

Port to use for FortiGuard Web Filter Warning override authentication.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPacketSizeLimit

Limit size of URL request packets sent to FortiGuard server (0 for default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarnAuthHttps

Enable/disable use of HTTPS for warning and authentication. Valid values: `enable`, `disable`.

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

