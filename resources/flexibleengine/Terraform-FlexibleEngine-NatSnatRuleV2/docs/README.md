# Terraform::FlexibleEngine::NatSnatRuleV2

Manages a V2 snat rule resource within FlexibleEngine Nat

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::NatSnatRuleV2",
    "Properties" : {
        "<a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>" : <i>String</i>,
        "<a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::NatSnatRuleV2
Properties:
    <a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>: <i>String</i>
    <a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### FloatingIpId

ID of the floating ip this snat rule connets to.
Changing this creates a new snat rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatGatewayId

ID of the nat gateway this snat rule belongs to.
Changing this creates a new snat rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

ID of the network this snat rule connects to.
This parameter and `cidr` are alternative. Changing this creates a new snat rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 nat client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new snat rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

