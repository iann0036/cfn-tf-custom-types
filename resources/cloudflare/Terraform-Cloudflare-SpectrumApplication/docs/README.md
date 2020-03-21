# Terraform::Cloudflare::SpectrumApplication

Provides a Cloudflare Spectrum Application. You can extend the power of Cloudflare's DDoS, TLS, and IP Firewall to your other TCP-based services.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::SpectrumApplication",
    "Properties" : {
        "<a href="#ipfirewall" title="IpFirewall">IpFirewall</a>" : <i>Boolean</i>,
        "<a href="#origindirect" title="OriginDirect">OriginDirect</a>" : <i>[ String, ... ]</i>,
        "<a href="#originport" title="OriginPort">OriginPort</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#proxyprotocol" title="ProxyProtocol">ProxyProtocol</a>" : <i>String</i>,
        "<a href="#tls" title="Tls">Tls</a>" : <i>String</i>,
        "<a href="#traffictype" title="TrafficType">TrafficType</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>[ <a href="dns.md">Dns</a>, ... ]</i>,
        "<a href="#origindns" title="OriginDns">OriginDns</a>" : <i>[ <a href="origindns.md">OriginDns</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::SpectrumApplication
Properties:
    <a href="#ipfirewall" title="IpFirewall">IpFirewall</a>: <i>Boolean</i>
    <a href="#origindirect" title="OriginDirect">OriginDirect</a>: <i>
      - String</i>
    <a href="#originport" title="OriginPort">OriginPort</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#proxyprotocol" title="ProxyProtocol">ProxyProtocol</a>: <i>String</i>
    <a href="#tls" title="Tls">Tls</a>: <i>String</i>
    <a href="#traffictype" title="TrafficType">TrafficType</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#dns" title="Dns">Dns</a>: <i>
      - <a href="dns.md">Dns</a></i>
    <a href="#origindns" title="OriginDns">OriginDns</a>: <i>
      - <a href="origindns.md">OriginDns</a></i>
</pre>

## Properties

#### IpFirewall

Enables the IP Firewall for this application. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginDirect

A list of destination addresses to the origin. e.g. `tcp://192.0.2.1:22`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginPort

If using `origin_dns` this is a required attribute. Origin port to proxy traffice to e.g. `22`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The port configuration at Cloudflare’s edge. e.g. `tcp/22`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyProtocol

Enables a proxy protocol to the origin. Valid values are: `off`, `v1`, `v2`, and `simple`. Defaults to `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

TLS configuration option for Cloudflare to connect to your origin. Valid values are: `off`, `flexible`, `full` and `strict`. Defaults to `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficType

Set's application type. Valid values are: `direct`, `http`, `https`.  Defaults to `direct`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The DNS zone ID to add the application to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: List of <a href="dns.md">Dns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginDns

_Required_: No

_Type_: List of <a href="origindns.md">OriginDns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

