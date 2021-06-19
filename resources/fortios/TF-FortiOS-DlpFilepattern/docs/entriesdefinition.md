# TF::FortiOS::DlpFilepattern EntriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filetype" title="FileType">FileType</a>" : <i>String</i>,
    "<a href="#filtertype" title="FilterType">FilterType</a>" : <i>String</i>,
    "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#filetype" title="FileType">FileType</a>: <i>String</i>
<a href="#filtertype" title="FilterType">FilterType</a>: <i>String</i>
<a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
</pre>

## Properties

#### FileType

Select a file type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterType

Filter by file name pattern or by file type. Valid values: `pattern`, `type`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

Add a file name pattern.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

