# TF::PagerDuty::ServiceEventRule ActionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#annotate" title="Annotate">Annotate</a>" : <i>[ <a href="annotatedefinition.md">AnnotateDefinition</a>, ... ]</i>,
    "<a href="#eventaction" title="EventAction">EventAction</a>" : <i>[ <a href="eventactiondefinition.md">EventActionDefinition</a>, ... ]</i>,
    "<a href="#extractions" title="Extractions">Extractions</a>" : <i>[ <a href="extractionsdefinition.md">ExtractionsDefinition</a>, ... ]</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>[ <a href="prioritydefinition.md">PriorityDefinition</a>, ... ]</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>[ <a href="severitydefinition.md">SeverityDefinition</a>, ... ]</i>,
    "<a href="#suppress" title="Suppress">Suppress</a>" : <i>[ <a href="suppressdefinition.md">SuppressDefinition</a>, ... ]</i>,
    "<a href="#suspend" title="Suspend">Suspend</a>" : <i>[ <a href="suspenddefinition.md">SuspendDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#annotate" title="Annotate">Annotate</a>: <i>
      - <a href="annotatedefinition.md">AnnotateDefinition</a></i>
<a href="#eventaction" title="EventAction">EventAction</a>: <i>
      - <a href="eventactiondefinition.md">EventActionDefinition</a></i>
<a href="#extractions" title="Extractions">Extractions</a>: <i>
      - <a href="extractionsdefinition.md">ExtractionsDefinition</a></i>
<a href="#priority" title="Priority">Priority</a>: <i>
      - <a href="prioritydefinition.md">PriorityDefinition</a></i>
<a href="#severity" title="Severity">Severity</a>: <i>
      - <a href="severitydefinition.md">SeverityDefinition</a></i>
<a href="#suppress" title="Suppress">Suppress</a>: <i>
      - <a href="suppressdefinition.md">SuppressDefinition</a></i>
<a href="#suspend" title="Suspend">Suspend</a>: <i>
      - <a href="suspenddefinition.md">SuspendDefinition</a></i>
</pre>

## Properties

#### Annotate

_Required_: No

_Type_: List of <a href="annotatedefinition.md">AnnotateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventAction

_Required_: No

_Type_: List of <a href="eventactiondefinition.md">EventActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extractions

_Required_: No

_Type_: List of <a href="extractionsdefinition.md">ExtractionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: List of <a href="prioritydefinition.md">PriorityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

_Required_: No

_Type_: List of <a href="severitydefinition.md">SeverityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Suppress

_Required_: No

_Type_: List of <a href="suppressdefinition.md">SuppressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Suspend

_Required_: No

_Type_: List of <a href="suspenddefinition.md">SuspendDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

