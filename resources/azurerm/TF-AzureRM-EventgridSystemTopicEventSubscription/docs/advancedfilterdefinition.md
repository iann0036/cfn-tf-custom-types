# TF::AzureRM::EventgridSystemTopicEventSubscription AdvancedFilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#boolequals" title="BoolEquals">BoolEquals</a>" : <i>[ <a href="boolequalsdefinition.md">BoolEqualsDefinition</a>, ... ]</i>,
    "<a href="#numbergreaterthan" title="NumberGreaterThan">NumberGreaterThan</a>" : <i>[ <a href="numbergreaterthandefinition.md">NumberGreaterThanDefinition</a>, ... ]</i>,
    "<a href="#numbergreaterthanorequals" title="NumberGreaterThanOrEquals">NumberGreaterThanOrEquals</a>" : <i>[ <a href="numbergreaterthanorequalsdefinition.md">NumberGreaterThanOrEqualsDefinition</a>, ... ]</i>,
    "<a href="#numberin" title="NumberIn">NumberIn</a>" : <i>[ <a href="numberindefinition.md">NumberInDefinition</a>, ... ]</i>,
    "<a href="#numberlessthan" title="NumberLessThan">NumberLessThan</a>" : <i>[ <a href="numberlessthandefinition.md">NumberLessThanDefinition</a>, ... ]</i>,
    "<a href="#numberlessthanorequals" title="NumberLessThanOrEquals">NumberLessThanOrEquals</a>" : <i>[ <a href="numberlessthanorequalsdefinition.md">NumberLessThanOrEqualsDefinition</a>, ... ]</i>,
    "<a href="#numbernotin" title="NumberNotIn">NumberNotIn</a>" : <i>[ <a href="numbernotindefinition.md">NumberNotInDefinition</a>, ... ]</i>,
    "<a href="#stringbeginswith" title="StringBeginsWith">StringBeginsWith</a>" : <i>[ <a href="stringbeginswithdefinition.md">StringBeginsWithDefinition</a>, ... ]</i>,
    "<a href="#stringcontains" title="StringContains">StringContains</a>" : <i>[ <a href="stringcontainsdefinition.md">StringContainsDefinition</a>, ... ]</i>,
    "<a href="#stringendswith" title="StringEndsWith">StringEndsWith</a>" : <i>[ <a href="stringendswithdefinition.md">StringEndsWithDefinition</a>, ... ]</i>,
    "<a href="#stringin" title="StringIn">StringIn</a>" : <i>[ <a href="stringindefinition.md">StringInDefinition</a>, ... ]</i>,
    "<a href="#stringnotin" title="StringNotIn">StringNotIn</a>" : <i>[ <a href="stringnotindefinition.md">StringNotInDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#boolequals" title="BoolEquals">BoolEquals</a>: <i>
      - <a href="boolequalsdefinition.md">BoolEqualsDefinition</a></i>
<a href="#numbergreaterthan" title="NumberGreaterThan">NumberGreaterThan</a>: <i>
      - <a href="numbergreaterthandefinition.md">NumberGreaterThanDefinition</a></i>
<a href="#numbergreaterthanorequals" title="NumberGreaterThanOrEquals">NumberGreaterThanOrEquals</a>: <i>
      - <a href="numbergreaterthanorequalsdefinition.md">NumberGreaterThanOrEqualsDefinition</a></i>
<a href="#numberin" title="NumberIn">NumberIn</a>: <i>
      - <a href="numberindefinition.md">NumberInDefinition</a></i>
<a href="#numberlessthan" title="NumberLessThan">NumberLessThan</a>: <i>
      - <a href="numberlessthandefinition.md">NumberLessThanDefinition</a></i>
<a href="#numberlessthanorequals" title="NumberLessThanOrEquals">NumberLessThanOrEquals</a>: <i>
      - <a href="numberlessthanorequalsdefinition.md">NumberLessThanOrEqualsDefinition</a></i>
<a href="#numbernotin" title="NumberNotIn">NumberNotIn</a>: <i>
      - <a href="numbernotindefinition.md">NumberNotInDefinition</a></i>
<a href="#stringbeginswith" title="StringBeginsWith">StringBeginsWith</a>: <i>
      - <a href="stringbeginswithdefinition.md">StringBeginsWithDefinition</a></i>
<a href="#stringcontains" title="StringContains">StringContains</a>: <i>
      - <a href="stringcontainsdefinition.md">StringContainsDefinition</a></i>
<a href="#stringendswith" title="StringEndsWith">StringEndsWith</a>: <i>
      - <a href="stringendswithdefinition.md">StringEndsWithDefinition</a></i>
<a href="#stringin" title="StringIn">StringIn</a>: <i>
      - <a href="stringindefinition.md">StringInDefinition</a></i>
<a href="#stringnotin" title="StringNotIn">StringNotIn</a>: <i>
      - <a href="stringnotindefinition.md">StringNotInDefinition</a></i>
</pre>

## Properties

#### BoolEquals

_Required_: No

_Type_: List of <a href="boolequalsdefinition.md">BoolEqualsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberGreaterThan

_Required_: No

_Type_: List of <a href="numbergreaterthandefinition.md">NumberGreaterThanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberGreaterThanOrEquals

_Required_: No

_Type_: List of <a href="numbergreaterthanorequalsdefinition.md">NumberGreaterThanOrEqualsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberIn

_Required_: No

_Type_: List of <a href="numberindefinition.md">NumberInDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberLessThan

_Required_: No

_Type_: List of <a href="numberlessthandefinition.md">NumberLessThanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberLessThanOrEquals

_Required_: No

_Type_: List of <a href="numberlessthanorequalsdefinition.md">NumberLessThanOrEqualsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberNotIn

_Required_: No

_Type_: List of <a href="numbernotindefinition.md">NumberNotInDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringBeginsWith

_Required_: No

_Type_: List of <a href="stringbeginswithdefinition.md">StringBeginsWithDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringContains

_Required_: No

_Type_: List of <a href="stringcontainsdefinition.md">StringContainsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringEndsWith

_Required_: No

_Type_: List of <a href="stringendswithdefinition.md">StringEndsWithDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringIn

_Required_: No

_Type_: List of <a href="stringindefinition.md">StringInDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringNotIn

_Required_: No

_Type_: List of <a href="stringnotindefinition.md">StringNotInDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

