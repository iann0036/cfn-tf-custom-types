# Terraform::Google::ComputeNetworkPeering

Manages a network peering within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/vpc/vpc-peering)
and
[API](https://cloud.google.com/compute/docs/reference/latest/networks).

-> Both network must create a peering with each other for the peering
to be functional.

~> Subnets IP ranges across peered VPC networks cannot overlap.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeNetworkPeering",
    "Properties" : {
        "<a href="#autocreateroutes" title="AutoCreateRoutes">AutoCreateRoutes</a>" : <i>Boolean</i>,
        "<a href="#exportcustomroutes" title="ExportCustomRoutes">ExportCustomRoutes</a>" : <i>Boolean</i>,
        "<a href="#importcustomroutes" title="ImportCustomRoutes">ImportCustomRoutes</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#peernetwork" title="PeerNetwork">PeerNetwork</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeNetworkPeering
Properties:
    <a href="#autocreateroutes" title="AutoCreateRoutes">AutoCreateRoutes</a>: <i>Boolean</i>
    <a href="#exportcustomroutes" title="ExportCustomRoutes">ExportCustomRoutes</a>: <i>Boolean</i>
    <a href="#importcustomroutes" title="ImportCustomRoutes">ImportCustomRoutes</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#peernetwork" title="PeerNetwork">PeerNetwork</a>: <i>String</i>
</pre>

## Properties

#### AutoCreateRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportCustomRoutes

Whether to export the custom routes to the peer network. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportCustomRoutes

Whether to export the custom routes from the peer network. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the peering.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

The primary network of the peering.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerNetwork

The peer network in the peering. The peer network
may belong to a different project.

_Required_: Yes

_Type_: String

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

#### State

Returns the <code>State</code> value.

#### StateDetails

Returns the <code>StateDetails</code> value.

