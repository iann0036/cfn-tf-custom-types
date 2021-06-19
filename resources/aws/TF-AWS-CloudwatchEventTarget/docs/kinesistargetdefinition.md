# TF::AWS::CloudwatchEventTarget KinesisTargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#partitionkeypath" title="PartitionKeyPath">PartitionKeyPath</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#partitionkeypath" title="PartitionKeyPath">PartitionKeyPath</a>: <i>String</i>
</pre>

## Properties

#### PartitionKeyPath

The JSON path to be extracted from the event and used as the partition key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

