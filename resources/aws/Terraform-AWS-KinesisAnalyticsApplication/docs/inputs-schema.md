# Terraform::AWS::KinesisAnalyticsApplication Inputs Schema

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#recordencoding" title="RecordEncoding">RecordEncoding</a>" : <i>String</i>,
    "<a href="#recordcolumns" title="RecordColumns">RecordColumns</a>" : <i>[ &lt;a href=&#34;inputs-schema-recordcolumns.md&#34;&gt;RecordColumns&lt;/a&gt;, ... ]</i>,
    "<a href="#recordformat" title="RecordFormat">RecordFormat</a>" : <i>[ &lt;a href=&#34;inputs-schema-recordformat.md&#34;&gt;RecordFormat&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#recordencoding" title="RecordEncoding">RecordEncoding</a>: <i>String</i>
<a href="#recordcolumns" title="RecordColumns">RecordColumns</a>: <i>
      - &lt;a href=&#34;inputs-schema-recordcolumns.md&#34;&gt;RecordColumns&lt;/a&gt;</i>
<a href="#recordformat" title="RecordFormat">RecordFormat</a>: <i>
      - &lt;a href=&#34;inputs-schema-recordformat.md&#34;&gt;RecordFormat&lt;/a&gt;</i>
</pre>

## Properties

#### RecordEncoding

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordColumns

_Required_: No
_Type_: List of &lt;a href=&#34;inputs-schema-recordcolumns.md&#34;&gt;RecordColumns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordFormat

_Required_: No
_Type_: List of &lt;a href=&#34;inputs-schema-recordformat.md&#34;&gt;RecordFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

