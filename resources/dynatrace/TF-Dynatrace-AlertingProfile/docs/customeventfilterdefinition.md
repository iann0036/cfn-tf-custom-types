# TF::Dynatrace::AlertingProfile CustomEventFilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#customdescriptionfilter" title="CustomDescriptionFilter">CustomDescriptionFilter</a>" : <i>[ <a href="customdescriptionfilterdefinition.md">CustomDescriptionFilterDefinition</a>, ... ]</i>,
    "<a href="#customtitlefilter" title="CustomTitleFilter">CustomTitleFilter</a>" : <i>[ <a href="customtitlefilterdefinition.md">CustomTitleFilterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#customdescriptionfilter" title="CustomDescriptionFilter">CustomDescriptionFilter</a>: <i>
      - <a href="customdescriptionfilterdefinition.md">CustomDescriptionFilterDefinition</a></i>
<a href="#customtitlefilter" title="CustomTitleFilter">CustomTitleFilter</a>: <i>
      - <a href="customtitlefilterdefinition.md">CustomTitleFilterDefinition</a></i>
</pre>

## Properties

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomDescriptionFilter

_Required_: No

_Type_: List of <a href="customdescriptionfilterdefinition.md">CustomDescriptionFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomTitleFilter

_Required_: No

_Type_: List of <a href="customtitlefilterdefinition.md">CustomTitleFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

