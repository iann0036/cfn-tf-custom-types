# TF::AzureRM::CosmosdbTable AutoscaleSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxthroughput" title="MaxThroughput">MaxThroughput</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#maxthroughput" title="MaxThroughput">MaxThroughput</a>: <i>Double</i>
</pre>

## Properties

#### MaxThroughput

The maximum throughput of the Table (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

