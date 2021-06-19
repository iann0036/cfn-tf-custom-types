# TF::Rancher2::ClusterTemplate BastionHostDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>,
    "<a href="#sshagentauth" title="SshAgentAuth">SshAgentAuth</a>" : <i>Boolean</i>,
    "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>String</i>,
    "<a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
<a href="#sshagentauth" title="SshAgentAuth">SshAgentAuth</a>: <i>Boolean</i>
<a href="#sshkey" title="SshKey">SshKey</a>: <i>String</i>
<a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### Address

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshAgentAuth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

