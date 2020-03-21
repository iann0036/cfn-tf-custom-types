# Terraform::AzureRM::WindowsVirtualMachineScaleSet AdditionalCapabilities

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ultrassdenabled" title="UltraSsdEnabled">UltraSsdEnabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#ultrassdenabled" title="UltraSsdEnabled">UltraSsdEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### UltraSsdEnabled

Should the capacity to enable Data Disks of the `UltraSSD_LRS` storage account type be supported on this Virtual Machine Scale Set? Defaults to `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

