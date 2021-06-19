# TF::CloudEOS::Wan

The `cloudeos_wan` resource is used to provide attributes for the underlay and overlay connectivity
amongst Edges and Route Reflectors which are part of single WAN Network. In a traditional network topology,
a WAN Network includes multiple site/branch/cloud Edges connected through Ipsec VPN and/or private connects.
Similarly here, we have extended that concept which allows you to connect multiple clouds and regions
in a single WAN fabric.

The Edge/RR VPC and Edge CloudEOS router associate with a WAN using its `name`.
It is also possible to create multiple isolated WAN fabrics by creating multiple `cloudeos_wan` resources
and then associating the WAN name to the corresponding resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CloudEOS::Wan",
    "Properties" : {
        "<a href="#cvcontainername" title="CvContainerName">CvContainerName</a>" : <i>String</i>,
        "<a href="#edgetoedgededicatedconnect" title="EdgeToEdgeDedicatedConnect">EdgeToEdgeDedicatedConnect</a>" : <i>Boolean</i>,
        "<a href="#edgetoedgeigw" title="EdgeToEdgeIgw">EdgeToEdgeIgw</a>" : <i>Boolean</i>,
        "<a href="#edgetoedgepeering" title="EdgeToEdgePeering">EdgeToEdgePeering</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#topologyname" title="TopologyName">TopologyName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CloudEOS::Wan
Properties:
    <a href="#cvcontainername" title="CvContainerName">CvContainerName</a>: <i>String</i>
    <a href="#edgetoedgededicatedconnect" title="EdgeToEdgeDedicatedConnect">EdgeToEdgeDedicatedConnect</a>: <i>Boolean</i>
    <a href="#edgetoedgeigw" title="EdgeToEdgeIgw">EdgeToEdgeIgw</a>: <i>Boolean</i>
    <a href="#edgetoedgepeering" title="EdgeToEdgePeering">EdgeToEdgePeering</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#topologyname" title="TopologyName">TopologyName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CvContainerName

CVaaS Container Name to which the CloudEdge Routers
will be added to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeToEdgeDedicatedConnect

Dedicated connection between two Edge VPC,
default is false. ( Not Supported yet ).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeToEdgeIgw

Edge to Edge Connectivity through the Internet Gateway.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeToEdgePeering

Peering across Edge VPC's, default is false.
( Not supported yet ).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the wan resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologyName

Name of the topology this wan resource depends on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### TfId

Returns the <code>TfId</code> value.

