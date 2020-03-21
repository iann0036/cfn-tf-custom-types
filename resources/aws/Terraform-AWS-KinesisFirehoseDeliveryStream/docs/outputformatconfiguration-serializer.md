# Terraform::AWS::KinesisFirehoseDeliveryStream OutputFormatConfiguration Serializer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#orcserde" title="OrcSerDe">OrcSerDe</a>" : <i>[ <a href="outputformatconfiguration-serializer-orcserde.md">OrcSerDe</a>, ... ]</i>,
    "<a href="#parquetserde" title="ParquetSerDe">ParquetSerDe</a>" : <i>[ <a href="outputformatconfiguration-serializer-parquetserde.md">ParquetSerDe</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#orcserde" title="OrcSerDe">OrcSerDe</a>: <i>
      - <a href="outputformatconfiguration-serializer-orcserde.md">OrcSerDe</a></i>
<a href="#parquetserde" title="ParquetSerDe">ParquetSerDe</a>: <i>
      - <a href="outputformatconfiguration-serializer-parquetserde.md">ParquetSerDe</a></i>
</pre>

## Properties

#### OrcSerDe

_Required_: No

_Type_: List of <a href="outputformatconfiguration-serializer-orcserde.md">OrcSerDe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParquetSerDe

_Required_: No

_Type_: List of <a href="outputformatconfiguration-serializer-parquetserde.md">ParquetSerDe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

