# TF::OCI::ObjectstorageBucket RetentionRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#timerulelocked" title="TimeRuleLocked">TimeRuleLocked</a>" : <i>String</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>[ <a href="durationdefinition.md">DurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#timerulelocked" title="TimeRuleLocked">TimeRuleLocked</a>: <i>String</i>
<a href="#duration" title="Duration">Duration</a>: <i>
      - <a href="durationdefinition.md">DurationDefinition</a></i>
</pre>

## Properties

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRuleLocked

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No

_Type_: List of <a href="durationdefinition.md">DurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

