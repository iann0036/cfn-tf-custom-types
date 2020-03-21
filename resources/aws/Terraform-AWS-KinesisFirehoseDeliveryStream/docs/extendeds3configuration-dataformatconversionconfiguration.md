# Terraform::AWS::KinesisFirehoseDeliveryStream ExtendedS3Configuration DataFormatConversionConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#inputformatconfiguration" title="InputFormatConfiguration">InputFormatConfiguration</a>" : <i>[ <a href="extendeds3configuration-dataformatconversionconfiguration-inputformatconfiguration.md">InputFormatConfiguration</a>, ... ]</i>,
    "<a href="#outputformatconfiguration" title="OutputFormatConfiguration">OutputFormatConfiguration</a>" : <i>[ <a href="extendeds3configuration-dataformatconversionconfiguration-outputformatconfiguration.md">OutputFormatConfiguration</a>, ... ]</i>,
    "<a href="#schemaconfiguration" title="SchemaConfiguration">SchemaConfiguration</a>" : <i>[ <a href="extendeds3configuration-dataformatconversionconfiguration-schemaconfiguration.md">SchemaConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#inputformatconfiguration" title="InputFormatConfiguration">InputFormatConfiguration</a>: <i>
      - <a href="extendeds3configuration-dataformatconversionconfiguration-inputformatconfiguration.md">InputFormatConfiguration</a></i>
<a href="#outputformatconfiguration" title="OutputFormatConfiguration">OutputFormatConfiguration</a>: <i>
      - <a href="extendeds3configuration-dataformatconversionconfiguration-outputformatconfiguration.md">OutputFormatConfiguration</a></i>
<a href="#schemaconfiguration" title="SchemaConfiguration">SchemaConfiguration</a>: <i>
      - <a href="extendeds3configuration-dataformatconversionconfiguration-schemaconfiguration.md">SchemaConfiguration</a></i>
</pre>

## Properties

#### Enabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputFormatConfiguration

_Required_: No
_Type_: List of <a href="extendeds3configuration-dataformatconversionconfiguration-inputformatconfiguration.md">InputFormatConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputFormatConfiguration

_Required_: No
_Type_: List of <a href="extendeds3configuration-dataformatconversionconfiguration-outputformatconfiguration.md">OutputFormatConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaConfiguration

_Required_: No
_Type_: List of <a href="extendeds3configuration-dataformatconversionconfiguration-schemaconfiguration.md">SchemaConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

