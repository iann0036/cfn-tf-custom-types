# TF::AVI::Ipamdnsproviderprofile InternalProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsvirtualserviceref" title="DnsVirtualserviceRef">DnsVirtualserviceRef</a>" : <i>String</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
    "<a href="#dnsservicedomain" title="DnsServiceDomain">DnsServiceDomain</a>" : <i>[ <a href="dnsservicedomaindefinition.md">DnsServiceDomainDefinition</a>, ... ]</i>,
    "<a href="#usablenetworks" title="UsableNetworks">UsableNetworks</a>" : <i>[ <a href="usablenetworksdefinition.md">UsableNetworksDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsvirtualserviceref" title="DnsVirtualserviceRef">DnsVirtualserviceRef</a>: <i>String</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
<a href="#dnsservicedomain" title="DnsServiceDomain">DnsServiceDomain</a>: <i>
      - <a href="dnsservicedomaindefinition.md">DnsServiceDomainDefinition</a></i>
<a href="#usablenetworks" title="UsableNetworks">UsableNetworks</a>: <i>
      - <a href="usablenetworksdefinition.md">UsableNetworksDefinition</a></i>
</pre>

## Properties

#### DnsVirtualserviceRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServiceDomain

_Required_: No

_Type_: List of <a href="dnsservicedomaindefinition.md">DnsServiceDomainDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableNetworks

_Required_: No

_Type_: List of <a href="usablenetworksdefinition.md">UsableNetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

