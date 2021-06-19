# TF::Rancher2::ClusterTemplate NodesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#dockersocket" title="DockerSocket">DockerSocket</a>" : <i>String</i>,
    "<a href="#hostnameoverride" title="HostnameOverride">HostnameOverride</a>" : <i>String</i>,
    "<a href="#internaladdress" title="InternalAddress">InternalAddress</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
    "<a href="#nodeid" title="NodeId">NodeId</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>,
    "<a href="#role" title="Role">Role</a>" : <i>[ String, ... ]</i>,
    "<a href="#sshagentauth" title="SshAgentAuth">SshAgentAuth</a>" : <i>Boolean</i>,
    "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>String</i>,
    "<a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#dockersocket" title="DockerSocket">DockerSocket</a>: <i>String</i>
<a href="#hostnameoverride" title="HostnameOverride">HostnameOverride</a>: <i>String</i>
<a href="#internaladdress" title="InternalAddress">InternalAddress</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
<a href="#nodeid" title="NodeId">NodeId</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
<a href="#role" title="Role">Role</a>: <i>
      - String</i>
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

#### DockerSocket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameOverride

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: Yes

_Type_: List of String

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

