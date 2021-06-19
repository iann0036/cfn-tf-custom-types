# TF::AVI::Upgradestatusinfo

The UpgradeStatusInfo resource allows the creation and management of Avi UpgradeStatusInfo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Upgradestatusinfo",
    "Properties" : {
        "<a href="#afterrebootrollbackfnc" title="AfterRebootRollbackFnc">AfterRebootRollbackFnc</a>" : <i>String</i>,
        "<a href="#afterreboottaskname" title="AfterRebootTaskName">AfterRebootTaskName</a>" : <i>String</i>,
        "<a href="#clean" title="Clean">Clean</a>" : <i>Boolean</i>,
        "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
        "<a href="#enablepatchrollback" title="EnablePatchRollback">EnablePatchRollback</a>" : <i>Boolean</i>,
        "<a href="#enablerollback" title="EnableRollback">EnableRollback</a>" : <i>Boolean</i>,
        "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
        "<a href="#enqueuetime" title="EnqueueTime">EnqueueTime</a>" : <i>String</i>,
        "<a href="#fipsmode" title="FipsMode">FipsMode</a>" : <i>Boolean</i>,
        "<a href="#imagepath" title="ImagePath">ImagePath</a>" : <i>String</i>,
        "<a href="#imageref" title="ImageRef">ImageRef</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodetype" title="NodeType">NodeType</a>" : <i>String</i>,
        "<a href="#objcloudref" title="ObjCloudRef">ObjCloudRef</a>" : <i>String</i>,
        "<a href="#patchimagepath" title="PatchImagePath">PatchImagePath</a>" : <i>String</i>,
        "<a href="#patchimageref" title="PatchImageRef">PatchImageRef</a>" : <i>String</i>,
        "<a href="#patchreboot" title="PatchReboot">PatchReboot</a>" : <i>Boolean</i>,
        "<a href="#patchversion" title="PatchVersion">PatchVersion</a>" : <i>String</i>,
        "<a href="#previmagepath" title="PrevImagePath">PrevImagePath</a>" : <i>String</i>,
        "<a href="#prevpatchimagepath" title="PrevPatchImagePath">PrevPatchImagePath</a>" : <i>String</i>,
        "<a href="#previousimageref" title="PreviousImageRef">PreviousImageRef</a>" : <i>String</i>,
        "<a href="#previouspatchimageref" title="PreviousPatchImageRef">PreviousPatchImageRef</a>" : <i>String</i>,
        "<a href="#previouspatchversion" title="PreviousPatchVersion">PreviousPatchVersion</a>" : <i>String</i>,
        "<a href="#previousversion" title="PreviousVersion">PreviousVersion</a>" : <i>String</i>,
        "<a href="#progress" title="Progress">Progress</a>" : <i>Double</i>,
        "<a href="#sepatchimagepath" title="SePatchImagePath">SePatchImagePath</a>" : <i>String</i>,
        "<a href="#sepatchimageref" title="SePatchImageRef">SePatchImageRef</a>" : <i>String</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
        "<a href="#system" title="System">System</a>" : <i>Boolean</i>,
        "<a href="#taskscompleted" title="TasksCompleted">TasksCompleted</a>" : <i>Double</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#totaltasks" title="TotalTasks">TotalTasks</a>" : <i>Double</i>,
        "<a href="#upgradeops" title="UpgradeOps">UpgradeOps</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#history" title="History">History</a>" : <i>[ <a href="historydefinition.md">HistoryDefinition</a>, ... ]</i>,
        "<a href="#params" title="Params">Params</a>" : <i>[ <a href="paramsdefinition.md">ParamsDefinition</a>, ... ]</i>,
        "<a href="#patchlist" title="PatchList">PatchList</a>" : <i>[ <a href="patchlistdefinition.md">PatchListDefinition</a>, ... ]</i>,
        "<a href="#previouspatchlist" title="PreviousPatchList">PreviousPatchList</a>" : <i>[ <a href="previouspatchlistdefinition.md">PreviousPatchListDefinition</a>, ... ]</i>,
        "<a href="#seupgradeevents" title="SeUpgradeEvents">SeUpgradeEvents</a>" : <i>[ <a href="seupgradeeventsdefinition.md">SeUpgradeEventsDefinition</a>, ... ]</i>,
        "<a href="#segparams" title="SegParams">SegParams</a>" : <i>[ <a href="segparamsdefinition.md">SegParamsDefinition</a>, ... ]</i>,
        "<a href="#segstatus" title="SegStatus">SegStatus</a>" : <i>[ <a href="segstatusdefinition.md">SegStatusDefinition</a>, ... ]</i>,
        "<a href="#state" title="State">State</a>" : <i>[ <a href="statedefinition.md">StateDefinition</a>, ... ]</i>,
        "<a href="#upgradeevents" title="UpgradeEvents">UpgradeEvents</a>" : <i>[ <a href="upgradeeventsdefinition.md">UpgradeEventsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Upgradestatusinfo
Properties:
    <a href="#afterrebootrollbackfnc" title="AfterRebootRollbackFnc">AfterRebootRollbackFnc</a>: <i>String</i>
    <a href="#afterreboottaskname" title="AfterRebootTaskName">AfterRebootTaskName</a>: <i>String</i>
    <a href="#clean" title="Clean">Clean</a>: <i>Boolean</i>
    <a href="#duration" title="Duration">Duration</a>: <i>Double</i>
    <a href="#enablepatchrollback" title="EnablePatchRollback">EnablePatchRollback</a>: <i>Boolean</i>
    <a href="#enablerollback" title="EnableRollback">EnableRollback</a>: <i>Boolean</i>
    <a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
    <a href="#enqueuetime" title="EnqueueTime">EnqueueTime</a>: <i>String</i>
    <a href="#fipsmode" title="FipsMode">FipsMode</a>: <i>Boolean</i>
    <a href="#imagepath" title="ImagePath">ImagePath</a>: <i>String</i>
    <a href="#imageref" title="ImageRef">ImageRef</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodetype" title="NodeType">NodeType</a>: <i>String</i>
    <a href="#objcloudref" title="ObjCloudRef">ObjCloudRef</a>: <i>String</i>
    <a href="#patchimagepath" title="PatchImagePath">PatchImagePath</a>: <i>String</i>
    <a href="#patchimageref" title="PatchImageRef">PatchImageRef</a>: <i>String</i>
    <a href="#patchreboot" title="PatchReboot">PatchReboot</a>: <i>Boolean</i>
    <a href="#patchversion" title="PatchVersion">PatchVersion</a>: <i>String</i>
    <a href="#previmagepath" title="PrevImagePath">PrevImagePath</a>: <i>String</i>
    <a href="#prevpatchimagepath" title="PrevPatchImagePath">PrevPatchImagePath</a>: <i>String</i>
    <a href="#previousimageref" title="PreviousImageRef">PreviousImageRef</a>: <i>String</i>
    <a href="#previouspatchimageref" title="PreviousPatchImageRef">PreviousPatchImageRef</a>: <i>String</i>
    <a href="#previouspatchversion" title="PreviousPatchVersion">PreviousPatchVersion</a>: <i>String</i>
    <a href="#previousversion" title="PreviousVersion">PreviousVersion</a>: <i>String</i>
    <a href="#progress" title="Progress">Progress</a>: <i>Double</i>
    <a href="#sepatchimagepath" title="SePatchImagePath">SePatchImagePath</a>: <i>String</i>
    <a href="#sepatchimageref" title="SePatchImageRef">SePatchImageRef</a>: <i>String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
    <a href="#system" title="System">System</a>: <i>Boolean</i>
    <a href="#taskscompleted" title="TasksCompleted">TasksCompleted</a>: <i>Double</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#totaltasks" title="TotalTasks">TotalTasks</a>: <i>Double</i>
    <a href="#upgradeops" title="UpgradeOps">UpgradeOps</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#history" title="History">History</a>: <i>
      - <a href="historydefinition.md">HistoryDefinition</a></i>
    <a href="#params" title="Params">Params</a>: <i>
      - <a href="paramsdefinition.md">ParamsDefinition</a></i>
    <a href="#patchlist" title="PatchList">PatchList</a>: <i>
      - <a href="patchlistdefinition.md">PatchListDefinition</a></i>
    <a href="#previouspatchlist" title="PreviousPatchList">PreviousPatchList</a>: <i>
      - <a href="previouspatchlistdefinition.md">PreviousPatchListDefinition</a></i>
    <a href="#seupgradeevents" title="SeUpgradeEvents">SeUpgradeEvents</a>: <i>
      - <a href="seupgradeeventsdefinition.md">SeUpgradeEventsDefinition</a></i>
    <a href="#segparams" title="SegParams">SegParams</a>: <i>
      - <a href="segparamsdefinition.md">SegParamsDefinition</a></i>
    <a href="#segstatus" title="SegStatus">SegStatus</a>: <i>
      - <a href="segstatusdefinition.md">SegStatusDefinition</a></i>
    <a href="#state" title="State">State</a>: <i>
      - <a href="statedefinition.md">StateDefinition</a></i>
    <a href="#upgradeevents" title="UpgradeEvents">UpgradeEvents</a>: <i>
      - <a href="upgradeeventsdefinition.md">UpgradeEventsDefinition</a></i>
</pre>

## Properties

#### AfterRebootRollbackFnc

Backward compatible abort function name. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AfterRebootTaskName

Backward compatible task dict name. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Clean

Flag for clean installation. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

Duration of upgrade operation in seconds. Field introduced in 18.2.6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePatchRollback

Check if the patch rollback is possible on this node. Field introduced in 18.2.6.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRollback

Check if the rollback is possible on this node. Field introduced in 18.2.6.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

End time of upgrade operation. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnqueueTime

Enqueue time of upgrade operation. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FipsMode

Fips mode for the entire system. Field introduced in 20.1.5.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePath

Image path of current base image. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageRef

Image uuid for identifying the current base image. It is a reference to an object of type image. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the system such as cluster name, se group name and se name. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeType

Type of the system such as controller_cluster, se_group or se. Enum options - NODE_CONTROLLER_CLUSTER, NODE_SE_GROUP, NODE_SE_TYPE. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjCloudRef

Cloud that this object belongs to. It is a reference to an object of type cloud. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchImagePath

Image path of current patch image. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchImageRef

Image uuid for identifying the current patch.example  base-image is 18.2.6 and a patch 6p1 is applied, then this field will indicate the 6p1 value. It is a reference to an object of type image. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchReboot

Flag for patch op with reboot. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchVersion

Current patch version applied to this node. Example  base-image is 18.2.6 and a patch 6p1 is applied, then this field will indicate the 6p1 value. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrevImagePath

Image path of previous base image. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrevPatchImagePath

Image path of previous patch image. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreviousImageRef

Image uuid for identifying previous base image.example  base-image was 18.2.5 and an upgrade was done to 18.2.6, then this field will indicate the 18.2.5 value. It is a reference to an object of type image. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreviousPatchImageRef

Image uuid for identifying previous patch.example  base-image was 18.2.6 with a patch 6p1. Upgrade was initiated to 18.2.8 with patch 8p1. The previous_image field will contain 18.2.6 and this field will indicate the 6p1 value. It is a reference to an object of type image. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreviousPatchVersion

Previous patch version applied to this node.example  base-image was 18.2.6 with a patch 6p1. Upgrade was initiated to 18.2.8 with patch 8p1. The previous_image field will contain 18.2.6 and this field will indicate the 6p1 value. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreviousVersion

Previous version prior to upgrade.example  base-image was 18.2.5 and an upgrade was done to 18.2.6, then this field will indicate the 18.2.5 value. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Progress

Upgrade operations progress which holds value between 0-100. Allowed values are 0-100. Field introduced in 18.2.8, 20.1.1. Unit is percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePatchImagePath

Image path of se patch image.(required in case of reimage and upgrade + patch). Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePatchImageRef

Image uuid for identifying the current se patch required in case of system upgrade(re-image) with se patch. It is a reference to an object of type image. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Start time of upgrade operation. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### System

Flag is set only in the cluster if the upgrade is initiated as a system-upgrade. Field introduced in 18.2.6.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TasksCompleted

Completed set of tasks in the upgrade operation. Field introduced in 18.2.6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

Tenant that this object belongs to. It is a reference to an object of type tenant. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TotalTasks

Total number of tasks in the upgrade operation. Field introduced in 18.2.6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeOps

Upgrade operations requested. Enum options - UPGRADE, PATCH, ROLLBACK, ROLLBACKPATCH, SEGROUP_RESUME. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Current base image applied to this node. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### History

_Required_: No

_Type_: List of <a href="historydefinition.md">HistoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Params

_Required_: No

_Type_: List of <a href="paramsdefinition.md">ParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchList

_Required_: No

_Type_: List of <a href="patchlistdefinition.md">PatchListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreviousPatchList

_Required_: No

_Type_: List of <a href="previouspatchlistdefinition.md">PreviousPatchListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUpgradeEvents

_Required_: No

_Type_: List of <a href="seupgradeeventsdefinition.md">SeUpgradeEventsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegParams

_Required_: No

_Type_: List of <a href="segparamsdefinition.md">SegParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegStatus

_Required_: No

_Type_: List of <a href="segstatusdefinition.md">SegStatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: List of <a href="statedefinition.md">StateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeEvents

_Required_: No

_Type_: List of <a href="upgradeeventsdefinition.md">UpgradeEventsDefinition</a>

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

