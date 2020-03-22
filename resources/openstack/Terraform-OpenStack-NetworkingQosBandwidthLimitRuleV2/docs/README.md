# Terraform::OpenStack::NetworkingQosBandwidthLimitRuleV2

Manages a V2 Neutron QoS bandwidth limit rule resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::NetworkingQosBandwidthLimitRuleV2",
    "Properties" : {
        "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
        "<a href="#maxburstkbps" title="MaxBurstKbps">MaxBurstKbps</a>" : <i>Double</i>,
        "<a href="#maxkbps" title="MaxKbps">MaxKbps</a>" : <i>Double</i>,
        "<a href="#qospolicyid" title="QosPolicyId">QosPolicyId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::NetworkingQosBandwidthLimitRuleV2
Properties:
    <a href="#direction" title="Direction">Direction</a>: <i>String</i>
    <a href="#maxburstkbps" title="MaxBurstKbps">MaxBurstKbps</a>: <i>Double</i>
    <a href="#maxkbps" title="MaxKbps">MaxKbps</a>: <i>Double</i>
    <a href="#qospolicyid" title="QosPolicyId">QosPolicyId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Direction

The direction of traffic. Defaults to "egress". Changing this updates the direction of the
existing QoS bandwidth limit rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBurstKbps

The maximum burst size in kilobits of a QoS bandwidth limit rule. Changing this updates the
maximum burst size in kilobits of the existing QoS bandwidth limit rule.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxKbps

The maximum kilobits per second of a QoS bandwidth limit rule. Changing this updates the
maximum kilobits per second of the existing QoS bandwidth limit rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosPolicyId

The QoS policy reference. Changing this creates a new QoS bandwidth limit rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS bandwidth limit rule. If omitted, the
`region` argument of the provider is used. Changing this creates a new QoS bandwidth limit rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

