# Terraform::AzureRM::DataLakeStore

CloudFormation equivalent of azurerm_data_lake_store

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::DataLakeStore",
    "Properties" : {
        "<a href="#encryptionstate" title="EncryptionState">EncryptionState</a>" : <i>String</i>,
        "<a href="#encryptiontype" title="EncryptionType">EncryptionType</a>" : <i>String</i>,
        "<a href="#firewallallowazureips" title="FirewallAllowAzureIps">FirewallAllowAzureIps</a>" : <i>String</i>,
        "<a href="#firewallstate" title="FirewallState">FirewallState</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::DataLakeStore
Properties:
    <a href="#encryptionstate" title="EncryptionState">EncryptionState</a>: <i>String</i>
    <a href="#encryptiontype" title="EncryptionType">EncryptionType</a>: <i>String</i>
    <a href="#firewallallowazureips" title="FirewallAllowAzureIps">FirewallAllowAzureIps</a>: <i>String</i>
    <a href="#firewallstate" title="FirewallState">FirewallState</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#tier" title="Tier">Tier</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### EncryptionState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallAllowAzureIps

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

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

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Endpoint

Returns the <code>Endpoint</code> value.
