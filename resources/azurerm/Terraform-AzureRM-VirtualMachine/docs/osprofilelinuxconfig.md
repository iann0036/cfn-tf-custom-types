# Terraform::AzureRM::VirtualMachine OsProfileLinuxConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablepasswordauthentication" title="DisablePasswordAuthentication">DisablePasswordAuthentication</a>" : <i>Boolean</i>,
    "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ <a href="osprofilelinuxconfig-sshkeys.md">SshKeys</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablepasswordauthentication" title="DisablePasswordAuthentication">DisablePasswordAuthentication</a>: <i>Boolean</i>
<a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - <a href="osprofilelinuxconfig-sshkeys.md">SshKeys</a></i>
</pre>

## Properties

#### DisablePasswordAuthentication

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

_Required_: No
_Type_: List of <a href="osprofilelinuxconfig-sshkeys.md">SshKeys</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

