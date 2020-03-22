# Terraform::PagerDuty::EventRule

An [event rule](https://v2.developer.pagerduty.com/docs/global-event-rules-api) determines what happens to an event that is sent to PagerDuty by monitoring tools and other integrations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PagerDuty::EventRule",
    "Properties" : {
        "<a href="#actionjson" title="ActionJson">ActionJson</a>" : <i>String</i>,
        "<a href="#advancedconditionjson" title="AdvancedConditionJson">AdvancedConditionJson</a>" : <i>String</i>,
        "<a href="#conditionjson" title="ConditionJson">ConditionJson</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PagerDuty::EventRule
Properties:
    <a href="#actionjson" title="ActionJson">ActionJson</a>: <i>String</i>
    <a href="#advancedconditionjson" title="AdvancedConditionJson">AdvancedConditionJson</a>: <i>String</i>
    <a href="#conditionjson" title="ConditionJson">ConditionJson</a>: <i>String</i>
</pre>

## Properties

#### ActionJson

A list of one or more actions for each rule. Each action within the list is itself a list.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedConditionJson

Contains a list of specific conditions including `active-between`,`scheduled-weekly`, and `frequency-over`. The first element in the list is the label for the condition, followed by a list of values for the specific condition. For more details on these conditions see [Advanced Condition](https://v2.developer.pagerduty.com/docs/global-event-rules-api#section-advanced-condition) in the PagerDuty API documentation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionJson

Contains a list of conditions. The first field in the list is `and` or `or`, followed by a list of operators and values.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CatchAll

Returns the <code>CatchAll</code> value.

#### Id

Returns the <code>Id</code> value.

