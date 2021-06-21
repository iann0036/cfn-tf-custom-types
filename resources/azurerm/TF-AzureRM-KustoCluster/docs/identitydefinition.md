# TF::AzureRM::KustoCluster IdentityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#identityids" title="IdentityIds">IdentityIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#identityids" title="IdentityIds">IdentityIds</a>: <i>
      - String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### IdentityIds

A list of IDs for User Assigned Managed Identity resources to be assigned.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies the type of Managed Service Identity that is configured on this Kusto Cluster. Possible values are: `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
