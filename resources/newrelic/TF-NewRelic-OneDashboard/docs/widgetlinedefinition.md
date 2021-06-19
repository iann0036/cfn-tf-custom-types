# TF::NewRelic::OneDashboard WidgetLineDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#column" title="Column">Column</a>" : <i>Double</i>,
    "<a href="#height" title="Height">Height</a>" : <i>Double</i>,
    "<a href="#row" title="Row">Row</a>" : <i>Double</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#width" title="Width">Width</a>" : <i>Double</i>,
    "<a href="#nrqlquery" title="NrqlQuery">NrqlQuery</a>" : <i>[ <a href="nrqlquerydefinition.md">NrqlQueryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#column" title="Column">Column</a>: <i>Double</i>
<a href="#height" title="Height">Height</a>: <i>Double</i>
<a href="#row" title="Row">Row</a>: <i>Double</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#width" title="Width">Width</a>: <i>Double</i>
<a href="#nrqlquery" title="NrqlQuery">NrqlQuery</a>: <i>
      - <a href="nrqlquerydefinition.md">NrqlQueryDefinition</a></i>
</pre>

## Properties

#### Column

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Height

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Row

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Width

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NrqlQuery

_Required_: No

_Type_: List of <a href="nrqlquerydefinition.md">NrqlQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

