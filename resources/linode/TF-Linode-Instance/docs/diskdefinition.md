# TF::Linode::Instance DiskDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authorizedkeys" title="AuthorizedKeys">AuthorizedKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#authorizedusers" title="AuthorizedUsers">AuthorizedUsers</a>" : <i>[ String, ... ]</i>,
    "<a href="#filesystem" title="Filesystem">Filesystem</a>" : <i>String</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#rootpass" title="RootPass">RootPass</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#stackscriptdata" title="StackscriptData">StackscriptData</a>" : <i>[ <a href="stackscriptdatadefinition.md">StackscriptDataDefinition</a>, ... ]</i>,
    "<a href="#stackscriptid" title="StackscriptId">StackscriptId</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#authorizedkeys" title="AuthorizedKeys">AuthorizedKeys</a>: <i>
      - String</i>
<a href="#authorizedusers" title="AuthorizedUsers">AuthorizedUsers</a>: <i>
      - String</i>
<a href="#filesystem" title="Filesystem">Filesystem</a>: <i>String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#rootpass" title="RootPass">RootPass</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#stackscriptdata" title="StackscriptData">StackscriptData</a>: <i>
      - <a href="stackscriptdatadefinition.md">StackscriptDataDefinition</a></i>
<a href="#stackscriptid" title="StackscriptId">StackscriptId</a>: <i>Double</i>
</pre>

## Properties

#### AuthorizedKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizedUsers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filesystem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootPass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackscriptData

_Required_: No

_Type_: List of <a href="stackscriptdatadefinition.md">StackscriptDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackscriptId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

