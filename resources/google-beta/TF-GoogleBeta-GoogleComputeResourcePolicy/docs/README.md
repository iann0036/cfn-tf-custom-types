# TF::GoogleBeta::GoogleComputeResourcePolicy

CloudFormation equivalent of google_compute_resource_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleComputeResourcePolicy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#groupplacementpolicy" title="GroupPlacementPolicy">GroupPlacementPolicy</a>" : <i>[ <a href="groupplacementpolicydefinition.md">GroupPlacementPolicyDefinition</a>, ... ]</i>,
        "<a href="#instanceschedulepolicy" title="InstanceSchedulePolicy">InstanceSchedulePolicy</a>" : <i>[ <a href="instanceschedulepolicydefinition.md">InstanceSchedulePolicyDefinition</a>, ... ]</i>,
        "<a href="#snapshotschedulepolicy" title="SnapshotSchedulePolicy">SnapshotSchedulePolicy</a>" : <i>[ <a href="snapshotschedulepolicydefinition.md">SnapshotSchedulePolicyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleComputeResourcePolicy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#groupplacementpolicy" title="GroupPlacementPolicy">GroupPlacementPolicy</a>: <i>
      - <a href="groupplacementpolicydefinition.md">GroupPlacementPolicyDefinition</a></i>
    <a href="#instanceschedulepolicy" title="InstanceSchedulePolicy">InstanceSchedulePolicy</a>: <i>
      - <a href="instanceschedulepolicydefinition.md">InstanceSchedulePolicyDefinition</a></i>
    <a href="#snapshotschedulepolicy" title="SnapshotSchedulePolicy">SnapshotSchedulePolicy</a>: <i>
      - <a href="snapshotschedulepolicydefinition.md">SnapshotSchedulePolicyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupPlacementPolicy

_Required_: No

_Type_: List of <a href="groupplacementpolicydefinition.md">GroupPlacementPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceSchedulePolicy

_Required_: No

_Type_: List of <a href="instanceschedulepolicydefinition.md">InstanceSchedulePolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotSchedulePolicy

_Required_: No

_Type_: List of <a href="snapshotschedulepolicydefinition.md">SnapshotSchedulePolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

