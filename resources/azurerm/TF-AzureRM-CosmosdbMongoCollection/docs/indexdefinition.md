# TF::AzureRM::CosmosdbMongoCollection IndexDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keys" title="Keys">Keys</a>" : <i>[ String, ... ]</i>,
    "<a href="#unique" title="Unique">Unique</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#keys" title="Keys">Keys</a>: <i>
      - String</i>
<a href="#unique" title="Unique">Unique</a>: <i>Boolean</i>
</pre>

## Properties

#### Keys

Specifies the list of user settable keys for each Cosmos DB Mongo Collection.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unique

Is the index unique or not? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
