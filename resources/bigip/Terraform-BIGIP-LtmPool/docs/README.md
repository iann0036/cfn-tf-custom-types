# Terraform::BIGIP::LtmPool

CloudFormation equivalent of bigip_ltm_pool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmPool",
    "Properties" : {
        "<a href="#allownat" title="AllowNat">AllowNat</a>" : <i>String</i>,
        "<a href="#allowsnat" title="AllowSnat">AllowSnat</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#loadbalancingmode" title="LoadBalancingMode">LoadBalancingMode</a>" : <i>String</i>,
        "<a href="#monitors" title="Monitors">Monitors</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reselecttries" title="ReselectTries">ReselectTries</a>" : <i>Double</i>,
        "<a href="#servicedownaction" title="ServiceDownAction">ServiceDownAction</a>" : <i>String</i>,
        "<a href="#slowramptime" title="SlowRampTime">SlowRampTime</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmPool
Properties:
    <a href="#allownat" title="AllowNat">AllowNat</a>: <i>String</i>
    <a href="#allowsnat" title="AllowSnat">AllowSnat</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#loadbalancingmode" title="LoadBalancingMode">LoadBalancingMode</a>: <i>String</i>
    <a href="#monitors" title="Monitors">Monitors</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reselecttries" title="ReselectTries">ReselectTries</a>: <i>Double</i>
    <a href="#servicedownaction" title="ServiceDownAction">ServiceDownAction</a>: <i>String</i>
    <a href="#slowramptime" title="SlowRampTime">SlowRampTime</a>: <i>Double</i>
</pre>

## Properties

#### AllowNat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSnat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitors

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReselectTries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDownAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlowRampTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

