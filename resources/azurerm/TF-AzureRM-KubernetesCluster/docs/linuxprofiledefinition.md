# TF::AzureRM::KubernetesCluster LinuxProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
    "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>[ <a href="sshkeydefinition.md">SshKeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
<a href="#sshkey" title="SshKey">SshKey</a>: <i>
      - <a href="sshkeydefinition.md">SshKeyDefinition</a></i>
</pre>

## Properties

#### AdminUsername

The Admin Username for the Cluster. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKey

_Required_: No

_Type_: List of <a href="sshkeydefinition.md">SshKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

