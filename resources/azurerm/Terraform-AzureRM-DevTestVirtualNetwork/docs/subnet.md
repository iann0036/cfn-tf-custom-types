# Terraform::AzureRM::DevTestVirtualNetwork Subnet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#useinvirtualmachinecreation" title="UseInVirtualMachineCreation">UseInVirtualMachineCreation</a>" : <i>String</i>,
    "<a href="#usepublicipaddress" title="UsePublicIpAddress">UsePublicIpAddress</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#useinvirtualmachinecreation" title="UseInVirtualMachineCreation">UseInVirtualMachineCreation</a>: <i>String</i>
<a href="#usepublicipaddress" title="UsePublicIpAddress">UsePublicIpAddress</a>: <i>String</i>
</pre>

## Properties

#### UseInVirtualMachineCreation

Can this subnet be used for creating Virtual Machines? Possible values are `Allow`, `Default` and `Deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePublicIpAddress

Can Virtual Machines in this Subnet use Public IP Addresses? Possible values are `Allow`, `Default` and `Deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

