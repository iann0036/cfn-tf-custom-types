# TF::AWS::KinesisFirehoseDeliveryStream SerializerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#orcserde" title="OrcSerDe">OrcSerDe</a>" : <i>[ <a href="orcserdedefinition.md">OrcSerDeDefinition</a>, ... ]</i>,
    "<a href="#parquetserde" title="ParquetSerDe">ParquetSerDe</a>" : <i>[ <a href="parquetserdedefinition.md">ParquetSerDeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#orcserde" title="OrcSerDe">OrcSerDe</a>: <i>
      - <a href="orcserdedefinition.md">OrcSerDeDefinition</a></i>
<a href="#parquetserde" title="ParquetSerDe">ParquetSerDe</a>: <i>
      - <a href="parquetserdedefinition.md">ParquetSerDeDefinition</a></i>
</pre>

## Properties

#### OrcSerDe

_Required_: No

_Type_: List of <a href="orcserdedefinition.md">OrcSerDeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParquetSerDe

_Required_: No

_Type_: List of <a href="parquetserdedefinition.md">ParquetSerDeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

