# Terraform::Datadog::Dashboard Widget HostmapDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#group" title="Group">Group</a>" : <i>[ String, ... ]</i>,
    "<a href="#nogrouphosts" title="NoGroupHosts">NoGroupHosts</a>" : <i>Boolean</i>,
    "<a href="#nometrichosts" title="NoMetricHosts">NoMetricHosts</a>" : <i>Boolean</i>,
    "<a href="#nodetype" title="NodeType">NodeType</a>" : <i>String</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>[ String, ... ]</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#titlealign" title="TitleAlign">TitleAlign</a>" : <i>String</i>,
    "<a href="#titlesize" title="TitleSize">TitleSize</a>" : <i>String</i>,
    "<a href="#request" title="Request">Request</a>" : <i>[ <a href="widget-hostmapdefinition-request.md">Request</a>, ... ]</i>,
    "<a href="#style" title="Style">Style</a>" : <i>[ <a href="widget-hostmapdefinition-style.md">Style</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#group" title="Group">Group</a>: <i>
      - String</i>
<a href="#nogrouphosts" title="NoGroupHosts">NoGroupHosts</a>: <i>Boolean</i>
<a href="#nometrichosts" title="NoMetricHosts">NoMetricHosts</a>: <i>Boolean</i>
<a href="#nodetype" title="NodeType">NodeType</a>: <i>String</i>
<a href="#scope" title="Scope">Scope</a>: <i>
      - String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#titlealign" title="TitleAlign">TitleAlign</a>: <i>String</i>
<a href="#titlesize" title="TitleSize">TitleSize</a>: <i>String</i>
<a href="#request" title="Request">Request</a>: <i>
      - <a href="widget-hostmapdefinition-request.md">Request</a></i>
<a href="#style" title="Style">Style</a>: <i>
      - <a href="widget-hostmapdefinition-style.md">Style</a></i>
</pre>

## Properties

#### Group

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoGroupHosts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoMetricHosts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: List of String

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

#### Request

_Required_: No

_Type_: List of <a href="widget-hostmapdefinition-request.md">Request</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Style

_Required_: No

_Type_: List of <a href="widget-hostmapdefinition-style.md">Style</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

