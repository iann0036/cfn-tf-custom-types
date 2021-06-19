# TF::AVI::Ipamdnsproviderprofile InfobloxProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsview" title="DnsView">DnsView</a>" : <i>String</i>,
    "<a href="#networkview" title="NetworkView">NetworkView</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#usabledomains" title="UsableDomains">UsableDomains</a>" : <i>[ String, ... ]</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#wapiversion" title="WapiVersion">WapiVersion</a>" : <i>String</i>,
    "<a href="#extensibleattributes" title="ExtensibleAttributes">ExtensibleAttributes</a>" : <i>[ <a href="extensibleattributesdefinition.md">ExtensibleAttributesDefinition</a>, ... ]</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>[ <a href="ipaddressdefinition.md">IpAddressDefinition</a>, ... ]</i>,
    "<a href="#usableallocsubnets" title="UsableAllocSubnets">UsableAllocSubnets</a>" : <i>[ <a href="usableallocsubnetsdefinition.md">UsableAllocSubnetsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsview" title="DnsView">DnsView</a>: <i>String</i>
<a href="#networkview" title="NetworkView">NetworkView</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#usabledomains" title="UsableDomains">UsableDomains</a>: <i>
      - String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#wapiversion" title="WapiVersion">WapiVersion</a>: <i>String</i>
<a href="#extensibleattributes" title="ExtensibleAttributes">ExtensibleAttributes</a>: <i>
      - <a href="extensibleattributesdefinition.md">ExtensibleAttributesDefinition</a></i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>
      - <a href="ipaddressdefinition.md">IpAddressDefinition</a></i>
<a href="#usableallocsubnets" title="UsableAllocSubnets">UsableAllocSubnets</a>: <i>
      - <a href="usableallocsubnetsdefinition.md">UsableAllocSubnetsDefinition</a></i>
</pre>

## Properties

#### DnsView

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkView

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WapiVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtensibleAttributes

_Required_: No

_Type_: List of <a href="extensibleattributesdefinition.md">ExtensibleAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: List of <a href="ipaddressdefinition.md">IpAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableAllocSubnets

_Required_: No

_Type_: List of <a href="usableallocsubnetsdefinition.md">UsableAllocSubnetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

