# Terraform::OpsGenie::ScheduleRotation

CloudFormation equivalent of opsgenie_schedule_rotation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpsGenie::ScheduleRotation",
    "Properties" : {
        "<a href="#enddate" title="EndDate">EndDate</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#length" title="Length">Length</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#scheduleid" title="ScheduleId">ScheduleId</a>" : <i>String</i>,
        "<a href="#startdate" title="StartDate">StartDate</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#participant" title="Participant">Participant</a>" : <i>[ &lt;a href=&#34;participant.md&#34;&gt;Participant&lt;/a&gt;, ... ]</i>,
        "<a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>" : <i>[ &lt;a href=&#34;timerestriction.md&#34;&gt;TimeRestriction&lt;/a&gt;, ... ]</i>,
        "<a href="#restriction" title="Restriction">Restriction</a>" : <i>[ &lt;a href=&#34;restriction.md&#34;&gt;Restriction&lt;/a&gt;, ... ]</i>,
        "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpsGenie::ScheduleRotation
Properties:
    <a href="#enddate" title="EndDate">EndDate</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#length" title="Length">Length</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#scheduleid" title="ScheduleId">ScheduleId</a>: <i>String</i>
    <a href="#startdate" title="StartDate">StartDate</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#participant" title="Participant">Participant</a>: <i>
      - &lt;a href=&#34;participant.md&#34;&gt;Participant&lt;/a&gt;</i>
    <a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>: <i>
      - &lt;a href=&#34;timerestriction.md&#34;&gt;TimeRestriction&lt;/a&gt;</i>
    <a href="#restriction" title="Restriction">Restriction</a>: <i>
      - &lt;a href=&#34;restriction.md&#34;&gt;Restriction&lt;/a&gt;</i>
    <a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;</i>
</pre>

## Properties

#### EndDate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Length

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDate

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Participant

_Required_: No

_Type_: List of &lt;a href=&#34;participant.md&#34;&gt;Participant&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRestriction

_Required_: No

_Type_: List of &lt;a href=&#34;timerestriction.md&#34;&gt;TimeRestriction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restriction

_Required_: No

_Type_: List of &lt;a href=&#34;restriction.md&#34;&gt;Restriction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No

_Type_: List of &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

