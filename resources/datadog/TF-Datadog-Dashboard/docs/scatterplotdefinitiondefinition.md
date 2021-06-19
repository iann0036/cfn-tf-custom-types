# TF::Datadog::Dashboard ScatterplotDefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#colorbygroups" title="ColorByGroups">ColorByGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#livespan" title="LiveSpan">LiveSpan</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#titlealign" title="TitleAlign">TitleAlign</a>" : <i>String</i>,
    "<a href="#titlesize" title="TitleSize">TitleSize</a>" : <i>String</i>,
    "<a href="#customlink" title="CustomLink">CustomLink</a>" : <i>[ <a href="customlinkdefinition.md">CustomLinkDefinition</a>, ... ]</i>,
    "<a href="#request" title="Request">Request</a>" : <i>[ <a href="requestdefinition.md">RequestDefinition</a>, ... ]</i>,
    "<a href="#xaxis" title="Xaxis">Xaxis</a>" : <i>[ <a href="xaxisdefinition.md">XaxisDefinition</a>, ... ]</i>,
    "<a href="#yaxis" title="Yaxis">Yaxis</a>" : <i>[ <a href="yaxisdefinition.md">YaxisDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#colorbygroups" title="ColorByGroups">ColorByGroups</a>: <i>
      - String</i>
<a href="#livespan" title="LiveSpan">LiveSpan</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#titlealign" title="TitleAlign">TitleAlign</a>: <i>String</i>
<a href="#titlesize" title="TitleSize">TitleSize</a>: <i>String</i>
<a href="#customlink" title="CustomLink">CustomLink</a>: <i>
      - <a href="customlinkdefinition.md">CustomLinkDefinition</a></i>
<a href="#request" title="Request">Request</a>: <i>
      - <a href="requestdefinition.md">RequestDefinition</a></i>
<a href="#xaxis" title="Xaxis">Xaxis</a>: <i>
      - <a href="xaxisdefinition.md">XaxisDefinition</a></i>
<a href="#yaxis" title="Yaxis">Yaxis</a>: <i>
      - <a href="yaxisdefinition.md">YaxisDefinition</a></i>
</pre>

## Properties

#### ColorByGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Xaxis

_Required_: No

_Type_: List of <a href="xaxisdefinition.md">XaxisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Yaxis

_Required_: No

_Type_: List of <a href="yaxisdefinition.md">YaxisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

