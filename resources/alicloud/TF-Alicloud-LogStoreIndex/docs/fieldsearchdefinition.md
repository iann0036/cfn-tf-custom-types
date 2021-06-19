# TF::Alicloud::LogStoreIndex FieldSearchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
    "<a href="#casesensitive" title="CaseSensitive">CaseSensitive</a>" : <i>Boolean</i>,
    "<a href="#enableanalytics" title="EnableAnalytics">EnableAnalytics</a>" : <i>Boolean</i>,
    "<a href="#includechinese" title="IncludeChinese">IncludeChinese</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#token" title="Token">Token</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#jsonkeys" title="JsonKeys">JsonKeys</a>" : <i>[ <a href="jsonkeysdefinition.md">JsonKeysDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alias" title="Alias">Alias</a>: <i>String</i>
<a href="#casesensitive" title="CaseSensitive">CaseSensitive</a>: <i>Boolean</i>
<a href="#enableanalytics" title="EnableAnalytics">EnableAnalytics</a>: <i>Boolean</i>
<a href="#includechinese" title="IncludeChinese">IncludeChinese</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#token" title="Token">Token</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#jsonkeys" title="JsonKeys">JsonKeys</a>: <i>
      - <a href="jsonkeysdefinition.md">JsonKeysDefinition</a></i>
</pre>

## Properties

#### Alias

The alias of one field.
* `doc_value` - (Optional) Whether to enable statistics. default to true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaseSensitive

Whether the case sensitive for the field. Default to false. It is valid when "type" is "text" or "json".
* `include_chinese` - (Optional) Whether includes the chinese for the field. Default to false. It is valid when "type" is "text" or "json".
* `token` - (Optional) The string of several split words, like "\r", "#". It is valid when "type" is "text" or "json".
* `enable_analytics` - (Optional) Whether to enable field analytics. Default to true.
* `json_keys` - (Optional, Available in 1.66.0+) Use nested index when type is json
* `name` - (Required) When using the json_keys field, this field is required.
* `type` - (Optional) The type of one field. Valid values: ["long", "text", "double"]. Default to "long"
* `alias` - (Optional) The alias of one field.
* `doc_value` - (Optional) Whether to enable statistics. default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAnalytics

Whether to enable field analytics. Default to true.
* `json_keys` - (Optional, Available in 1.66.0+) Use nested index when type is json
* `name` - (Required) When using the json_keys field, this field is required.
* `type` - (Optional) The type of one field. Valid values: ["long", "text", "double"]. Default to "long"
* `alias` - (Optional) The alias of one field.
* `doc_value` - (Optional) Whether to enable statistics. default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeChinese

Whether includes the chinese for the field. Default to false. It is valid when "type" is "text" or "json".
* `token` - (Optional) The string of several split words, like "\r", "#". It is valid when "type" is "text" or "json".
* `enable_analytics` - (Optional) Whether to enable field analytics. Default to true.
* `json_keys` - (Optional, Available in 1.66.0+) Use nested index when type is json
* `name` - (Required) When using the json_keys field, this field is required.
* `type` - (Optional) The type of one field. Valid values: ["long", "text", "double"]. Default to "long"
* `alias` - (Optional) The alias of one field.
* `doc_value` - (Optional) Whether to enable statistics. default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

When using the json_keys field, this field is required.
* `type` - (Optional) The type of one field. Valid values: ["long", "text", "double"]. Default to "long"
* `alias` - (Optional) The alias of one field.
* `doc_value` - (Optional) Whether to enable statistics. default to true.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

The string of several split words, like "\r", "#". It is valid when "type" is "text" or "json".
* `enable_analytics` - (Optional) Whether to enable field analytics. Default to true.
* `json_keys` - (Optional, Available in 1.66.0+) Use nested index when type is json
* `name` - (Required) When using the json_keys field, this field is required.
* `type` - (Optional) The type of one field. Valid values: ["long", "text", "double"]. Default to "long"
* `alias` - (Optional) The alias of one field.
* `doc_value` - (Optional) Whether to enable statistics. default to true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of one field. Valid values: ["long", "text", "double"]. Default to "long"
* `alias` - (Optional) The alias of one field.
* `doc_value` - (Optional) Whether to enable statistics. default to true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsonKeys

_Required_: No

_Type_: List of <a href="jsonkeysdefinition.md">JsonKeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

