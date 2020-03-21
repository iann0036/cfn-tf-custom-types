# Terraform::Google::AppEngineServiceSplitTraffic Split

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allocations" title="Allocations">Allocations</a>" : <i>[ &lt;a href=&#34;split-allocations.md&#34;&gt;Allocations&lt;/a&gt;, ... ]</i>,
    "<a href="#shardby" title="ShardBy">ShardBy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allocations" title="Allocations">Allocations</a>: <i>
      - &lt;a href=&#34;split-allocations.md&#34;&gt;Allocations&lt;/a&gt;</i>
<a href="#shardby" title="ShardBy">ShardBy</a>: <i>String</i>
</pre>

## Properties

#### Allocations

_Required_: Yes
_Type_: List of &lt;a href=&#34;split-allocations.md&#34;&gt;Allocations&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShardBy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

