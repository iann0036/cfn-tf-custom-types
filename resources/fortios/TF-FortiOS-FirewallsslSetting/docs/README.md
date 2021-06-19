# TF::FortiOS::FirewallsslSetting

SSL proxy settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallsslSetting",
    "Properties" : {
        "<a href="#abbreviatehandshake" title="AbbreviateHandshake">AbbreviateHandshake</a>" : <i>String</i>,
        "<a href="#certcachecapacity" title="CertCacheCapacity">CertCacheCapacity</a>" : <i>Double</i>,
        "<a href="#certcachetimeout" title="CertCacheTimeout">CertCacheTimeout</a>" : <i>Double</i>,
        "<a href="#kxpqueuethreshold" title="KxpQueueThreshold">KxpQueueThreshold</a>" : <i>Double</i>,
        "<a href="#nomatchingcipheraction" title="NoMatchingCipherAction">NoMatchingCipherAction</a>" : <i>String</i>,
        "<a href="#proxyconnecttimeout" title="ProxyConnectTimeout">ProxyConnectTimeout</a>" : <i>Double</i>,
        "<a href="#sessioncachecapacity" title="SessionCacheCapacity">SessionCacheCapacity</a>" : <i>Double</i>,
        "<a href="#sessioncachetimeout" title="SessionCacheTimeout">SessionCacheTimeout</a>" : <i>Double</i>,
        "<a href="#ssldhbits" title="SslDhBits">SslDhBits</a>" : <i>String</i>,
        "<a href="#sslqueuethreshold" title="SslQueueThreshold">SslQueueThreshold</a>" : <i>Double</i>,
        "<a href="#sslsendemptyfrags" title="SslSendEmptyFrags">SslSendEmptyFrags</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallsslSetting
Properties:
    <a href="#abbreviatehandshake" title="AbbreviateHandshake">AbbreviateHandshake</a>: <i>String</i>
    <a href="#certcachecapacity" title="CertCacheCapacity">CertCacheCapacity</a>: <i>Double</i>
    <a href="#certcachetimeout" title="CertCacheTimeout">CertCacheTimeout</a>: <i>Double</i>
    <a href="#kxpqueuethreshold" title="KxpQueueThreshold">KxpQueueThreshold</a>: <i>Double</i>
    <a href="#nomatchingcipheraction" title="NoMatchingCipherAction">NoMatchingCipherAction</a>: <i>String</i>
    <a href="#proxyconnecttimeout" title="ProxyConnectTimeout">ProxyConnectTimeout</a>: <i>Double</i>
    <a href="#sessioncachecapacity" title="SessionCacheCapacity">SessionCacheCapacity</a>: <i>Double</i>
    <a href="#sessioncachetimeout" title="SessionCacheTimeout">SessionCacheTimeout</a>: <i>Double</i>
    <a href="#ssldhbits" title="SslDhBits">SslDhBits</a>: <i>String</i>
    <a href="#sslqueuethreshold" title="SslQueueThreshold">SslQueueThreshold</a>: <i>Double</i>
    <a href="#sslsendemptyfrags" title="SslSendEmptyFrags">SslSendEmptyFrags</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AbbreviateHandshake

Enable/disable use of SSL abbreviated handshake. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertCacheCapacity

Maximum capacity of the host certificate cache (0 - 500, default = 200).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertCacheTimeout

Time limit to keep certificate cache (1 - 120 min, default = 10).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KxpQueueThreshold

Maximum length of the CP KXP queue. When the queue becomes full, the proxy switches cipher functions to the main CPU (0 - 512, default = 16).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoMatchingCipherAction

Bypass or drop the connection when no matching cipher is found. Valid values: `bypass`, `drop`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyConnectTimeout

Time limit to make an internal connection to the appropriate proxy process (1 - 60 sec, default = 30).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionCacheCapacity

Capacity of the SSL session cache (--Obsolete--) (1 - 1000, default = 500).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionCacheTimeout

Time limit to keep SSL session state (1 - 60 min, default = 20).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslDhBits

Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048). Valid values: `768`, `1024`, `1536`, `2048`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslQueueThreshold

Maximum length of the CP SSL queue. When the queue becomes full, the proxy switches cipher functions to the main CPU (0 - 512, default = 32).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSendEmptyFrags

Enable/disable sending empty fragments to avoid attack on CBC IV (for SSL 3.0 and TLS 1.0 only). Valid values: `enable`, `disable`.

_Required_: Yes

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

