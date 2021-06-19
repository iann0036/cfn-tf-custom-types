# TF::AzureRM::PacketCapture StorageLocationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filepath" title="FilePath">FilePath</a>" : <i>String</i>,
    "<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#filepath" title="FilePath">FilePath</a>: <i>String</i>
<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>: <i>String</i>
</pre>

## Properties

#### FilePath

A valid local path on the targeting VM. Must include the name of the capture file (*.cap). For linux virtual machine it must start with `/var/captures`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountId

The ID of the storage account to save the packet capture session.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

