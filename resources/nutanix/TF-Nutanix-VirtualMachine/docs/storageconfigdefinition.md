# TF::Nutanix::VirtualMachine StorageConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#flashmode" title="FlashMode">FlashMode</a>" : <i>String</i>,
    "<a href="#storagecontainerreference" title="StorageContainerReference">StorageContainerReference</a>" : <i>[ <a href="storagecontainerreferencedefinition.md">StorageContainerReferenceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#flashmode" title="FlashMode">FlashMode</a>: <i>String</i>
<a href="#storagecontainerreference" title="StorageContainerReference">StorageContainerReference</a>: <i>
      - <a href="storagecontainerreferencedefinition.md">StorageContainerReferenceDefinition</a></i>
</pre>

## Properties

#### FlashMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageContainerReference

_Required_: No

_Type_: List of <a href="storagecontainerreferencedefinition.md">StorageContainerReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

