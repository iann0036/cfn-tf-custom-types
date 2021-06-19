# TF::Thunder::IpNatPool

`thunder_ip_nat_pool` Provides details about thunder ip nat pool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::IpNatPool",
    "Properties" : {
        "<a href="#chunknetmask" title="ChunkNetmask">ChunkNetmask</a>" : <i>String</i>,
        "<a href="#endaddress" title="EndAddress">EndAddress</a>" : <i>String</i>,
        "<a href="#ethernet" title="Ethernet">Ethernet</a>" : <i>Double</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#iprr" title="IpRr">IpRr</a>" : <i>Double</i>,
        "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
        "<a href="#poolname" title="PoolName">PoolName</a>" : <i>String</i>,
        "<a href="#portoverload" title="PortOverload">PortOverload</a>" : <i>Double</i>,
        "<a href="#scaleoutdeviceid" title="ScaleoutDeviceId">ScaleoutDeviceId</a>" : <i>Double</i>,
        "<a href="#startaddress" title="StartAddress">StartAddress</a>" : <i>String</i>,
        "<a href="#useifip" title="UseIfIp">UseIfIp</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vrid" title="Vrid">Vrid</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::IpNatPool
Properties:
    <a href="#chunknetmask" title="ChunkNetmask">ChunkNetmask</a>: <i>String</i>
    <a href="#endaddress" title="EndAddress">EndAddress</a>: <i>String</i>
    <a href="#ethernet" title="Ethernet">Ethernet</a>: <i>Double</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#iprr" title="IpRr">IpRr</a>: <i>Double</i>
    <a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
    <a href="#poolname" title="PoolName">PoolName</a>: <i>String</i>
    <a href="#portoverload" title="PortOverload">PortOverload</a>: <i>Double</i>
    <a href="#scaleoutdeviceid" title="ScaleoutDeviceId">ScaleoutDeviceId</a>: <i>Double</i>
    <a href="#startaddress" title="StartAddress">StartAddress</a>: <i>String</i>
    <a href="#useifip" title="UseIfIp">UseIfIp</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vrid" title="Vrid">Vrid</a>: <i>Double</i>
</pre>

## Properties

#### ChunkNetmask

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndAddress

Configure end IP address of NAT pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ethernet

Ethernet interface.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

Configure gateway IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRr

Use IP address round-robin behavior.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

Configure mask for pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolName

Specify pool name or pool group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortOverload

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleoutDeviceId

Configure Scaleout device id to which this NAT pool is to be bound (Specify Scaleout device id).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartAddress

Configure start IP address of NAT pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseIfIp

Use Interface IP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrid

Configure VRRP-A vrid (Specify ha VRRP-A vrid).

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

#### Id

Returns the <code>Id</code> value.

