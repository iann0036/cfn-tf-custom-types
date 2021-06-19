# TF::NetAppCloudManager::CifsServer

CloudFormation equivalent of netapp-cloudmanager_cifs_server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::CifsServer",
    "Properties" : {
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#dnsdomain" title="DnsDomain">DnsDomain</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#isworkgroup" title="IsWorkgroup">IsWorkgroup</a>" : <i>Boolean</i>,
        "<a href="#netbios" title="Netbios">Netbios</a>" : <i>String</i>,
        "<a href="#organizationalunit" title="OrganizationalUnit">OrganizationalUnit</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#svmname" title="SvmName">SvmName</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#workgroupname" title="WorkgroupName">WorkgroupName</a>" : <i>String</i>,
        "<a href="#workingenvironmentid" title="WorkingEnvironmentId">WorkingEnvironmentId</a>" : <i>String</i>,
        "<a href="#workingenvironmentname" title="WorkingEnvironmentName">WorkingEnvironmentName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::CifsServer
Properties:
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#dnsdomain" title="DnsDomain">DnsDomain</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#ipaddresses" title="IpAddresses">IpAddresses</a>: <i>
      - String</i>
    <a href="#isworkgroup" title="IsWorkgroup">IsWorkgroup</a>: <i>Boolean</i>
    <a href="#netbios" title="Netbios">Netbios</a>: <i>String</i>
    <a href="#organizationalunit" title="OrganizationalUnit">OrganizationalUnit</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#svmname" title="SvmName">SvmName</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#workgroupname" title="WorkgroupName">WorkgroupName</a>: <i>String</i>
    <a href="#workingenvironmentid" title="WorkingEnvironmentId">WorkingEnvironmentId</a>: <i>String</i>
    <a href="#workingenvironmentname" title="WorkingEnvironmentName">WorkingEnvironmentName</a>: <i>String</i>
</pre>

## Properties

#### ClientId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsWorkgroup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netbios

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationalUnit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvmName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkgroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingEnvironmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingEnvironmentName

_Required_: No

_Type_: String

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

