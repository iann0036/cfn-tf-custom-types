# TF::AVI::Virtualservice StaticDnsRecordsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
    "<a href="#delegated" title="Delegated">Delegated</a>" : <i>Boolean</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>[ String, ... ]</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>String</i>,
    "<a href="#numrecordsinresponse" title="NumRecordsInResponse">NumRecordsInResponse</a>" : <i>Double</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#wildcardmatch" title="WildcardMatch">WildcardMatch</a>" : <i>Boolean</i>,
    "<a href="#cname" title="Cname">Cname</a>" : <i>[ <a href="cnamedefinition.md">CnameDefinition</a>, ... ]</i>,
    "<a href="#ip6address" title="Ip6Address">Ip6Address</a>" : <i>[ <a href="ip6addressdefinition.md">Ip6AddressDefinition</a>, ... ]</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>[ <a href="ipaddressdefinition.md">IpAddressDefinition</a>, ... ]</i>,
    "<a href="#mxrecords" title="MxRecords">MxRecords</a>" : <i>[ <a href="mxrecordsdefinition.md">MxRecordsDefinition</a>, ... ]</i>,
    "<a href="#ns" title="Ns">Ns</a>" : <i>[ <a href="nsdefinition.md">NsDefinition</a>, ... ]</i>,
    "<a href="#servicelocator" title="ServiceLocator">ServiceLocator</a>" : <i>[ <a href="servicelocatordefinition.md">ServiceLocatorDefinition</a>, ... ]</i>,
    "<a href="#txtrecords" title="TxtRecords">TxtRecords</a>" : <i>[ <a href="txtrecordsdefinition.md">TxtRecordsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
<a href="#delegated" title="Delegated">Delegated</a>: <i>Boolean</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#fqdn" title="Fqdn">Fqdn</a>: <i>
      - String</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>String</i>
<a href="#numrecordsinresponse" title="NumRecordsInResponse">NumRecordsInResponse</a>: <i>Double</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
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
<a href="#servicelocator" title="ServiceLocator">ServiceLocator</a>: <i>
      - <a href="servicelocatordefinition.md">ServiceLocatorDefinition</a></i>
<a href="#txtrecords" title="TxtRecords">TxtRecords</a>: <i>
      - <a href="txtrecordsdefinition.md">TxtRecordsDefinition</a></i>
</pre>

## Properties

#### Algorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delegated

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumRecordsInResponse

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildcardMatch

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

#### ServiceLocator

_Required_: No

_Type_: List of <a href="servicelocatordefinition.md">ServiceLocatorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TxtRecords

_Required_: No

_Type_: List of <a href="txtrecordsdefinition.md">TxtRecordsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

