# TF::ILert::EscalationPolicy

An [escalation policy](https://api.ilert.com/api-docs/#tag/Escalation-Policies) connects an alert source with the users that are responsible for this alert source. It defines which users or on-call schedules should be notified when an incident is created.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ILert::EscalationPolicy",
    "Properties" : {
        "<a href="#frequency" title="Frequency">Frequency</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#repeating" title="Repeating">Repeating</a>" : <i>Boolean</i>,
        "<a href="#teams" title="Teams">Teams</a>" : <i>[ Double, ... ]</i>,
        "<a href="#escalationrule" title="EscalationRule">EscalationRule</a>" : <i>[ <a href="escalationruledefinition.md">EscalationRuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ILert::EscalationPolicy
Properties:
    <a href="#frequency" title="Frequency">Frequency</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#repeating" title="Repeating">Repeating</a>: <i>Boolean</i>
    <a href="#teams" title="Teams">Teams</a>: <i>
      - Double</i>
    <a href="#escalationrule" title="EscalationRule">EscalationRule</a>: <i>
      - <a href="escalationruledefinition.md">EscalationRuleDefinition</a></i>
</pre>

## Properties

#### Frequency

The number of times the escalation policy will repeat after reaching the end of its escalation. This option is allowed if `repeating` is `true`. Default: `1`.
- `escalation_rule` - (Optional) One or more [escalation rule](#escalation-rule-arguments) blocks.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the escalation policy.
- `repeating` - (Optional) Indicates whether or not the escalation policy will repeat. Default: `true`.
- `frequency` - (Optional) The number of times the escalation policy will repeat after reaching the end of its escalation. This option is allowed if `repeating` is `true`. Default: `1`.
- `escalation_rule` - (Optional) One or more [escalation rule](#escalation-rule-arguments) blocks.
- `teams` - (Optional) A list of related team ids.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repeating

Indicates whether or not the escalation policy will repeat. Default: `true`.
- `frequency` - (Optional) The number of times the escalation policy will repeat after reaching the end of its escalation. This option is allowed if `repeating` is `true`. Default: `1`.
- `escalation_rule` - (Optional) One or more [escalation rule](#escalation-rule-arguments) blocks.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Teams

A list of related team ids.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscalationRule

_Required_: No

_Type_: List of <a href="escalationruledefinition.md">EscalationRuleDefinition</a>

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

