# TF::FortiOS::SwitchcontrollerPortpolicy

Configure port policy to be applied on the managed FortiSwitch ports through NAC device. Applies to FortiOS Version `>= 6.4.0`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerPortpolicy",
    "Properties" : {
        "<a href="#bounceportlink" title="BouncePortLink">BouncePortLink</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#fortilink" title="Fortilink">Fortilink</a>" : <i>String</i>,
        "<a href="#lldpprofile" title="LldpProfile">LldpProfile</a>" : <i>String</i>,
        "<a href="#n8021x" title="N8021x">N8021x</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#qospolicy" title="QosPolicy">QosPolicy</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#vlanpolicy" title="VlanPolicy">VlanPolicy</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerPortpolicy
Properties:
    <a href="#bounceportlink" title="BouncePortLink">BouncePortLink</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#fortilink" title="Fortilink">Fortilink</a>: <i>String</i>
    <a href="#lldpprofile" title="LldpProfile">LldpProfile</a>: <i>String</i>
    <a href="#n8021x" title="N8021x">N8021x</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#qospolicy" title="QosPolicy">QosPolicy</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#vlanpolicy" title="VlanPolicy">VlanPolicy</a>: <i>String</i>
</pre>

## Properties

#### BouncePortLink

Enable/disable bouncing (administratively bring the link down, up) of a switch port where this port policy is applied. Helps to clear and reassign VLAN from lldp-profile. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for the port policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fortilink

FortiLink interface for which this port policy belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpProfile

LLDP profile to be applied when using this port-policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### N8021x

802.1x security policy to be applied when using this port-policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Port policy name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosPolicy

QoS policy to be applied when using this port-policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanPolicy

VLAN policy to be applied when using this port-policy.

_Required_: No

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

#### Id

Returns the <code>Id</code> value.

