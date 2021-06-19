# TF::AzureRM::KubernetesCluster SshKeyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keydata" title="KeyData">KeyData</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#keydata" title="KeyData">KeyData</a>: <i>String</i>
</pre>

## Properties

#### KeyData

The Public SSH Key used to access the cluster. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

