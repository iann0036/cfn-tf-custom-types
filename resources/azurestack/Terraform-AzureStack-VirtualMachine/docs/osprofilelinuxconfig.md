# Terraform::AzureStack::VirtualMachine OsProfileLinuxConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablepasswordauthentication" title="DisablePasswordAuthentication">DisablePasswordAuthentication</a>" : <i>Boolean</i>,
    "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ &lt;a href=&#34;osprofilelinuxconfig-sshkeys.md&#34;&gt;SshKeys&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablepasswordauthentication" title="DisablePasswordAuthentication">DisablePasswordAuthentication</a>: <i>Boolean</i>
<a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - &lt;a href=&#34;osprofilelinuxconfig-sshkeys.md&#34;&gt;SshKeys&lt;/a&gt;</i>
</pre>

## Properties

#### DisablePasswordAuthentication

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

_Required_: No
_Type_: List of &lt;a href=&#34;osprofilelinuxconfig-sshkeys.md&#34;&gt;SshKeys&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

