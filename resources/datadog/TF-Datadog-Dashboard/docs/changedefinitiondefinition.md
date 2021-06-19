# TF::Datadog::Dashboard ChangeDefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#livespan" title="LiveSpan">LiveSpan</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#titlealign" title="TitleAlign">TitleAlign</a>" : <i>String</i>,
    "<a href="#titlesize" title="TitleSize">TitleSize</a>" : <i>String</i>,
    "<a href="#customlink" title="CustomLink">CustomLink</a>" : <i>[ <a href="customlinkdefinition.md">CustomLinkDefinition</a>, ... ]</i>,
    "<a href="#request" title="Request">Request</a>" : <i>[ <a href="requestdefinition.md">RequestDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#livespan" title="LiveSpan">LiveSpan</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#titlealign" title="TitleAlign">TitleAlign</a>: <i>String</i>
<a href="#titlesize" title="TitleSize">TitleSize</a>: <i>String</i>
<a href="#customlink" title="CustomLink">CustomLink</a>: <i>
      - <a href="customlinkdefinition.md">CustomLinkDefinition</a></i>
<a href="#request" title="Request">Request</a>: <i>
      - <a href="requestdefinition.md">RequestDefinition</a></i>
</pre>

## Properties

#### LiveSpan

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TitleAlign

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TitleSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomLink

_Required_: No

_Type_: List of <a href="customlinkdefinition.md">CustomLinkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of <a href="requestdefinition.md">RequestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

