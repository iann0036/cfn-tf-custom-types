# TF::AWS::KinesisAnalyticsApplication OutputsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>" : <i>[ <a href="kinesisfirehosedefinition.md">KinesisFirehoseDefinition</a>, ... ]</i>,
    "<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>" : <i>[ <a href="kinesisstreamdefinition.md">KinesisStreamDefinition</a>, ... ]</i>,
    "<a href="#lambda" title="Lambda">Lambda</a>" : <i>[ <a href="lambdadefinition.md">LambdaDefinition</a>, ... ]</i>,
    "<a href="#schema" title="Schema">Schema</a>" : <i>[ <a href="schemadefinition.md">SchemaDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>: <i>
      - <a href="kinesisfirehosedefinition.md">KinesisFirehoseDefinition</a></i>
<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>: <i>
      - <a href="kinesisstreamdefinition.md">KinesisStreamDefinition</a></i>
<a href="#lambda" title="Lambda">Lambda</a>: <i>
      - <a href="lambdadefinition.md">LambdaDefinition</a></i>
<a href="#schema" title="Schema">Schema</a>: <i>
      - <a href="schemadefinition.md">SchemaDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisFirehose

_Required_: No

_Type_: List of <a href="kinesisfirehosedefinition.md">KinesisFirehoseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisStream

_Required_: No

_Type_: List of <a href="kinesisstreamdefinition.md">KinesisStreamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lambda

_Required_: No

_Type_: List of <a href="lambdadefinition.md">LambdaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: List of <a href="schemadefinition.md">SchemaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

