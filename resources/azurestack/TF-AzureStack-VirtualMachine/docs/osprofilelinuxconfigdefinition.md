# TF::AzureStack::VirtualMachine OsProfileLinuxConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablepasswordauthentication" title="DisablePasswordAuthentication">DisablePasswordAuthentication</a>" : <i>Boolean</i>,
    "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ <a href="sshkeysdefinition.md">SshKeysDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablepasswordauthentication" title="DisablePasswordAuthentication">DisablePasswordAuthentication</a>: <i>Boolean</i>
<a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - <a href="sshkeysdefinition.md">SshKeysDefinition</a></i>
</pre>

## Properties

#### DisablePasswordAuthentication

Specifies whether password authentication should be disabled. If set to `false`, an `admin_password` must be specified.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

_Required_: No

_Type_: List of <a href="sshkeysdefinition.md">SshKeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

