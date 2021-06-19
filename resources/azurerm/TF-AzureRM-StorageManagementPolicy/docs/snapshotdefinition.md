# TF::AzureRM::StorageManagementPolicy SnapshotDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#changetiertoarchiveafterdayssincecreation" title="ChangeTierToArchiveAfterDaysSinceCreation">ChangeTierToArchiveAfterDaysSinceCreation</a>" : <i>Double</i>,
    "<a href="#changetiertocoolafterdayssincecreation" title="ChangeTierToCoolAfterDaysSinceCreation">ChangeTierToCoolAfterDaysSinceCreation</a>" : <i>Double</i>,
    "<a href="#deleteafterdayssincecreationgreaterthan" title="DeleteAfterDaysSinceCreationGreaterThan">DeleteAfterDaysSinceCreationGreaterThan</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#changetiertoarchiveafterdayssincecreation" title="ChangeTierToArchiveAfterDaysSinceCreation">ChangeTierToArchiveAfterDaysSinceCreation</a>: <i>Double</i>
<a href="#changetiertocoolafterdayssincecreation" title="ChangeTierToCoolAfterDaysSinceCreation">ChangeTierToCoolAfterDaysSinceCreation</a>: <i>Double</i>
<a href="#deleteafterdayssincecreationgreaterthan" title="DeleteAfterDaysSinceCreationGreaterThan">DeleteAfterDaysSinceCreationGreaterThan</a>: <i>Double</i>
</pre>

## Properties

#### ChangeTierToArchiveAfterDaysSinceCreation

The age in days after creation to tier blob snapshot to archive storage. Must be between 0 and 99999.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChangeTierToCoolAfterDaysSinceCreation

The age in days after creation to tier blob snapshot to cool storage. Must be between 0 and 99999.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteAfterDaysSinceCreationGreaterThan

The age in days after creation to delete the blob snapshot. Must be between 0 and 99999.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

