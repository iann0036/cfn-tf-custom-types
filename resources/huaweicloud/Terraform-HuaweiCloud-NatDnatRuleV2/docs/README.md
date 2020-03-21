# Terraform::HuaweiCloud::NatDnatRuleV2

CloudFormation equivalent of huaweicloud_nat_dnat_rule_v2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::NatDnatRuleV2",
    "Properties" : {
        "<a href="#externalserviceport" title="ExternalServicePort">ExternalServicePort</a>" : <i>Double</i>,
        "<a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>" : <i>String</i>,
        "<a href="#internalserviceport" title="InternalServicePort">InternalServicePort</a>" : <i>Double</i>,
        "<a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>" : <i>String</i>,
        "<a href="#portid" title="PortId">PortId</a>" : <i>String</i>,
        "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::NatDnatRuleV2
Properties:
    <a href="#externalserviceport" title="ExternalServicePort">ExternalServicePort</a>: <i>Double</i>
    <a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>: <i>String</i>
    <a href="#internalserviceport" title="InternalServicePort">InternalServicePort</a>: <i>Double</i>
    <a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>: <i>String</i>
    <a href="#portid" title="PortId">PortId</a>: <i>String</i>
    <a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### ExternalServicePort

Specifies port used by ECSs or
BMSs to provide services for external systems.
Changing this creates a new dnat rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIpId

Specifies the ID of the floating IP address.
Changing this creates a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalServicePort

Specifies port used by ECSs or BMSs
to provide services for external systems. Changing this creates a new resource.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatGatewayId

ID of the nat gateway this dnat rule belongs to.
Changing this creates a new dnat rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortId

Specifies the port ID of an ECS or a BMS.
This parameter and private_ip are alternative. Changing this creates a
new dnat rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

Specifies the private IP address of a
user, for example, the IP address of a VPC for dedicated connection.
This parameter and port_id are alternative.
Changing this creates a new dnat rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Specifies the protocol type. Currently,
TCP, UDP, and ANY are supported.
Changing this creates a new dnat rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### FloatingIpAddress

Returns the <code>FloatingIpAddress</code> value.

#### Status

Returns the <code>Status</code> value.

#### TenantId

Returns the <code>TenantId</code> value.

