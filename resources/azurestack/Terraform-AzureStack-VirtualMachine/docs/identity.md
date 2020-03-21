# Terraform::AzureStack::VirtualMachine Identity

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Type

Specifies the identity type of the virtual machine. The only allowable value is `SystemAssigned`. To enable Managed Service Identity the virtual machine extension "ManagedIdentityExtensionForWindows" or "ManagedIdentityExtensionForLinux" must also be added to the virtual machine. The Principal ID can be retrieved after the virtual machine has been created, e.g.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

