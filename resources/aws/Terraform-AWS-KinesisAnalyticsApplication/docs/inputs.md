# Terraform::AWS::KinesisAnalyticsApplication Inputs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
    "<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>" : <i>[ <a href="inputs-kinesisfirehose.md">KinesisFirehose</a>, ... ]</i>,
    "<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>" : <i>[ <a href="inputs-kinesisstream.md">KinesisStream</a>, ... ]</i>,
    "<a href="#parallelism" title="Parallelism">Parallelism</a>" : <i>[ <a href="inputs-parallelism.md">Parallelism</a>, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="inputs-processingconfiguration.md">ProcessingConfiguration</a>, ... ]</i>,
    "<a href="#schema" title="Schema">Schema</a>" : <i>[ <a href="inputs-schema.md">Schema</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>: <i>
      - <a href="inputs-kinesisfirehose.md">KinesisFirehose</a></i>
<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>: <i>
      - <a href="inputs-kinesisstream.md">KinesisStream</a></i>
<a href="#parallelism" title="Parallelism">Parallelism</a>: <i>
      - <a href="inputs-parallelism.md">Parallelism</a></i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="inputs-processingconfiguration.md">ProcessingConfiguration</a></i>
<a href="#schema" title="Schema">Schema</a>: <i>
      - <a href="inputs-schema.md">Schema</a></i>
</pre>

## Properties

#### NamePrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisFirehose

_Required_: No

_Type_: List of <a href="inputs-kinesisfirehose.md">KinesisFirehose</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisStream

_Required_: No

_Type_: List of <a href="inputs-kinesisstream.md">KinesisStream</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parallelism

_Required_: No

_Type_: List of <a href="inputs-parallelism.md">Parallelism</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of <a href="inputs-processingconfiguration.md">ProcessingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: List of <a href="inputs-schema.md">Schema</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

