# TF::Alicloud::GaForwardingRule

CloudFormation equivalent of alicloud_ga_forwarding_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::GaForwardingRule",
    "Properties" : {
        "<a href="#acceleratorid" title="AcceleratorId">AcceleratorId</a>" : <i>String</i>,
        "<a href="#forwardingrulename" title="ForwardingRuleName">ForwardingRuleName</a>" : <i>String</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#ruleactions" title="RuleActions">RuleActions</a>" : <i>[ <a href="ruleactionsdefinition.md">RuleActionsDefinition</a>, ... ]</i>,
        "<a href="#ruleconditions" title="RuleConditions">RuleConditions</a>" : <i>[ <a href="ruleconditionsdefinition.md">RuleConditionsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::GaForwardingRule
Properties:
    <a href="#acceleratorid" title="AcceleratorId">AcceleratorId</a>: <i>String</i>
    <a href="#forwardingrulename" title="ForwardingRuleName">ForwardingRuleName</a>: <i>String</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#ruleactions" title="RuleActions">RuleActions</a>: <i>
      - <a href="ruleactionsdefinition.md">RuleActionsDefinition</a></i>
    <a href="#ruleconditions" title="RuleConditions">RuleConditions</a>: <i>
      - <a href="ruleconditionsdefinition.md">RuleConditionsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AcceleratorId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardingRuleName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleActions

_Required_: No

_Type_: List of <a href="ruleactionsdefinition.md">RuleActionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleConditions

_Required_: No

_Type_: List of <a href="ruleconditionsdefinition.md">RuleConditionsDefinition</a>

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

#### ForwardingRuleId

Returns the <code>ForwardingRuleId</code> value.

#### ForwardingRuleStatus

Returns the <code>ForwardingRuleStatus</code> value.

#### Id

Returns the <code>Id</code> value.

