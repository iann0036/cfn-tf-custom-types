# TF::B2::Bucket DefaultRetentionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#period" title="Period">Period</a>" : <i>[ <a href="perioddefinition.md">PeriodDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#period" title="Period">Period</a>: <i>
      - <a href="perioddefinition.md">PeriodDefinition</a></i>
</pre>

## Properties

#### Mode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: List of <a href="perioddefinition.md">PeriodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

