# TF::OCI::NosqlTable SchemaDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#columns" title="Columns">Columns</a>" : <i>[ <a href="schemadefinition.md">SchemaDefinition</a>, ... ]</i>,
    "<a href="#primarykey" title="PrimaryKey">PrimaryKey</a>" : <i>[ String, ... ]</i>,
    "<a href="#shardkey" title="ShardKey">ShardKey</a>" : <i>[ String, ... ]</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#columns" title="Columns">Columns</a>: <i>
      - <a href="schemadefinition.md">SchemaDefinition</a></i>
<a href="#primarykey" title="PrimaryKey">PrimaryKey</a>: <i>
      - String</i>
<a href="#shardkey" title="ShardKey">ShardKey</a>: <i>
      - String</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
</pre>

## Properties

#### Columns

_Required_: No

_Type_: List of <a href="schemadefinition.md">SchemaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryKey

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShardKey

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

