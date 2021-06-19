# TF::Dynatrace::AlertingProfile EventTypeFiltersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#customeventfilter" title="CustomEventFilter">CustomEventFilter</a>" : <i>[ <a href="customeventfilterdefinition.md">CustomEventFilterDefinition</a>, ... ]</i>,
    "<a href="#predefinedeventfilter" title="PredefinedEventFilter">PredefinedEventFilter</a>" : <i>[ <a href="predefinedeventfilterdefinition.md">PredefinedEventFilterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#customeventfilter" title="CustomEventFilter">CustomEventFilter</a>: <i>
      - <a href="customeventfilterdefinition.md">CustomEventFilterDefinition</a></i>
<a href="#predefinedeventfilter" title="PredefinedEventFilter">PredefinedEventFilter</a>: <i>
      - <a href="predefinedeventfilterdefinition.md">PredefinedEventFilterDefinition</a></i>
</pre>

## Properties

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomEventFilter

_Required_: No

_Type_: List of <a href="customeventfilterdefinition.md">CustomEventFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedEventFilter

_Required_: No

_Type_: List of <a href="predefinedeventfilterdefinition.md">PredefinedEventFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

