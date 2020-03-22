# Terraform::AWS::BudgetsBudget

CloudFormation equivalent of aws_budgets_budget

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BudgetType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CostFilters

_Required_: No

_Type_: List of <a href="costfilters.md">CostFilters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitAmount

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitUnit

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimePeriodEnd

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimePeriodStart

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeUnit

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

