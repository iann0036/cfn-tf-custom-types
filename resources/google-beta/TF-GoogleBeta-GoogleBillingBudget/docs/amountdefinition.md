# TF::GoogleBeta::GoogleBillingBudget AmountDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#lastperiodamount" title="LastPeriodAmount">LastPeriodAmount</a>" : <i>Boolean</i>,
    "<a href="#specifiedamount" title="SpecifiedAmount">SpecifiedAmount</a>" : <i>[ <a href="specifiedamountdefinition.md">SpecifiedAmountDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#lastperiodamount" title="LastPeriodAmount">LastPeriodAmount</a>: <i>Boolean</i>
<a href="#specifiedamount" title="SpecifiedAmount">SpecifiedAmount</a>: <i>
      - <a href="specifiedamountdefinition.md">SpecifiedAmountDefinition</a></i>
</pre>

## Properties

#### LastPeriodAmount

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecifiedAmount

_Required_: No

_Type_: List of <a href="specifiedamountdefinition.md">SpecifiedAmountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

