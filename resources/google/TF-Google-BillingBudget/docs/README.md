# TF::Google::BillingBudget

Budget configuration for a billing account.


To get more information about Budget, see:

* [API documentation](https://cloud.google.com/billing/docs/reference/budget/rest/v1/billingAccounts.budgets)
* How-to Guides
    * [Creating a budget](https://cloud.google.com/billing/docs/how-to/budgets)

~> **Warning:** If you are using User ADCs (Application Default Credentials) with this resource,
you must specify a `billing_project` and set `user_project_override` to true
in the provider configuration. Otherwise the Billing Budgets API will return a 403 error.
Your account must have the `serviceusage.services.use` permission on the
`billing_project` you defined.

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=billing_budget_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::BillingBudget",
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
Type: TF::Google::BillingBudget
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

