# Terraform::OCI::NosqlTable Schema

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#columns" title="Columns">Columns</a>" : <i>[ &lt;a href=&#34;schema-columns.md&#34;&gt;Columns&lt;/a&gt;, ... ]</i>,
    "<a href="#primarykey" title="PrimaryKey">PrimaryKey</a>" : <i>[ String, ... ]</i>,
    "<a href="#shardkey" title="ShardKey">ShardKey</a>" : <i>[ String, ... ]</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#columns" title="Columns">Columns</a>: <i>
      - &lt;a href=&#34;schema-columns.md&#34;&gt;Columns&lt;/a&gt;</i>
<a href="#primarykey" title="PrimaryKey">PrimaryKey</a>: <i>
      - String</i>
<a href="#shardkey" title="ShardKey">ShardKey</a>: <i>
      - String</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
</pre>

## Properties

#### Columns

_Required_: No
_Type_: List of &lt;a href=&#34;schema-columns.md&#34;&gt;Columns&lt;/a&gt;

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

