# Terraform::AzureRM::CosmosdbAccount Capabilities

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Name

The capability to enable - Possible values are `EnableAggregationPipeline`, `EnableCassandra`, `EnableGremlin`,`EnableMongo`, `EnableTable`, `MongoDBv3.4`, and `mongoEnableDocLevelTTL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

