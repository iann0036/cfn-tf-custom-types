# Terraform::AzureRM::SqlFailoverGroup

CloudFormation equivalent of azurerm_sql_failover_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::SqlFailoverGroup",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#databases" title="Databases">Databases</a>" : <i>[ String, ... ]</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#partnerservers" title="PartnerServers">PartnerServers</a>" : <i>[ &lt;a href=&#34;partnerservers.md&#34;&gt;PartnerServers&lt;/a&gt;, ... ]</i>,
        "<a href="#readwriteendpointfailoverpolicy" title="ReadWriteEndpointFailoverPolicy">ReadWriteEndpointFailoverPolicy</a>" : <i>[ &lt;a href=&#34;readwriteendpointfailoverpolicy.md&#34;&gt;ReadWriteEndpointFailoverPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#readonlyendpointfailoverpolicy" title="ReadonlyEndpointFailoverPolicy">ReadonlyEndpointFailoverPolicy</a>" : <i>[ &lt;a href=&#34;readonlyendpointfailoverpolicy.md&#34;&gt;ReadonlyEndpointFailoverPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::SqlFailoverGroup
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#databases" title="Databases">Databases</a>: <i>
      - String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#partnerservers" title="PartnerServers">PartnerServers</a>: <i>
      - &lt;a href=&#34;partnerservers.md&#34;&gt;PartnerServers&lt;/a&gt;</i>
    <a href="#readwriteendpointfailoverpolicy" title="ReadWriteEndpointFailoverPolicy">ReadWriteEndpointFailoverPolicy</a>: <i>
      - &lt;a href=&#34;readwriteendpointfailoverpolicy.md&#34;&gt;ReadWriteEndpointFailoverPolicy&lt;/a&gt;</i>
    <a href="#readonlyendpointfailoverpolicy" title="ReadonlyEndpointFailoverPolicy">ReadonlyEndpointFailoverPolicy</a>: <i>
      - &lt;a href=&#34;readonlyendpointfailoverpolicy.md&#34;&gt;ReadonlyEndpointFailoverPolicy&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Databases

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartnerServers

_Required_: No

_Type_: List of &lt;a href=&#34;partnerservers.md&#34;&gt;PartnerServers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadWriteEndpointFailoverPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;readwriteendpointfailoverpolicy.md&#34;&gt;ReadWriteEndpointFailoverPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadonlyEndpointFailoverPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;readonlyendpointfailoverpolicy.md&#34;&gt;ReadonlyEndpointFailoverPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Location

Returns the &lt;code&gt;Location&lt;/code&gt; value.

#### Role

Returns the &lt;code&gt;Role&lt;/code&gt; value.

