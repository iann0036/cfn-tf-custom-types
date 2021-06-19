# TF::GoogleBeta::GoogleStorageTransferJob

CloudFormation equivalent of google_storage_transfer_job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleStorageTransferJob",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="scheduledefinition.md">ScheduleDefinition</a>, ... ]</i>,
        "<a href="#transferspec" title="TransferSpec">TransferSpec</a>" : <i>[ <a href="transferspecdefinition.md">TransferSpecDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleStorageTransferJob
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="scheduledefinition.md">ScheduleDefinition</a></i>
    <a href="#transferspec" title="TransferSpec">TransferSpec</a>: <i>
      - <a href="transferspecdefinition.md">TransferSpecDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="scheduledefinition.md">ScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransferSpec

_Required_: No

_Type_: List of <a href="transferspecdefinition.md">TransferSpecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationTime

Returns the <code>CreationTime</code> value.

#### DeletionTime

Returns the <code>DeletionTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModificationTime

Returns the <code>LastModificationTime</code> value.

#### Name

Returns the <code>Name</code> value.

