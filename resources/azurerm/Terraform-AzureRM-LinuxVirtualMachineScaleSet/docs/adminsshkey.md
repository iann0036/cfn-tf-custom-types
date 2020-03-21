# Terraform::AzureRM::LinuxVirtualMachineScaleSet AdminSshKey

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#publickey" title="PublicKey">PublicKey</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#publickey" title="PublicKey">PublicKey</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### PublicKey

The Public Key which should be used for authentication, which needs to be at least 2048-bit and in `ssh-rsa` format.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The Username for which this Public SSH Key should be configured.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

