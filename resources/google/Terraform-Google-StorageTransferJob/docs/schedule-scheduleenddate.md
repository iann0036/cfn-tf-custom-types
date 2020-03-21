# Terraform::Google::StorageTransferJob Schedule ScheduleEndDate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#day" title="Day">Day</a>" : <i>Double</i>,
    "<a href="#month" title="Month">Month</a>" : <i>Double</i>,
    "<a href="#year" title="Year">Year</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#day" title="Day">Day</a>: <i>Double</i>
<a href="#month" title="Month">Month</a>: <i>Double</i>
<a href="#year" title="Year">Year</a>: <i>Double</i>
</pre>

## Properties

#### Day

Day of month. Must be from 1 to 31 and valid for the year and month.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Month

Month of year. Must be from 1 to 12.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Year

Year of date. Must be from 1 to 9999.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

