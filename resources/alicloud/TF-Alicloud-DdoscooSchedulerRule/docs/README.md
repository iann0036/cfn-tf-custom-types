# TF::Alicloud::DdoscooSchedulerRule

Provides a DdosCoo Scheduler Rule resource. For information about DdosCoo Scheduler Rule and how to use it, see[What is DdosCoo Scheduler Rule](https://www.alibabacloud.com/help/en/doc-detail/157481.htm).

-> **NOTE:** Available in 1.86.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::DdoscooSchedulerRule",
    "Properties" : {
        "<a href="#param" title="Param">Param</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#rulename" title="RuleName">RuleName</a>" : <i>String</i>,
        "<a href="#ruletype" title="RuleType">RuleType</a>" : <i>Double</i>,
        "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rulesdefinition.md">RulesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::DdoscooSchedulerRule
Properties:
    <a href="#param" title="Param">Param</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#rulename" title="RuleName">RuleName</a>: <i>String</i>
    <a href="#ruletype" title="RuleType">RuleType</a>: <i>Double</i>
    <a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rulesdefinition.md">RulesDefinition</a></i>
</pre>

## Properties

#### Param

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The ID of the resource group to which the anti-DDoS pro instance belongs in resource management. By default, no value is specified, indicating that the domains in the default resource group are listed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleName

The name of the rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleType

The rule type. Valid values:
`2`: tiered protection.
`3`: globalization acceleration.
`6`: Cloud product interaction.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rulesdefinition.md">RulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Cname

Returns the <code>Cname</code> value.

#### Id

Returns the <code>Id</code> value.

