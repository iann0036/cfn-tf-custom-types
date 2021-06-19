# TF::PagerDuty::RulesetRule

An [event rule](https://support.pagerduty.com/docs/rulesets#section-create-event-rules) allows you to set actions that should be taken on events that meet your designated rule criteria.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PagerDuty::RulesetRule",
    "Properties" : {
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#position" title="Position">Position</a>" : <i>Double</i>,
        "<a href="#ruleset" title="Ruleset">Ruleset</a>" : <i>String</i>,
        "<a href="#actions" title="Actions">Actions</a>" : <i>[ <a href="actionsdefinition.md">ActionsDefinition</a>, ... ]</i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="conditionsdefinition.md">ConditionsDefinition</a>, ... ]</i>,
        "<a href="#timeframe" title="TimeFrame">TimeFrame</a>" : <i>[ <a href="timeframedefinition.md">TimeFrameDefinition</a>, ... ]</i>,
        "<a href="#variable" title="Variable">Variable</a>" : <i>[ <a href="variabledefinition.md">VariableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PagerDuty::RulesetRule
Properties:
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#position" title="Position">Position</a>: <i>Double</i>
    <a href="#ruleset" title="Ruleset">Ruleset</a>: <i>String</i>
    <a href="#actions" title="Actions">Actions</a>: <i>
      - <a href="actionsdefinition.md">ActionsDefinition</a></i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="conditionsdefinition.md">ConditionsDefinition</a></i>
    <a href="#timeframe" title="TimeFrame">TimeFrame</a>: <i>
      - <a href="timeframedefinition.md">TimeFrameDefinition</a></i>
    <a href="#variable" title="Variable">Variable</a>: <i>
      - <a href="variabledefinition.md">VariableDefinition</a></i>
</pre>

## Properties

#### Disabled

Indicates whether the rule is disabled and would therefore not be evaluated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

Position/index of the rule within the ruleset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ruleset

The ID of the ruleset that the rule belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Actions

_Required_: No

_Type_: List of <a href="actionsdefinition.md">ActionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of <a href="conditionsdefinition.md">ConditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeFrame

_Required_: No

_Type_: List of <a href="timeframedefinition.md">TimeFrameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variable

_Required_: No

_Type_: List of <a href="variabledefinition.md">VariableDefinition</a>

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

