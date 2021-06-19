# TF::AVI::Applicationprofile DnsServiceProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aaaaemptyresponse" title="AaaaEmptyResponse">AaaaEmptyResponse</a>" : <i>Boolean</i>,
    "<a href="#adminemail" title="AdminEmail">AdminEmail</a>" : <i>String</i>,
    "<a href="#dnsovertcpenabled" title="DnsOverTcpEnabled">DnsOverTcpEnabled</a>" : <i>Boolean</i>,
    "<a href="#domainnames" title="DomainNames">DomainNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#ecsstrippingenabled" title="EcsStrippingEnabled">EcsStrippingEnabled</a>" : <i>Boolean</i>,
    "<a href="#edns" title="Edns">Edns</a>" : <i>Boolean</i>,
    "<a href="#ednsclientsubnetprefixlen" title="EdnsClientSubnetPrefixLen">EdnsClientSubnetPrefixLen</a>" : <i>Double</i>,
    "<a href="#errorresponse" title="ErrorResponse">ErrorResponse</a>" : <i>String</i>,
    "<a href="#nameserver" title="NameServer">NameServer</a>" : <i>String</i>,
    "<a href="#negativecachingttl" title="NegativeCachingTtl">NegativeCachingTtl</a>" : <i>Double</i>,
    "<a href="#numdnsip" title="NumDnsIp">NumDnsIp</a>" : <i>Double</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
    "<a href="#dnszones" title="DnsZones">DnsZones</a>" : <i>[ <a href="dnszonesdefinition.md">DnsZonesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aaaaemptyresponse" title="AaaaEmptyResponse">AaaaEmptyResponse</a>: <i>Boolean</i>
<a href="#adminemail" title="AdminEmail">AdminEmail</a>: <i>String</i>
<a href="#dnsovertcpenabled" title="DnsOverTcpEnabled">DnsOverTcpEnabled</a>: <i>Boolean</i>
<a href="#domainnames" title="DomainNames">DomainNames</a>: <i>
      - String</i>
<a href="#ecsstrippingenabled" title="EcsStrippingEnabled">EcsStrippingEnabled</a>: <i>Boolean</i>
<a href="#edns" title="Edns">Edns</a>: <i>Boolean</i>
<a href="#ednsclientsubnetprefixlen" title="EdnsClientSubnetPrefixLen">EdnsClientSubnetPrefixLen</a>: <i>Double</i>
<a href="#errorresponse" title="ErrorResponse">ErrorResponse</a>: <i>String</i>
<a href="#nameserver" title="NameServer">NameServer</a>: <i>String</i>
<a href="#negativecachingttl" title="NegativeCachingTtl">NegativeCachingTtl</a>: <i>Double</i>
<a href="#numdnsip" title="NumDnsIp">NumDnsIp</a>: <i>Double</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
<a href="#dnszones" title="DnsZones">DnsZones</a>: <i>
      - <a href="dnszonesdefinition.md">DnsZonesDefinition</a></i>
</pre>

## Properties

#### AaaaEmptyResponse

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsOverTcpEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsStrippingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Edns

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdnsClientSubnetPrefixLen

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorResponse

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegativeCachingTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumDnsIp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsZones

_Required_: No

_Type_: List of <a href="dnszonesdefinition.md">DnsZonesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

