# TF::ILert::AlertSource SupportHoursDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoraiseincidents" title="AutoRaiseIncidents">AutoRaiseIncidents</a>" : <i>Boolean</i>,
    "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
    "<a href="#supportdays" title="SupportDays">SupportDays</a>" : <i>[ <a href="supportdaysdefinition.md">SupportDaysDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoraiseincidents" title="AutoRaiseIncidents">AutoRaiseIncidents</a>: <i>Boolean</i>
<a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
<a href="#supportdays" title="SupportDays">SupportDays</a>: <i>
      - <a href="supportdaysdefinition.md">SupportDaysDefinition</a></i>
</pre>

## Properties

#### AutoRaiseIncidents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportDays

_Required_: No

_Type_: List of <a href="supportdaysdefinition.md">SupportDaysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

