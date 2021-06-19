# TF::TencentCloud::MonitorPolicyGroup

Provides a policy group resource for monitor.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::MonitorPolicyGroup",
    "Properties" : {
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#isunionrule" title="IsUnionRule">IsUnionRule</a>" : <i>Double</i>,
        "<a href="#policyviewname" title="PolicyViewName">PolicyViewName</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#remark" title="Remark">Remark</a>" : <i>String</i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="conditionsdefinition.md">ConditionsDefinition</a>, ... ]</i>,
        "<a href="#eventconditions" title="EventConditions">EventConditions</a>" : <i>[ <a href="eventconditionsdefinition.md">EventConditionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::MonitorPolicyGroup
Properties:
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#isunionrule" title="IsUnionRule">IsUnionRule</a>: <i>Double</i>
    <a href="#policyviewname" title="PolicyViewName">PolicyViewName</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#remark" title="Remark">Remark</a>: <i>String</i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="conditionsdefinition.md">ConditionsDefinition</a></i>
    <a href="#eventconditions" title="EventConditions">EventConditions</a>: <i>
      - <a href="eventconditionsdefinition.md">EventConditionsDefinition</a></i>
</pre>

## Properties

#### GroupName

Policy group name, length should between 1 and 20.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsUnionRule

The and or relation of indicator alarm rule. Valid values: `0`, `1`. `0` represents or rule (if any rule is met, the alarm will be raised), `1` represents and rule (if all rules are met, the alarm will be raised).The default is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyViewName

Policy view name, eg:`cvm_device`,`BANDWIDTHPACKAGE`, refer to `data.tencentcloud_monitor_policy_conditions(policy_view_name)`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project id to which the policy group belongs, default is `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remark

Policy group's remark information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of <a href="conditionsdefinition.md">ConditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventConditions

_Required_: No

_Type_: List of <a href="eventconditionsdefinition.md">EventConditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BindingObjects

Returns the <code>BindingObjects</code> value.

#### DimensionGroup

Returns the <code>DimensionGroup</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastEditUin

Returns the <code>LastEditUin</code> value.

#### Receivers

Returns the <code>Receivers</code> value.

#### SupportRegions

Returns the <code>SupportRegions</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

