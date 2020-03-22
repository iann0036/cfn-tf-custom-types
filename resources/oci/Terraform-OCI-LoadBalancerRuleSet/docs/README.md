# Terraform::OCI::LoadBalancerRuleSet

This resource provides the Rule Set resource in Oracle Cloud Infrastructure Load Balancer service.

Creates a new rule set associated with the specified load balancer. For more information, see
[Managing Rule Sets](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/managingrulesets.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::LoadBalancerRuleSet",
    "Properties" : {
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#items" title="Items">Items</a>" : <i>[ <a href="items.md">Items</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="conditions.md">Conditions</a>, ... ]</i>,
        "<a href="#redirecturi" title="RedirectUri">RedirectUri</a>" : <i>[ <a href="redirecturi.md">RedirectUri</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::LoadBalancerRuleSet
Properties:
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#items" title="Items">Items</a>: <i>
      - <a href="items.md">Items</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="conditions.md">Conditions</a></i>
    <a href="#redirecturi" title="RedirectUri">RedirectUri</a>: <i>
      - <a href="redirecturi.md">RedirectUri</a></i>
</pre>

## Properties

#### LoadBalancerId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the specified load balancer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name for this set of rules. It must be unique and it cannot be changed. Avoid entering confidential information.  Example: `example_rule_set`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Items

_Required_: No

_Type_: List of <a href="items.md">Items</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of <a href="conditions.md">Conditions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUri

_Required_: No

_Type_: List of <a href="redirecturi.md">RedirectUri</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

