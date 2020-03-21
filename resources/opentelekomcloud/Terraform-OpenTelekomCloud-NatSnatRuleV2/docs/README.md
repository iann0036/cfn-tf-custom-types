# Terraform::OpenTelekomCloud::NatSnatRuleV2

Manages a V2 snat rule resource within OpenTelekomCloud Nat

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::NatSnatRuleV2",
    "Properties" : {
        "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
        "<a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>" : <i>String</i>,
        "<a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::NatSnatRuleV2
Properties:
    <a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
    <a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>: <i>String</i>
    <a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sourcetype" title="SourceType">SourceType</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Cidr

Specifies CIDR, which can be in the format of a network segment or
a host IP address. This parameter and network_id are alternative. If the value of
source_type is 0, the CIDR block must be a subset of the VPC subnet CIDR block. If
the value of source_type is 1, the CIDR block must be a CIDR block of Direct Connect
and cannot conflict with the VPC CIDR blocks. Changing this creates a new snat rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

ID of the network this snat rule connects to. This parameter
and cidr are alternative. Changing this creates a new snat rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

0: Either network_id or cidr can be specified in a VPC. 1:
Only cidr can be specified over a dedicated network. Changing this creates a new snat rule.

_Required_: No

_Type_: Double

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

