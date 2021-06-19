# TF::GoogleBeta::GoogleAppEngineServiceSplitTraffic SplitDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allocations" title="Allocations">Allocations</a>" : <i>[ <a href="allocationsdefinition.md">AllocationsDefinition</a>, ... ]</i>,
    "<a href="#shardby" title="ShardBy">ShardBy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allocations" title="Allocations">Allocations</a>: <i>
      - <a href="allocationsdefinition.md">AllocationsDefinition</a></i>
<a href="#shardby" title="ShardBy">ShardBy</a>: <i>String</i>
</pre>

## Properties

#### Allocations

_Required_: Yes

_Type_: List of <a href="allocationsdefinition.md">AllocationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShardBy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

