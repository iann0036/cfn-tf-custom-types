# Terraform::AWS::RdsClusterEndpoint

Manages a RDS Aurora Cluster Endpoint.
You can refer to the [User Guide][1].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::RdsClusterEndpoint",
    "Properties" : {
        "<a href="#clusterendpointidentifier" title="ClusterEndpointIdentifier">ClusterEndpointIdentifier</a>" : <i>String</i>,
        "<a href="#clusteridentifier" title="ClusterIdentifier">ClusterIdentifier</a>" : <i>String</i>,
        "<a href="#customendpointtype" title="CustomEndpointType">CustomEndpointType</a>" : <i>String</i>,
        "<a href="#excludedmembers" title="ExcludedMembers">ExcludedMembers</a>" : <i>[ String, ... ]</i>,
        "<a href="#staticmembers" title="StaticMembers">StaticMembers</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::RdsClusterEndpoint
Properties:
    <a href="#clusterendpointidentifier" title="ClusterEndpointIdentifier">ClusterEndpointIdentifier</a>: <i>String</i>
    <a href="#clusteridentifier" title="ClusterIdentifier">ClusterIdentifier</a>: <i>String</i>
    <a href="#customendpointtype" title="CustomEndpointType">CustomEndpointType</a>: <i>String</i>
    <a href="#excludedmembers" title="ExcludedMembers">ExcludedMembers</a>: <i>
      - String</i>
    <a href="#staticmembers" title="StaticMembers">StaticMembers</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### ClusterEndpointIdentifier

The identifier to use for the new endpoint. This parameter is stored as a lowercase string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIdentifier

The cluster identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomEndpointType

The type of the endpoint. One of: READER , ANY .

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedMembers

List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty. Conflicts with `static_members`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticMembers

List of DB instance identifiers that are part of the custom endpoint group. Conflicts with `excluded_members`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

