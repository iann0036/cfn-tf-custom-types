# TF::AVI::Wafpolicypsmgroup RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#matchcase" title="MatchCase">MatchCase</a>" : <i>String</i>,
    "<a href="#matchvaluemaxlength" title="MatchValueMaxLength">MatchValueMaxLength</a>" : <i>Double</i>,
    "<a href="#matchvaluepattern" title="MatchValuePattern">MatchValuePattern</a>" : <i>String</i>,
    "<a href="#matchvaluestringgroupkey" title="MatchValueStringGroupKey">MatchValueStringGroupKey</a>" : <i>String</i>,
    "<a href="#matchvaluestringgroupref" title="MatchValueStringGroupRef">MatchValueStringGroupRef</a>" : <i>String</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#paranoialevel" title="ParanoiaLevel">ParanoiaLevel</a>" : <i>String</i>,
    "<a href="#ruleid" title="RuleId">RuleId</a>" : <i>String</i>,
    "<a href="#matchelements" title="MatchElements">MatchElements</a>" : <i>[ <a href="matchelementsdefinition.md">MatchElementsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#matchcase" title="MatchCase">MatchCase</a>: <i>String</i>
<a href="#matchvaluemaxlength" title="MatchValueMaxLength">MatchValueMaxLength</a>: <i>Double</i>
<a href="#matchvaluepattern" title="MatchValuePattern">MatchValuePattern</a>: <i>String</i>
<a href="#matchvaluestringgroupkey" title="MatchValueStringGroupKey">MatchValueStringGroupKey</a>: <i>String</i>
<a href="#matchvaluestringgroupref" title="MatchValueStringGroupRef">MatchValueStringGroupRef</a>: <i>String</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#paranoialevel" title="ParanoiaLevel">ParanoiaLevel</a>: <i>String</i>
<a href="#ruleid" title="RuleId">RuleId</a>: <i>String</i>
<a href="#matchelements" title="MatchElements">MatchElements</a>: <i>
      - <a href="matchelementsdefinition.md">MatchElementsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchCase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchValueMaxLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchValuePattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchValueStringGroupKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchValueStringGroupRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParanoiaLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchElements

_Required_: No

_Type_: List of <a href="matchelementsdefinition.md">MatchElementsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

