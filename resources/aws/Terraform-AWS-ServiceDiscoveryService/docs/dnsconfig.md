# Terraform::AWS::ServiceDiscoveryService DnsConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#namespaceid" title="NamespaceId">NamespaceId</a>" : <i>String</i>,
    "<a href="#routingpolicy" title="RoutingPolicy">RoutingPolicy</a>" : <i>String</i>,
    "<a href="#dnsrecords" title="DnsRecords">DnsRecords</a>" : <i>[ <a href="dnsconfig-dnsrecords.md">DnsRecords</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#namespaceid" title="NamespaceId">NamespaceId</a>: <i>String</i>
<a href="#routingpolicy" title="RoutingPolicy">RoutingPolicy</a>: <i>String</i>
<a href="#dnsrecords" title="DnsRecords">DnsRecords</a>: <i>
      - <a href="dnsconfig-dnsrecords.md">DnsRecords</a></i>
</pre>

## Properties

#### NamespaceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsRecords

_Required_: No

_Type_: List of <a href="dnsconfig-dnsrecords.md">DnsRecords</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

