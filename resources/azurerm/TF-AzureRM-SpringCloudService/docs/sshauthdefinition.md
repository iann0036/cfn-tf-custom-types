# TF::AzureRM::SpringCloudService SshAuthDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostkey" title="HostKey">HostKey</a>" : <i>String</i>,
    "<a href="#hostkeyalgorithm" title="HostKeyAlgorithm">HostKeyAlgorithm</a>" : <i>String</i>,
    "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
    "<a href="#stricthostkeycheckingenabled" title="StrictHostKeyCheckingEnabled">StrictHostKeyCheckingEnabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#hostkey" title="HostKey">HostKey</a>: <i>String</i>
<a href="#hostkeyalgorithm" title="HostKeyAlgorithm">HostKeyAlgorithm</a>: <i>String</i>
<a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
<a href="#stricthostkeycheckingenabled" title="StrictHostKeyCheckingEnabled">StrictHostKeyCheckingEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### HostKey

The host key of the Git repository server, should not include the algorithm prefix as covered by `host-key-algorithm`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostKeyAlgorithm

The host key algorithm, should be `ssh-dss`, `ssh-rsa`, `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, or `ecdsa-sha2-nistp521`. Required only if `host-key` exists.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

The SSH private key to access the Git repository, required when the URI starts with `git@` or `ssh://`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictHostKeyCheckingEnabled

Indicates whether the Config Server instance will fail to start if the host_key does not match.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

