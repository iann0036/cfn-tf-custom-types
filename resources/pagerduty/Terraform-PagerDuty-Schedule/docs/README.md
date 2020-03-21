# Terraform::PagerDuty::Schedule

A [schedule](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Schedules/get_schedules) determines the time periods that users are on call. Only on-call users are eligible to receive notifications from incidents.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PagerDuty::Schedule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overflow" title="Overflow">Overflow</a>" : <i>Boolean</i>,
        "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
        "<a href="#layer" title="Layer">Layer</a>" : <i>[ <a href="layer.md">Layer</a>, ... ]</i>,
        "<a href="#restriction" title="Restriction">Restriction</a>" : <i>[ <a href="restriction.md">Restriction</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PagerDuty::Schedule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overflow" title="Overflow">Overflow</a>: <i>Boolean</i>
    <a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
    <a href="#layer" title="Layer">Layer</a>: <i>
      - <a href="layer.md">Layer</a></i>
    <a href="#restriction" title="Restriction">Restriction</a>: <i>
      - <a href="restriction.md">Restriction</a></i>
</pre>

## Properties

#### Description

The description of the schedule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the schedule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overflow

Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter `overflow` is passed. For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from `2011-06-01T10:00:00Z` to `2011-06-01T14:00:00Z`:
If you don't pass the overflow=true parameter, you will get one schedule entry returned with a start of `2011-06-01T10:00:00Z` and end of `2011-06-01T14:00:00Z`.
If you do pass the `overflow` parameter, you will get one schedule entry returned with a start of `2011-06-01T00:00:00Z` and end of `2011-06-02T00:00:00Z`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

The time zone of the schedule (e.g Europe/Berlin).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layer

_Required_: No

_Type_: List of <a href="layer.md">Layer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restriction

_Required_: No

_Type_: List of <a href="restriction.md">Restriction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

