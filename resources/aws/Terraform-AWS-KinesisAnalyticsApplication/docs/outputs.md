# Terraform::AWS::KinesisAnalyticsApplication Outputs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>" : <i>[ &lt;a href=&#34;outputs-kinesisfirehose.md&#34;&gt;KinesisFirehose&lt;/a&gt;, ... ]</i>,
    "<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>" : <i>[ &lt;a href=&#34;outputs-kinesisstream.md&#34;&gt;KinesisStream&lt;/a&gt;, ... ]</i>,
    "<a href="#lambda" title="Lambda">Lambda</a>" : <i>[ &lt;a href=&#34;outputs-lambda.md&#34;&gt;Lambda&lt;/a&gt;, ... ]</i>,
    "<a href="#schema" title="Schema">Schema</a>" : <i>[ &lt;a href=&#34;outputs-schema.md&#34;&gt;Schema&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>: <i>
      - &lt;a href=&#34;outputs-kinesisfirehose.md&#34;&gt;KinesisFirehose&lt;/a&gt;</i>
<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>: <i>
      - &lt;a href=&#34;outputs-kinesisstream.md&#34;&gt;KinesisStream&lt;/a&gt;</i>
<a href="#lambda" title="Lambda">Lambda</a>: <i>
      - &lt;a href=&#34;outputs-lambda.md&#34;&gt;Lambda&lt;/a&gt;</i>
<a href="#schema" title="Schema">Schema</a>: <i>
      - &lt;a href=&#34;outputs-schema.md&#34;&gt;Schema&lt;/a&gt;</i>
</pre>

## Properties

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisFirehose

_Required_: No
_Type_: List of &lt;a href=&#34;outputs-kinesisfirehose.md&#34;&gt;KinesisFirehose&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisStream

_Required_: No
_Type_: List of &lt;a href=&#34;outputs-kinesisstream.md&#34;&gt;KinesisStream&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lambda

_Required_: No
_Type_: List of &lt;a href=&#34;outputs-lambda.md&#34;&gt;Lambda&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No
_Type_: List of &lt;a href=&#34;outputs-schema.md&#34;&gt;Schema&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

