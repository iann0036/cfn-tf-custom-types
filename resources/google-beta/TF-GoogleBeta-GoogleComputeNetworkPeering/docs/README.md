# TF::GoogleBeta::GoogleComputeNetworkPeering

CloudFormation equivalent of google_compute_network_peering

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleComputeNetworkPeering",
    "Properties" : {
        "<a href="#exportcustomroutes" title="ExportCustomRoutes">ExportCustomRoutes</a>" : <i>Boolean</i>,
        "<a href="#exportsubnetrouteswithpublicip" title="ExportSubnetRoutesWithPublicIp">ExportSubnetRoutesWithPublicIp</a>" : <i>Boolean</i>,
        "<a href="#importcustomroutes" title="ImportCustomRoutes">ImportCustomRoutes</a>" : <i>Boolean</i>,
        "<a href="#importsubnetrouteswithpublicip" title="ImportSubnetRoutesWithPublicIp">ImportSubnetRoutesWithPublicIp</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#peernetwork" title="PeerNetwork">PeerNetwork</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleComputeNetworkPeering
Properties:
    <a href="#exportcustomroutes" title="ExportCustomRoutes">ExportCustomRoutes</a>: <i>Boolean</i>
    <a href="#exportsubnetrouteswithpublicip" title="ExportSubnetRoutesWithPublicIp">ExportSubnetRoutesWithPublicIp</a>: <i>Boolean</i>
    <a href="#importcustomroutes" title="ImportCustomRoutes">ImportCustomRoutes</a>: <i>Boolean</i>
    <a href="#importsubnetrouteswithpublicip" title="ImportSubnetRoutesWithPublicIp">ImportSubnetRoutesWithPublicIp</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#peernetwork" title="PeerNetwork">PeerNetwork</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ExportCustomRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportSubnetRoutesWithPublicIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportCustomRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportSubnetRoutesWithPublicIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerNetwork

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

#### State

Returns the <code>State</code> value.

#### StateDetails

Returns the <code>StateDetails</code> value.

