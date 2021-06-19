# TF::BIGIP::LtmVirtualAddress

`bigip_ltm_virtual_address` Configures Virtual Server

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/virtual_server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::LtmVirtualAddress",
    "Properties" : {
        "<a href="#advertizeroute" title="AdvertizeRoute">AdvertizeRoute</a>" : <i>String</i>,
        "<a href="#arp" title="Arp">Arp</a>" : <i>Boolean</i>,
        "<a href="#autodelete" title="AutoDelete">AutoDelete</a>" : <i>Boolean</i>,
        "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#icmpecho" title="IcmpEcho">IcmpEcho</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#trafficgroup" title="TrafficGroup">TrafficGroup</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::LtmVirtualAddress
Properties:
    <a href="#advertizeroute" title="AdvertizeRoute">AdvertizeRoute</a>: <i>String</i>
    <a href="#arp" title="Arp">Arp</a>: <i>Boolean</i>
    <a href="#autodelete" title="AutoDelete">AutoDelete</a>: <i>Boolean</i>
    <a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#icmpecho" title="IcmpEcho">IcmpEcho</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#trafficgroup" title="TrafficGroup">TrafficGroup</a>: <i>String</i>
</pre>

## Properties

#### AdvertizeRoute

Enabled dynamic routing of the address ( In versions prior to BIG-IP 13.0.0 HF1, you can configure the Route Advertisement option for a virtual address to be either Enabled or Disabled only. Beginning with BIG-IP 13.0.0 HF1, F5 added more settings for the Route Advertisement option. In addition, the Enabled setting is deprecated and replaced by the Selective setting. For more information, please look into KB article https://support.f5.com/csp/article/K85543242 ).

_Required_: No

_Type_: String

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

Specifies how the system sends responses to ICMP echo requests on a per-virtual address basis.

_Required_: No

_Type_: String

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

#### Id

Returns the <code>Id</code> value.

