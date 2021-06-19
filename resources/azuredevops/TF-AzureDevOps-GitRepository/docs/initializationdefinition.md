# TF::AzureDevOps::GitRepository InitializationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inittype" title="InitType">InitType</a>" : <i>String</i>,
    "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
    "<a href="#sourceurl" title="SourceUrl">SourceUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#inittype" title="InitType">InitType</a>: <i>String</i>
<a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
<a href="#sourceurl" title="SourceUrl">SourceUrl</a>: <i>String</i>
</pre>

## Properties

#### InitType

The type of repository to create. Valid values: `Uninitialized`, `Clean` or `Import`. Defaults to `Uninitialized`.
- `source_type` - (Optional) Type of the source repository. Used if the `init_type` is `Import`. Valid values: `Git`.
- `source_url` - (Optional) The URL of the source repository. Used if the `init_type` is `Import`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

Type of the source repository. Used if the `init_type` is `Import`. Valid values: `Git`.
- `source_url` - (Optional) The URL of the source repository. Used if the `init_type` is `Import`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUrl

The URL of the source repository. Used if the `init_type` is `Import`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

