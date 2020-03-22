# Terraform::Google::ServiceNetworkingConnection

Manages a private VPC connection with a GCP service provider. For more information see
[the official documentation](https://cloud.google.com/vpc/docs/configure-private-services-access#creating-connection)
and
[API](https://cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ServiceNetworkingConnection",
    "Properties" : {
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#reservedpeeringranges" title="ReservedPeeringRanges">ReservedPeeringRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ServiceNetworkingConnection
Properties:
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#reservedpeeringranges" title="ReservedPeeringRanges">ReservedPeeringRanges</a>: <i>
      - String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
</pre>

## Properties

#### Network

Name of VPC network connected with service producers using VPC peering.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedPeeringRanges

Named IP address range(s) of PEERING type reserved for
this service provider. Note that invoking this method with a different range when connection
is already established will not reallocate already provisioned service producer subnetworks.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

Provider peering service that is managing peering connectivity for a
service provider organization. For Google services that support this functionality it is
'servicenetworking.googleapis.com'.

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

#### Id

Returns the <code>Id</code> value.

#### Peering

Returns the <code>Peering</code> value.

