# Terraform::AzureRM::WindowsVirtualMachineScaleSet BootDiagnostics

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#storageaccounturi" title="StorageAccountUri">StorageAccountUri</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#storageaccounturi" title="StorageAccountUri">StorageAccountUri</a>: <i>String</i>
</pre>

## Properties

#### StorageAccountUri

The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

