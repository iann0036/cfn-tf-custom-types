# TF::AWS::KinesisFirehoseDeliveryStream DeserializerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hivejsonserde" title="HiveJsonSerDe">HiveJsonSerDe</a>" : <i>[ <a href="hivejsonserdedefinition.md">HiveJsonSerDeDefinition</a>, ... ]</i>,
    "<a href="#openxjsonserde" title="OpenXJsonSerDe">OpenXJsonSerDe</a>" : <i>[ <a href="openxjsonserdedefinition.md">OpenXJsonSerDeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hivejsonserde" title="HiveJsonSerDe">HiveJsonSerDe</a>: <i>
      - <a href="hivejsonserdedefinition.md">HiveJsonSerDeDefinition</a></i>
<a href="#openxjsonserde" title="OpenXJsonSerDe">OpenXJsonSerDe</a>: <i>
      - <a href="openxjsonserdedefinition.md">OpenXJsonSerDeDefinition</a></i>
</pre>

## Properties

#### HiveJsonSerDe

_Required_: No

_Type_: List of <a href="hivejsonserdedefinition.md">HiveJsonSerDeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenXJsonSerDe

_Required_: No

_Type_: List of <a href="openxjsonserdedefinition.md">OpenXJsonSerDeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

