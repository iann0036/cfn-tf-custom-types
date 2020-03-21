# Terraform::Gitlab::ProjectCluster

CloudFormation equivalent of gitlab_project_cluster

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesApiUrl

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesAuthorizationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesCaCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesNamespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesToken

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Managed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

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

#### ClusterType

Returns the <code>ClusterType</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### PlatformType

Returns the <code>PlatformType</code> value.

#### ProviderType

Returns the <code>ProviderType</code> value.

