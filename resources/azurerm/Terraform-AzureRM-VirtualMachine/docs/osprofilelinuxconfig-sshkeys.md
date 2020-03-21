# Terraform::AzureRM::VirtualMachine OsProfileLinuxConfig SshKeys

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keydata" title="KeyData">KeyData</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#keydata" title="KeyData">KeyData</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### KeyData

The Public SSH Key which should be written to the `path` defined above.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path of the destination file on the virtual machine.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

