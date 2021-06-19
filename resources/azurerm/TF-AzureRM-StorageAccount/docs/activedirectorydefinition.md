# TF::AzureRM::StorageAccount ActiveDirectoryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domainguid" title="DomainGuid">DomainGuid</a>" : <i>String</i>,
    "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
    "<a href="#domainsid" title="DomainSid">DomainSid</a>" : <i>String</i>,
    "<a href="#forestname" title="ForestName">ForestName</a>" : <i>String</i>,
    "<a href="#netbiosdomainname" title="NetbiosDomainName">NetbiosDomainName</a>" : <i>String</i>,
    "<a href="#storagesid" title="StorageSid">StorageSid</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#domainguid" title="DomainGuid">DomainGuid</a>: <i>String</i>
<a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
<a href="#domainsid" title="DomainSid">DomainSid</a>: <i>String</i>
<a href="#forestname" title="ForestName">ForestName</a>: <i>String</i>
<a href="#netbiosdomainname" title="NetbiosDomainName">NetbiosDomainName</a>: <i>String</i>
<a href="#storagesid" title="StorageSid">StorageSid</a>: <i>String</i>
</pre>

## Properties

#### DomainGuid

Specifies the domain GUID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

Specifies the primary domain that the AD DNS server is authoritative for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainSid

Specifies the security identifier (SID).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForestName

Specifies the Active Directory forest.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetbiosDomainName

Specifies the NetBIOS domain name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageSid

Specifies the security identifier (SID) for Azure Storage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

