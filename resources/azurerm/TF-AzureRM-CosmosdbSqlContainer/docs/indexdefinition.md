# TF::AzureRM::CosmosdbSqlContainer IndexDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#order" title="Order">Order</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#order" title="Order">Order</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### Order

Order of the index. Possible values are `Ascending` or `Descending`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Path for which the indexing behaviour applies to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

