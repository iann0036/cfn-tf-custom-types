# Terraform::AWS::KinesisAnalyticsApplication Inputs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
    "<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>" : <i>[ &lt;a href=&#34;inputs-kinesisfirehose.md&#34;&gt;KinesisFirehose&lt;/a&gt;, ... ]</i>,
    "<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>" : <i>[ &lt;a href=&#34;inputs-kinesisstream.md&#34;&gt;KinesisStream&lt;/a&gt;, ... ]</i>,
    "<a href="#parallelism" title="Parallelism">Parallelism</a>" : <i>[ &lt;a href=&#34;inputs-parallelism.md&#34;&gt;Parallelism&lt;/a&gt;, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ &lt;a href=&#34;inputs-processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;, ... ]</i>,
    "<a href="#schema" title="Schema">Schema</a>" : <i>[ &lt;a href=&#34;inputs-schema.md&#34;&gt;Schema&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>: <i>
      - &lt;a href=&#34;inputs-kinesisfirehose.md&#34;&gt;KinesisFirehose&lt;/a&gt;</i>
<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>: <i>
      - &lt;a href=&#34;inputs-kinesisstream.md&#34;&gt;KinesisStream&lt;/a&gt;</i>
<a href="#parallelism" title="Parallelism">Parallelism</a>: <i>
      - &lt;a href=&#34;inputs-parallelism.md&#34;&gt;Parallelism&lt;/a&gt;</i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - &lt;a href=&#34;inputs-processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;</i>
<a href="#schema" title="Schema">Schema</a>: <i>
      - &lt;a href=&#34;inputs-schema.md&#34;&gt;Schema&lt;/a&gt;</i>
</pre>

## Properties

#### NamePrefix

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisFirehose

_Required_: No
_Type_: List of &lt;a href=&#34;inputs-kinesisfirehose.md&#34;&gt;KinesisFirehose&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisStream

_Required_: No
_Type_: List of &lt;a href=&#34;inputs-kinesisstream.md&#34;&gt;KinesisStream&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parallelism

_Required_: No
_Type_: List of &lt;a href=&#34;inputs-parallelism.md&#34;&gt;Parallelism&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;inputs-processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No
_Type_: List of &lt;a href=&#34;inputs-schema.md&#34;&gt;Schema&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

