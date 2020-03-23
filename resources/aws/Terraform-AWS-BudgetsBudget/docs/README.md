# Terraform::AWS::BudgetsBudget

Provides a budgets budget resource. Budgets use the cost visualisation provided by Cost Explorer to show you the status of your budgets, to provide forecasts of your estimated costs, and to track your AWS usage, including your free tier usage.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::BudgetsBudget",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#budgettype" title="BudgetType">BudgetType</a>" : <i>String</i>,
        "<a href="#costfilters" title="CostFilters">CostFilters</a>" : <i>[ <a href="costfilters.md">CostFilters</a>, ... ]</i>,
        "<a href="#limitamount" title="LimitAmount">LimitAmount</a>" : <i>String</i>,
        "<a href="#limitunit" title="LimitUnit">LimitUnit</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#timeperiodend" title="TimePeriodEnd">TimePeriodEnd</a>" : <i>String</i>,
        "<a href="#timeperiodstart" title="TimePeriodStart">TimePeriodStart</a>" : <i>String</i>,
        "<a href="#timeunit" title="TimeUnit">TimeUnit</a>" : <i>String</i>,
        "<a href="#costtypes" title="CostTypes">CostTypes</a>" : <i>[ <a href="costtypes.md">CostTypes</a>, ... ]</i>,
        "<a href="#notification" title="Notification">Notification</a>" : <i>[ <a href="notification.md">Notification</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::BudgetsBudget
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#budgettype" title="BudgetType">BudgetType</a>: <i>String</i>
    <a href="#costfilters" title="CostFilters">CostFilters</a>: <i>
      - <a href="costfilters.md">CostFilters</a></i>
    <a href="#limitamount" title="LimitAmount">LimitAmount</a>: <i>String</i>
    <a href="#limitunit" title="LimitUnit">LimitUnit</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#timeperiodend" title="TimePeriodEnd">TimePeriodEnd</a>: <i>String</i>
    <a href="#timeperiodstart" title="TimePeriodStart">TimePeriodStart</a>: <i>String</i>
    <a href="#timeunit" title="TimeUnit">TimeUnit</a>: <i>String</i>
    <a href="#costtypes" title="CostTypes">CostTypes</a>: <i>
      - <a href="costtypes.md">CostTypes</a></i>
    <a href="#notification" title="Notification">Notification</a>: <i>
      - <a href="notification.md">Notification</a></i>
</pre>

## Properties

#### AccountId

The ID of the target account for budget. Will use current user's account_id by default if omitted.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BudgetType

Whether this budget tracks monetary cost or usage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CostFilters

Map of [CostFilters](#CostFilters) key/value pairs to apply to the budget.

_Required_: No

_Type_: List of <a href="costfilters.md">CostFilters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitAmount

The amount of cost or usage being measured for a budget.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitUnit

The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of a budget. Unique within accounts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

The prefix of the name of a budget. Unique within accounts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimePeriodEnd

The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimePeriodStart

The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeUnit

The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CostTypes

_Required_: No

_Type_: List of <a href="costtypes.md">CostTypes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notification

_Required_: No

_Type_: List of <a href="notification.md">Notification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

