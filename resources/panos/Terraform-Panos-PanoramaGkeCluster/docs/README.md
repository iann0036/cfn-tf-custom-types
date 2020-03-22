# Terraform::Panos::PanoramaGkeCluster

This resource allows you to add/update/delete a GKE cluster in a cluster group.

This resource requires that the GCP plugin be installed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaGkeCluster",
    "Properties" : {
        "<a href="#clustercredential" title="ClusterCredential">ClusterCredential</a>" : <i>String</i>,
        "<a href="#gcpzone" title="GcpZone">GcpZone</a>" : <i>String</i>,
        "<a href="#gkeclustergroup" title="GkeClusterGroup">GkeClusterGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaGkeCluster
Properties:
    <a href="#clustercredential" title="ClusterCredential">ClusterCredential</a>: <i>String</i>
    <a href="#gcpzone" title="GcpZone">GcpZone</a>: <i>String</i>
    <a href="#gkeclustergroup" title="GkeClusterGroup">GkeClusterGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### ClusterCredential

The GKE account to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpZone

The GCP zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GkeClusterGroup

The cluster group name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The cluster group's name.

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

