# TF::GoogleBeta::GoogleComputeInstanceFromMachineImage BootDiskDefinition3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autodelete" title="AutoDelete">AutoDelete</a>" : <i>Boolean</i>,
    "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
    "<a href="#diskencryptionkeyraw" title="DiskEncryptionKeyRaw">DiskEncryptionKeyRaw</a>" : <i>String</i>,
    "<a href="#diskencryptionkeysha256" title="DiskEncryptionKeySha256">DiskEncryptionKeySha256</a>" : <i>String</i>,
    "<a href="#initializeparams" title="InitializeParams">InitializeParams</a>" : <i>[ <a href="bootdiskdefinition2.md">BootDiskDefinition2</a>, ... ]</i>,
    "<a href="#kmskeyselflink" title="KmsKeySelfLink">KmsKeySelfLink</a>" : <i>String</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#autodelete" title="AutoDelete">AutoDelete</a>: <i>Boolean</i>
<a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
<a href="#diskencryptionkeyraw" title="DiskEncryptionKeyRaw">DiskEncryptionKeyRaw</a>: <i>String</i>
<a href="#diskencryptionkeysha256" title="DiskEncryptionKeySha256">DiskEncryptionKeySha256</a>: <i>String</i>
<a href="#initializeparams" title="InitializeParams">InitializeParams</a>: <i>
      - <a href="bootdiskdefinition2.md">BootDiskDefinition2</a></i>
<a href="#kmskeyselflink" title="KmsKeySelfLink">KmsKeySelfLink</a>: <i>String</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
</pre>

## Properties

#### AutoDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKeyRaw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKeySha256

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializeParams

_Required_: No

_Type_: List of <a href="bootdiskdefinition2.md">BootDiskDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeySelfLink

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

