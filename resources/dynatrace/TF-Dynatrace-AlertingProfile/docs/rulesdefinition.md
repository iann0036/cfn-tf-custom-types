# TF::Dynatrace::AlertingProfile RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#delayinminutes" title="DelayInMinutes">DelayInMinutes</a>" : <i>Double</i>,
    "<a href="#severitylevel" title="SeverityLevel">SeverityLevel</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#tagfilter" title="TagFilter">TagFilter</a>" : <i>[ <a href="tagfilterdefinition.md">TagFilterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#delayinminutes" title="DelayInMinutes">DelayInMinutes</a>: <i>Double</i>
<a href="#severitylevel" title="SeverityLevel">SeverityLevel</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#tagfilter" title="TagFilter">TagFilter</a>: <i>
      - <a href="tagfilterdefinition.md">TagFilterDefinition</a></i>
</pre>

## Properties

#### DelayInMinutes

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeverityLevel

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagFilter

_Required_: No

_Type_: List of <a href="tagfilterdefinition.md">TagFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

