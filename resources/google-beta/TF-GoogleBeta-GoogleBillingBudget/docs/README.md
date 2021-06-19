# TF::GoogleBeta::GoogleBillingBudget

CloudFormation equivalent of google_billing_budget

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleBillingBudget",
    "Properties" : {
        "<a href="#billingaccount" title="BillingAccount">BillingAccount</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#allupdatesrule" title="AllUpdatesRule">AllUpdatesRule</a>" : <i>[ <a href="allupdatesruledefinition.md">AllUpdatesRuleDefinition</a>, ... ]</i>,
        "<a href="#amount" title="Amount">Amount</a>" : <i>[ <a href="amountdefinition.md">AmountDefinition</a>, ... ]</i>,
        "<a href="#budgetfilter" title="BudgetFilter">BudgetFilter</a>" : <i>[ <a href="budgetfilterdefinition.md">BudgetFilterDefinition</a>, ... ]</i>,
        "<a href="#thresholdrules" title="ThresholdRules">ThresholdRules</a>" : <i>[ <a href="thresholdrulesdefinition.md">ThresholdRulesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleBillingBudget
Properties:
    <a href="#billingaccount" title="BillingAccount">BillingAccount</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#allupdatesrule" title="AllUpdatesRule">AllUpdatesRule</a>: <i>
      - <a href="allupdatesruledefinition.md">AllUpdatesRuleDefinition</a></i>
    <a href="#amount" title="Amount">Amount</a>: <i>
      - <a href="amountdefinition.md">AmountDefinition</a></i>
    <a href="#budgetfilter" title="BudgetFilter">BudgetFilter</a>: <i>
      - <a href="budgetfilterdefinition.md">BudgetFilterDefinition</a></i>
    <a href="#thresholdrules" title="ThresholdRules">ThresholdRules</a>: <i>
      - <a href="thresholdrulesdefinition.md">ThresholdRulesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BillingAccount

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllUpdatesRule

_Required_: No

_Type_: List of <a href="allupdatesruledefinition.md">AllUpdatesRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Amount

_Required_: No

_Type_: List of <a href="amountdefinition.md">AmountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BudgetFilter

_Required_: No

_Type_: List of <a href="budgetfilterdefinition.md">BudgetFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdRules

_Required_: No

_Type_: List of <a href="thresholdrulesdefinition.md">ThresholdRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Name

Returns the <code>Name</code> value.

