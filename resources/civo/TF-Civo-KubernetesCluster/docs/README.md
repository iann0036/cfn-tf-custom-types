# TF::Civo::KubernetesCluster

Provides a Civo Kubernetes cluster resource. This can be used to create, delete, and modify clusters.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Civo::KubernetesCluster",
    "Properties" : {
        "<a href="#applications" title="Applications">Applications</a>" : <i>String</i>,
        "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#numtargetnodes" title="NumTargetNodes">NumTargetNodes</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>String</i>,
        "<a href="#targetnodessize" title="TargetNodesSize">TargetNodesSize</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Civo::KubernetesCluster
Properties:
    <a href="#applications" title="Applications">Applications</a>: <i>String</i>
    <a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#numtargetnodes" title="NumTargetNodes">NumTargetNodes</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>String</i>
    <a href="#targetnodessize" title="TargetNodesSize">TargetNodesSize</a>: <i>String</i>
</pre>

## Properties

#### Applications

A comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

The version of k3s to install (The default is currently the latest available).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the Kubernetes cluster, if is not declare the provider will generate one for you.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumTargetNodes

The number of instances to create (The default at the time of writing is 3).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region for the cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A space separated list of tags, to be used freely as required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetNodesSize

The size of each node (The default is currently g3.k3s.small).

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

#### ApiEndpoint

Returns the <code>ApiEndpoint</code> value.

#### BuiltAt

Returns the <code>BuiltAt</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### DnsEntry

Returns the <code>DnsEntry</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstalledApplications

Returns the <code>InstalledApplications</code> value.

#### Instances

Returns the <code>Instances</code> value.

#### Kubeconfig

Returns the <code>Kubeconfig</code> value.

#### MasterIp

Returns the <code>MasterIp</code> value.

#### Pools

Returns the <code>Pools</code> value.

#### Ready

Returns the <code>Ready</code> value.

#### Status

Returns the <code>Status</code> value.

