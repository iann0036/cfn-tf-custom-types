# TF::AVI::Alertconfig SysEventRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#eventid" title="EventId">EventId</a>" : <i>String</i>,
    "<a href="#notcond" title="NotCond">NotCond</a>" : <i>Boolean</i>,
    "<a href="#eventdetails" title="EventDetails">EventDetails</a>" : <i>[ <a href="eventdetailsdefinition.md">EventDetailsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#eventid" title="EventId">EventId</a>: <i>String</i>
<a href="#notcond" title="NotCond">NotCond</a>: <i>Boolean</i>
<a href="#eventdetails" title="EventDetails">EventDetails</a>: <i>
      - <a href="eventdetailsdefinition.md">EventDetailsDefinition</a></i>
</pre>

## Properties

#### EventId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotCond

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventDetails

_Required_: No

_Type_: List of <a href="eventdetailsdefinition.md">EventDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

