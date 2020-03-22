# Terraform::VSphere::Vnic

Provides a VMware vSphere vnic resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::Vnic",
    "Properties" : {
        "<a href="#distributedportgroup" title="DistributedPortGroup">DistributedPortGroup</a>" : <i>String</i>,
        "<a href="#distributedswitchport" title="DistributedSwitchPort">DistributedSwitchPort</a>" : <i>String</i>,
        "<a href="#host" title="Host">Host</a>" : <i>String</i>,
        "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#netstack" title="Netstack">Netstack</a>" : <i>String</i>,
        "<a href="#portgroup" title="Portgroup">Portgroup</a>" : <i>String</i>,
        "<a href="#ipv4" title="Ipv4">Ipv4</a>" : <i>[ <a href="ipv4.md">Ipv4</a>, ... ]</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>[ <a href="ipv6.md">Ipv6</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::Vnic
Properties:
    <a href="#distributedportgroup" title="DistributedPortGroup">DistributedPortGroup</a>: <i>String</i>
    <a href="#distributedswitchport" title="DistributedSwitchPort">DistributedSwitchPort</a>: <i>String</i>
    <a href="#host" title="Host">Host</a>: <i>String</i>
    <a href="#mac" title="Mac">Mac</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#netstack" title="Netstack">Netstack</a>: <i>String</i>
    <a href="#portgroup" title="Portgroup">Portgroup</a>: <i>String</i>
    <a href="#ipv4" title="Ipv4">Ipv4</a>: <i>
      - <a href="ipv4.md">Ipv4</a></i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>
      - <a href="ipv6.md">Ipv6</a></i>
</pre>

## Properties

#### DistributedPortGroup

Key of the distributed portgroup the nic will connect to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributedSwitchPort

UUID of the DVSwitch the nic will be attached to. Do not set if you set portgroup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

MAC address of the interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

MTU of the interface.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netstack

TCP/IP stack setting for this interface. Possible values are 'defaultTcpipStack', 'vmotion', 'vSphereProvisioning'. Changing this will force the creation of a new interface since it's not possible to change the stack once it gets created. (Default: `defaultTcpipStack`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Portgroup

Portgroup to attach the nic to. Do not set if you set distributed_switch_port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4

_Required_: No

_Type_: List of <a href="ipv4.md">Ipv4</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: List of <a href="ipv6.md">Ipv6</a>

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

