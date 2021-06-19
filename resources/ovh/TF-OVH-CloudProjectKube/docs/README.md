# TF::OVH::CloudProjectKube

Creates a kubernetes managed cluster in a public cloud project.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OVH::CloudProjectKube",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privatenetworkid" title="PrivateNetworkId">PrivateNetworkId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OVH::CloudProjectKube
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privatenetworkid" title="PrivateNetworkId">PrivateNetworkId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the kubernetes cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateNetworkId

OpenStack private network (or vrack) ID to use.
Changing this value recreates the resource. Defaults - not use private network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

a valid OVH public cloud region ID in which the kubernetes
cluster will be available. Ex.: "GRA1". Defaults to all public cloud regions.
Changing this value recreates the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The id of the public cloud project. If omitted,
the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

kubernetes version to use.
Changing this value recreates the resource. Defaults to latest available.

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

#### ControlPlaneIsUpToDate

Returns the <code>ControlPlaneIsUpToDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsUpToDate

Returns the <code>IsUpToDate</code> value.

#### Kubeconfig

Returns the <code>Kubeconfig</code> value.

#### NextUpgradeVersions

Returns the <code>NextUpgradeVersions</code> value.

#### NodesUrl

Returns the <code>NodesUrl</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdatePolicy

Returns the <code>UpdatePolicy</code> value.

#### Url

Returns the <code>Url</code> value.

