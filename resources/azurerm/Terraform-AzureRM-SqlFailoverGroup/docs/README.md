# Terraform::AzureRM::SqlFailoverGroup

Create a failover group of databases on a collection of Azure SQL servers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::SqlFailoverGroup",
    "Properties" : {
        "<a href="#databases" title="Databases">Databases</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#partnerservers" title="PartnerServers">PartnerServers</a>" : <i>[ <a href="partnerservers.md">PartnerServers</a>, ... ]</i>,
        "<a href="#readwriteendpointfailoverpolicy" title="ReadWriteEndpointFailoverPolicy">ReadWriteEndpointFailoverPolicy</a>" : <i>[ <a href="readwriteendpointfailoverpolicy.md">ReadWriteEndpointFailoverPolicy</a>, ... ]</i>,
        "<a href="#readonlyendpointfailoverpolicy" title="ReadonlyEndpointFailoverPolicy">ReadonlyEndpointFailoverPolicy</a>" : <i>[ <a href="readonlyendpointfailoverpolicy.md">ReadonlyEndpointFailoverPolicy</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::SqlFailoverGroup
Properties:
    <a href="#databases" title="Databases">Databases</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#partnerservers" title="PartnerServers">PartnerServers</a>: <i>
      - <a href="partnerservers.md">PartnerServers</a></i>
    <a href="#readwriteendpointfailoverpolicy" title="ReadWriteEndpointFailoverPolicy">ReadWriteEndpointFailoverPolicy</a>: <i>
      - <a href="readwriteendpointfailoverpolicy.md">ReadWriteEndpointFailoverPolicy</a></i>
    <a href="#readonlyendpointfailoverpolicy" title="ReadonlyEndpointFailoverPolicy">ReadonlyEndpointFailoverPolicy</a>: <i>
      - <a href="readonlyendpointfailoverpolicy.md">ReadonlyEndpointFailoverPolicy</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Databases

A list of database ids to add to the failover group.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the failover group. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group containing the SQL server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

The name of the primary SQL server. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartnerServers

_Required_: No

_Type_: List of <a href="partnerservers.md">PartnerServers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadWriteEndpointFailoverPolicy

_Required_: No

_Type_: List of <a href="readwriteendpointfailoverpolicy.md">ReadWriteEndpointFailoverPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadonlyEndpointFailoverPolicy

_Required_: No

_Type_: List of <a href="readonlyendpointfailoverpolicy.md">ReadonlyEndpointFailoverPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Location

Returns the <code>Location</code> value.

#### Role

Returns the <code>Role</code> value.

