# TF::GoogleBeta::GoogleBillingBudget BudgetFilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#credittypes" title="CreditTypes">CreditTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#credittypestreatment" title="CreditTypesTreatment">CreditTypesTreatment</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
    "<a href="#projects" title="Projects">Projects</a>" : <i>[ String, ... ]</i>,
    "<a href="#services" title="Services">Services</a>" : <i>[ String, ... ]</i>,
    "<a href="#subaccounts" title="Subaccounts">Subaccounts</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#credittypes" title="CreditTypes">CreditTypes</a>: <i>
      - String</i>
<a href="#credittypestreatment" title="CreditTypesTreatment">CreditTypesTreatment</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
<a href="#projects" title="Projects">Projects</a>: <i>
      - String</i>
<a href="#services" title="Services">Services</a>: <i>
      - String</i>
<a href="#subaccounts" title="Subaccounts">Subaccounts</a>: <i>
      - String</i>
</pre>

## Properties

#### CreditTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreditTypesTreatment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Projects

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subaccounts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

