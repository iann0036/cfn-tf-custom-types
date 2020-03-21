# Terraform::HuaweiCloud::CesAlarmrule Condition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>" : <i>String</i>,
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
    "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
    "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>: <i>String</i>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#filter" title="Filter">Filter</a>: <i>String</i>
<a href="#period" title="Period">Period</a>: <i>Double</i>
<a href="#unit" title="Unit">Unit</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>Double</i>
</pre>

## Properties

#### ComparisonOperator

Specifies the comparison condition of alarm
thresholds. The value can be >, =, <, >=, or <=.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Count

Specifies the number of consecutive occurrence times.
The value ranges from 1 to 5.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

Specifies the data rollup methods. The value can be
max, min, average, sum, and vaiance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

Specifies the alarm checking period in seconds. The
value can be 1, 300, 1200, 3600, 14400, and 86400.
Note: If period is set to 1, the raw metric data is used to determine
whether to generate an alarm.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

Specifies the data unit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

Specifies the alarm threshold. The value ranges from
0 to Number of 1.7976931348623157e+308.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

