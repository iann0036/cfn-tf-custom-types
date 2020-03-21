# Terraform::AzureRM::TrafficManagerProfile DnsConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#relativename" title="RelativeName">RelativeName</a>" : <i>String</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#relativename" title="RelativeName">RelativeName</a>: <i>String</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
</pre>

## Properties

#### RelativeName

The relative domain name, this is combined with the domain name used by Traffic Manager to form the FQDN which is exported as documented below. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

The TTL value of the Profile used by Local DNS resolvers and clients.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

