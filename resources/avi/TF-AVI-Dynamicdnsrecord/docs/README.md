# TF::AVI::Dynamicdnsrecord

The DynamicDnsRecord resource allows the creation and management of Avi DynamicDnsRecord

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Dynamicdnsrecord",
    "Properties" : {
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#delegated" title="Delegated">Delegated</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dnsvsuuid" title="DnsVsUuid">DnsVsUuid</a>" : <i>String</i>,
        "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#numrecordsinresponse" title="NumRecordsInResponse">NumRecordsInResponse</a>" : <i>Double</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#wildcardmatch" title="WildcardMatch">WildcardMatch</a>" : <i>Boolean</i>,
        "<a href="#cname" title="Cname">Cname</a>" : <i>[ <a href="cnamedefinition.md">CnameDefinition</a>, ... ]</i>,
        "<a href="#ip6address" title="Ip6Address">Ip6Address</a>" : <i>[ <a href="ip6addressdefinition.md">Ip6AddressDefinition</a>, ... ]</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>[ <a href="ipaddressdefinition.md">IpAddressDefinition</a>, ... ]</i>,
        "<a href="#mxrecords" title="MxRecords">MxRecords</a>" : <i>[ <a href="mxrecordsdefinition.md">MxRecordsDefinition</a>, ... ]</i>,
        "<a href="#ns" title="Ns">Ns</a>" : <i>[ <a href="nsdefinition.md">NsDefinition</a>, ... ]</i>,
        "<a href="#servicelocators" title="ServiceLocators">ServiceLocators</a>" : <i>[ <a href="servicelocatorsdefinition.md">ServiceLocatorsDefinition</a>, ... ]</i>,
        "<a href="#txtrecords" title="TxtRecords">TxtRecords</a>" : <i>[ <a href="txtrecordsdefinition.md">TxtRecordsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Dynamicdnsrecord
Properties:
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#delegated" title="Delegated">Delegated</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dnsvsuuid" title="DnsVsUuid">DnsVsUuid</a>: <i>String</i>
    <a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#numrecordsinresponse" title="NumRecordsInResponse">NumRecordsInResponse</a>: <i>Double</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#wildcardmatch" title="WildcardMatch">WildcardMatch</a>: <i>Boolean</i>
    <a href="#cname" title="Cname">Cname</a>: <i>
      - <a href="cnamedefinition.md">CnameDefinition</a></i>
    <a href="#ip6address" title="Ip6Address">Ip6Address</a>: <i>
      - <a href="ip6addressdefinition.md">Ip6AddressDefinition</a></i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>
      - <a href="ipaddressdefinition.md">IpAddressDefinition</a></i>
    <a href="#mxrecords" title="MxRecords">MxRecords</a>: <i>
      - <a href="mxrecordsdefinition.md">MxRecordsDefinition</a></i>
    <a href="#ns" title="Ns">Ns</a>: <i>
      - <a href="nsdefinition.md">NsDefinition</a></i>
    <a href="#servicelocators" title="ServiceLocators">ServiceLocators</a>: <i>
      - <a href="servicelocatorsdefinition.md">ServiceLocatorsDefinition</a></i>
    <a href="#txtrecords" title="TxtRecords">TxtRecords</a>: <i>
      - <a href="txtrecordsdefinition.md">TxtRecordsDefinition</a></i>
</pre>

## Properties

#### Algorithm

Specifies the algorithm to pick the ip address(es) to be returned,when multiple entries are configured. This does not apply if num_records_in_response is 0. Default is round-robin. Enum options - DNS_RECORD_RESPONSE_ROUND_ROBIN, DNS_RECORD_RESPONSE_CONSISTENT_HASH. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delegated

Configured fqdns are delegated domains (i.e. They represent a zone cut). Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Details of dns record. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsVsUuid

Uuid of the dns vs. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

Fully qualified domain name. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

Internal metadata for the dns record. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Dynamicdnsrecord name, needed for a top level uuid protobuf, for display in shell. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumRecordsInResponse

Specifies the number of records returned by the dns service.enter 0 to return all records. Default is 0. Allowed values are 0-20. Special values are 0- 'return all records'. Field introduced in 20.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

Tenant_uuid from dns vs's tenant_uuid. It is a reference to an object of type tenant. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

Time to live for this dns record. Field introduced in 20.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Dns record type. Enum options - DNS_RECORD_OTHER, DNS_RECORD_A, DNS_RECORD_NS, DNS_RECORD_CNAME, DNS_RECORD_SOA, DNS_RECORD_PTR, DNS_RECORD_HINFO, DNS_RECORD_MX, DNS_RECORD_TXT, DNS_RECORD_RP, DNS_RECORD_DNSKEY, DNS_RECORD_AAAA, DNS_RECORD_SRV, DNS_RECORD_OPT, DNS_RECORD_RRSIG, DNS_RECORD_AXFR, DNS_RECORD_ANY. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildcardMatch

Enable wild-card match of fqdn  if an exact match is not found in the dns table, the longest match is chosen by wild-carding the fqdn in the dns request. Default is false. Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cname

_Required_: No

_Type_: List of <a href="cnamedefinition.md">CnameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Address

_Required_: No

_Type_: List of <a href="ip6addressdefinition.md">Ip6AddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: List of <a href="ipaddressdefinition.md">IpAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MxRecords

_Required_: No

_Type_: List of <a href="mxrecordsdefinition.md">MxRecordsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ns

_Required_: No

_Type_: List of <a href="nsdefinition.md">NsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceLocators

_Required_: No

_Type_: List of <a href="servicelocatorsdefinition.md">ServiceLocatorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TxtRecords

_Required_: No

_Type_: List of <a href="txtrecordsdefinition.md">TxtRecordsDefinition</a>

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

