# Terraform::Gitlab::ProjectCluster

This resource allows you to create and manage project clusters for your GitLab projects.
For further information on clusters, consult the [gitlab
documentation](https://docs.gitlab.com/ce/user/project/clusters/index.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Gitlab::ProjectCluster",
    "Properties" : {
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#environmentscope" title="EnvironmentScope">EnvironmentScope</a>" : <i>String</i>,
        "<a href="#kubernetesapiurl" title="KubernetesApiUrl">KubernetesApiUrl</a>" : <i>String</i>,
        "<a href="#kubernetesauthorizationtype" title="KubernetesAuthorizationType">KubernetesAuthorizationType</a>" : <i>String</i>,
        "<a href="#kubernetescacert" title="KubernetesCaCert">KubernetesCaCert</a>" : <i>String</i>,
        "<a href="#kubernetesnamespace" title="KubernetesNamespace">KubernetesNamespace</a>" : <i>String</i>,
        "<a href="#kubernetestoken" title="KubernetesToken">KubernetesToken</a>" : <i>String</i>,
        "<a href="#managed" title="Managed">Managed</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Gitlab::ProjectCluster
Properties:
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#environmentscope" title="EnvironmentScope">EnvironmentScope</a>: <i>String</i>
    <a href="#kubernetesapiurl" title="KubernetesApiUrl">KubernetesApiUrl</a>: <i>String</i>
    <a href="#kubernetesauthorizationtype" title="KubernetesAuthorizationType">KubernetesAuthorizationType</a>: <i>String</i>
    <a href="#kubernetescacert" title="KubernetesCaCert">KubernetesCaCert</a>: <i>String</i>
    <a href="#kubernetesnamespace" title="KubernetesNamespace">KubernetesNamespace</a>: <i>String</i>
    <a href="#kubernetestoken" title="KubernetesToken">KubernetesToken</a>: <i>String</i>
    <a href="#managed" title="Managed">Managed</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
</pre>

## Properties

#### Domain

The base domain of the cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Determines if cluster is active or not. Defaults to `true`. This attribute cannot be read.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentScope

The associated environment to the cluster. Defaults to `*`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesApiUrl

The URL to access the Kubernetes API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesAuthorizationType

The cluster authorization type. Valid values are `rbac`, `abac`, `unknown_authorization`. Defaults to `rbac`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesCaCert

TLS certificate (needed if API is using a self-signed TLS certificate).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesNamespace

The unique namespace related to the project.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesToken

The token to authenticate against Kubernetes.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Managed

Determines if cluster is managed by gitlab or not. Defaults to `true`. This attribute cannot be read.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The id of the project to add the cluster to.

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

#### ClusterType

Returns the <code>ClusterType</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### PlatformType

Returns the <code>PlatformType</code> value.

#### ProviderType

Returns the <code>ProviderType</code> value.

