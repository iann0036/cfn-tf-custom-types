# Terraform::AWS::KinesisFirehoseDeliveryStream DataFormatConversionConfiguration OutputFormatConfiguration Serializer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#orcserde" title="OrcSerDe">OrcSerDe</a>" : <i>[ &lt;a href=&#34;dataformatconversionconfiguration-outputformatconfiguration-serializer-orcserde.md&#34;&gt;OrcSerDe&lt;/a&gt;, ... ]</i>,
    "<a href="#parquetserde" title="ParquetSerDe">ParquetSerDe</a>" : <i>[ &lt;a href=&#34;dataformatconversionconfiguration-outputformatconfiguration-serializer-parquetserde.md&#34;&gt;ParquetSerDe&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#orcserde" title="OrcSerDe">OrcSerDe</a>: <i>
      - &lt;a href=&#34;dataformatconversionconfiguration-outputformatconfiguration-serializer-orcserde.md&#34;&gt;OrcSerDe&lt;/a&gt;</i>
<a href="#parquetserde" title="ParquetSerDe">ParquetSerDe</a>: <i>
      - &lt;a href=&#34;dataformatconversionconfiguration-outputformatconfiguration-serializer-parquetserde.md&#34;&gt;ParquetSerDe&lt;/a&gt;</i>
</pre>

## Properties

#### OrcSerDe

_Required_: No
_Type_: List of &lt;a href=&#34;dataformatconversionconfiguration-outputformatconfiguration-serializer-orcserde.md&#34;&gt;OrcSerDe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParquetSerDe

_Required_: No
_Type_: List of &lt;a href=&#34;dataformatconversionconfiguration-outputformatconfiguration-serializer-parquetserde.md&#34;&gt;ParquetSerDe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

