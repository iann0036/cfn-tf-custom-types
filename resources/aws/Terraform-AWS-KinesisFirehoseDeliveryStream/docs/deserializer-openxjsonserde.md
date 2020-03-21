# Terraform::AWS::KinesisFirehoseDeliveryStream Deserializer OpenXJsonSerDe

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caseinsensitive" title="CaseInsensitive">CaseInsensitive</a>" : <i>Boolean</i>,
    "<a href="#columntojsonkeymappings" title="ColumnToJsonKeyMappings">ColumnToJsonKeyMappings</a>" : <i>[ &lt;a href=&#34;deserializer-openxjsonserde-columntojsonkeymappings.md&#34;&gt;ColumnToJsonKeyMappings&lt;/a&gt;, ... ]</i>,
    "<a href="#convertdotsinjsonkeystounderscores" title="ConvertDotsInJsonKeysToUnderscores">ConvertDotsInJsonKeysToUnderscores</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#caseinsensitive" title="CaseInsensitive">CaseInsensitive</a>: <i>Boolean</i>
<a href="#columntojsonkeymappings" title="ColumnToJsonKeyMappings">ColumnToJsonKeyMappings</a>: <i>
      - &lt;a href=&#34;deserializer-openxjsonserde-columntojsonkeymappings.md&#34;&gt;ColumnToJsonKeyMappings&lt;/a&gt;</i>
<a href="#convertdotsinjsonkeystounderscores" title="ConvertDotsInJsonKeysToUnderscores">ConvertDotsInJsonKeysToUnderscores</a>: <i>Boolean</i>
</pre>

## Properties

#### CaseInsensitive

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColumnToJsonKeyMappings

_Required_: No
_Type_: List of &lt;a href=&#34;deserializer-openxjsonserde-columntojsonkeymappings.md&#34;&gt;ColumnToJsonKeyMappings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConvertDotsInJsonKeysToUnderscores

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

