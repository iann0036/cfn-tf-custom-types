# TF::AzureRM::MssqlDatabase LongTermRetentionPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#monthlyretention" title="MonthlyRetention">MonthlyRetention</a>" : <i>String</i>,
    "<a href="#weekofyear" title="WeekOfYear">WeekOfYear</a>" : <i>Double</i>,
    "<a href="#weeklyretention" title="WeeklyRetention">WeeklyRetention</a>" : <i>String</i>,
    "<a href="#yearlyretention" title="YearlyRetention">YearlyRetention</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#monthlyretention" title="MonthlyRetention">MonthlyRetention</a>: <i>String</i>
<a href="#weekofyear" title="WeekOfYear">WeekOfYear</a>: <i>Double</i>
<a href="#weeklyretention" title="WeeklyRetention">WeeklyRetention</a>: <i>String</i>
<a href="#yearlyretention" title="YearlyRetention">YearlyRetention</a>: <i>String</i>
</pre>

## Properties

#### MonthlyRetention

The monthly retention policy for an LTR backup in an ISO 8601 format. Valid value is between 1 to 120 months. e.g. `P1Y`, `P1M`, `P4W` or `P30D`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeekOfYear

The week of year to take the yearly backup in an ISO 8601 format. Value has to be between `1` and `52`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklyRetention

The weekly retention policy for an LTR backup in an ISO 8601 format. Valid value is between 1 to 520 weeks. e.g. `P1Y`, `P1M`, `P1W` or `P7D`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YearlyRetention

The yearly retention policy for an LTR backup in an ISO 8601 format. Valid value is between 1 to 10 years. e.g. `P1Y`, `P12M`, `P52W` or `P365D`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

