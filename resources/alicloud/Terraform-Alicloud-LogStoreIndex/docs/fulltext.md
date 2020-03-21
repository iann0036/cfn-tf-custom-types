# Terraform::Alicloud::LogStoreIndex FullText

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#casesensitive" title="CaseSensitive">CaseSensitive</a>" : <i>Boolean</i>,
    "<a href="#includechinese" title="IncludeChinese">IncludeChinese</a>" : <i>Boolean</i>,
    "<a href="#token" title="Token">Token</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#casesensitive" title="CaseSensitive">CaseSensitive</a>: <i>Boolean</i>
<a href="#includechinese" title="IncludeChinese">IncludeChinese</a>: <i>Boolean</i>
<a href="#token" title="Token">Token</a>: <i>String</i>
</pre>

## Properties

#### CaseSensitive

Whether the case sensitive. Default to false.
* `include_chinese` - (Optional) Whether includes the chinese. Default to false.
* `token` - (Optional) The string of several split words, like "\r", "#".

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeChinese

Whether includes the chinese. Default to false.
* `token` - (Optional) The string of several split words, like "\r", "#".

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

The string of several split words, like "\r", "#".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

