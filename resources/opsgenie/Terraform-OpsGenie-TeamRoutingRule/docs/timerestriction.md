# Terraform::OpsGenie::TeamRoutingRule TimeRestriction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#restriction" title="Restriction">Restriction</a>" : <i>[ <a href="timerestriction-restriction.md">Restriction</a>, ... ]</i>,
    "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ <a href="timerestriction-restrictions.md">Restrictions</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#restriction" title="Restriction">Restriction</a>: <i>
      - <a href="timerestriction-restriction.md">Restriction</a></i>
<a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - <a href="timerestriction-restrictions.md">Restrictions</a></i>
</pre>

## Properties

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restriction

_Required_: No

_Type_: List of <a href="timerestriction-restriction.md">Restriction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No

_Type_: List of <a href="timerestriction-restrictions.md">Restrictions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

