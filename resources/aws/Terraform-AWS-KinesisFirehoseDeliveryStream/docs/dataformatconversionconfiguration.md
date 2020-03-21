# Terraform::AWS::KinesisFirehoseDeliveryStream DataFormatConversionConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#inputformatconfiguration" title="InputFormatConfiguration">InputFormatConfiguration</a>" : <i>[ &lt;a href=&#34;dataformatconversionconfiguration-inputformatconfiguration.md&#34;&gt;InputFormatConfiguration&lt;/a&gt;, ... ]</i>,
    "<a href="#outputformatconfiguration" title="OutputFormatConfiguration">OutputFormatConfiguration</a>" : <i>[ &lt;a href=&#34;dataformatconversionconfiguration-outputformatconfiguration.md&#34;&gt;OutputFormatConfiguration&lt;/a&gt;, ... ]</i>,
    "<a href="#schemaconfiguration" title="SchemaConfiguration">SchemaConfiguration</a>" : <i>[ &lt;a href=&#34;dataformatconversionconfiguration-schemaconfiguration.md&#34;&gt;SchemaConfiguration&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#inputformatconfiguration" title="InputFormatConfiguration">InputFormatConfiguration</a>: <i>
      - &lt;a href=&#34;dataformatconversionconfiguration-inputformatconfiguration.md&#34;&gt;InputFormatConfiguration&lt;/a&gt;</i>
<a href="#outputformatconfiguration" title="OutputFormatConfiguration">OutputFormatConfiguration</a>: <i>
      - &lt;a href=&#34;dataformatconversionconfiguration-outputformatconfiguration.md&#34;&gt;OutputFormatConfiguration&lt;/a&gt;</i>
<a href="#schemaconfiguration" title="SchemaConfiguration">SchemaConfiguration</a>: <i>
      - &lt;a href=&#34;dataformatconversionconfiguration-schemaconfiguration.md&#34;&gt;SchemaConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### Enabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputFormatConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;dataformatconversionconfiguration-inputformatconfiguration.md&#34;&gt;InputFormatConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputFormatConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;dataformatconversionconfiguration-outputformatconfiguration.md&#34;&gt;OutputFormatConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;dataformatconversionconfiguration-schemaconfiguration.md&#34;&gt;SchemaConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

