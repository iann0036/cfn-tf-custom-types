# TF::AzureRM::HpcCache DirectoryActiveDirectoryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cachenetbiosname" title="CacheNetbiosName">CacheNetbiosName</a>" : <i>String</i>,
    "<a href="#dnsprimaryip" title="DnsPrimaryIp">DnsPrimaryIp</a>" : <i>String</i>,
    "<a href="#dnssecondaryip" title="DnsSecondaryIp">DnsSecondaryIp</a>" : <i>String</i>,
    "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
    "<a href="#domainnetbiosname" title="DomainNetbiosName">DomainNetbiosName</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cachenetbiosname" title="CacheNetbiosName">CacheNetbiosName</a>: <i>String</i>
<a href="#dnsprimaryip" title="DnsPrimaryIp">DnsPrimaryIp</a>: <i>String</i>
<a href="#dnssecondaryip" title="DnsSecondaryIp">DnsSecondaryIp</a>: <i>String</i>
<a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
<a href="#domainnetbiosname" title="DomainNetbiosName">DomainNetbiosName</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### CacheNetbiosName

The NetBIOS name to assign to the HPC Cache when it joins the Active Directory domain as a server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsPrimaryIp

The primary DNS IP address used to resolve the Active Directory domain controller's FQDN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSecondaryIp

The secondary DNS IP address used to resolve the Active Directory domain controller's FQDN.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

The fully qualified domain name of the Active Directory domain controller.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainNetbiosName

The Active Directory domain's NetBIOS name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password of the Active Directory domain administrator.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The username of the Active Directory domain administrator.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

