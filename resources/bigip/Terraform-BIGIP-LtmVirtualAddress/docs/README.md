# Terraform::BIGIP::LtmVirtualAddress

`bigip_ltm_virtual_address` Configures Virtual Server

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmVirtualAddress",
    "Properties" : {
        "<a href="#advertizeroute" title="AdvertizeRoute">AdvertizeRoute</a>" : <i>Boolean</i>,
        "<a href="#arp" title="Arp">Arp</a>" : <i>Boolean</i>,
        "<a href="#autodelete" title="AutoDelete">AutoDelete</a>" : <i>Boolean</i>,
        "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#icmpecho" title="IcmpEcho">IcmpEcho</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#trafficgroup" title="TrafficGroup">TrafficGroup</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmVirtualAddress
Properties:
    <a href="#advertizeroute" title="AdvertizeRoute">AdvertizeRoute</a>: <i>Boolean</i>
    <a href="#arp" title="Arp">Arp</a>: <i>Boolean</i>
    <a href="#autodelete" title="AutoDelete">AutoDelete</a>: <i>Boolean</i>
    <a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#icmpecho" title="IcmpEcho">IcmpEcho</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#trafficgroup" title="TrafficGroup">TrafficGroup</a>: <i>String</i>
</pre>

## Properties

#### AdvertizeRoute

Enabled dynamic routing of the address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arp

Enable or disable ARP for the virtual address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoDelete

Automatically delete the virtual address with the virtual server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLimit

Max number of connections for virtual address.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enable or disable the virtual address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpEcho

Enable/Disable ICMP response to the virtual address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the virtual address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficGroup

Specify the partition and traffic group.

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

