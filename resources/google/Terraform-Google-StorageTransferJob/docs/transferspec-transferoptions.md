# Terraform::Google::StorageTransferJob TransferSpec TransferOptions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deleteobjectsfromsourceaftertransfer" title="DeleteObjectsFromSourceAfterTransfer">DeleteObjectsFromSourceAfterTransfer</a>" : <i>Boolean</i>,
    "<a href="#deleteobjectsuniqueinsink" title="DeleteObjectsUniqueInSink">DeleteObjectsUniqueInSink</a>" : <i>Boolean</i>,
    "<a href="#overwriteobjectsalreadyexistinginsink" title="OverwriteObjectsAlreadyExistingInSink">OverwriteObjectsAlreadyExistingInSink</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#deleteobjectsfromsourceaftertransfer" title="DeleteObjectsFromSourceAfterTransfer">DeleteObjectsFromSourceAfterTransfer</a>: <i>Boolean</i>
<a href="#deleteobjectsuniqueinsink" title="DeleteObjectsUniqueInSink">DeleteObjectsUniqueInSink</a>: <i>Boolean</i>
<a href="#overwriteobjectsalreadyexistinginsink" title="OverwriteObjectsAlreadyExistingInSink">OverwriteObjectsAlreadyExistingInSink</a>: <i>Boolean</i>
</pre>

## Properties

#### DeleteObjectsFromSourceAfterTransfer

Whether objects should be deleted from the source after they are transferred to the sink. Note that this option and `delete_objects_unique_in_sink` are mutually exclusive.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteObjectsUniqueInSink

Whether objects that exist only in the sink should be deleted. Note that this option and
`delete_objects_from_source_after_transfer` are mutually exclusive.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverwriteObjectsAlreadyExistingInSink

Whether overwriting objects that already exist in the sink is allowed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

