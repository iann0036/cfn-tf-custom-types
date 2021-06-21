# TF::AzureDevOps::ServiceendpointKubernetes KubeconfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acceptuntrustedcerts" title="AcceptUntrustedCerts">AcceptUntrustedCerts</a>" : <i>Boolean</i>,
    "<a href="#clustercontext" title="ClusterContext">ClusterContext</a>" : <i>String</i>,
    "<a href="#kubeconfig" title="KubeConfig">KubeConfig</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#acceptuntrustedcerts" title="AcceptUntrustedCerts">AcceptUntrustedCerts</a>: <i>Boolean</i>
<a href="#clustercontext" title="ClusterContext">ClusterContext</a>: <i>String</i>
<a href="#kubeconfig" title="KubeConfig">KubeConfig</a>: <i>String</i>
</pre>

## Properties

#### AcceptUntrustedCerts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterContext

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeConfig

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
