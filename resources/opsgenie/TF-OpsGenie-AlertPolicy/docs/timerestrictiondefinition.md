# TF::OpsGenie::AlertPolicy TimeRestrictionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#restriction" title="Restriction">Restriction</a>" : <i>[ <a href="restrictiondefinition.md">RestrictionDefinition</a>, ... ]</i>,
    "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ <a href="restrictionsdefinition.md">RestrictionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#restriction" title="Restriction">Restriction</a>: <i>
      - <a href="restrictiondefinition.md">RestrictionDefinition</a></i>
<a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - <a href="restrictionsdefinition.md">RestrictionsDefinition</a></i>
</pre>

## Properties

#### Type

Defines if restriction should apply daily on given hours or on certain days and hours. Possible values are: `time-of-day`, `weekday-and-time-of-day`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restriction

_Required_: No

_Type_: List of <a href="restrictiondefinition.md">RestrictionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No

_Type_: List of <a href="restrictionsdefinition.md">RestrictionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

