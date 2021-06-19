# TF::OraclePaaS::DatabaseServiceInstance DatabaseConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
    "<a href="#backupdestination" title="BackupDestination">BackupDestination</a>" : <i>String</i>,
    "<a href="#backupstoragevolumesize" title="BackupStorageVolumeSize">BackupStorageVolumeSize</a>" : <i>Double</i>,
    "<a href="#characterset" title="CharacterSet">CharacterSet</a>" : <i>String</i>,
    "<a href="#datastoragevolumesize" title="DataStorageVolumeSize">DataStorageVolumeSize</a>" : <i>Double</i>,
    "<a href="#dbdemo" title="DbDemo">DbDemo</a>" : <i>String</i>,
    "<a href="#disasterrecovery" title="DisasterRecovery">DisasterRecovery</a>" : <i>Boolean</i>,
    "<a href="#failoverdatabase" title="FailoverDatabase">FailoverDatabase</a>" : <i>Boolean</i>,
    "<a href="#goldengate" title="GoldenGate">GoldenGate</a>" : <i>Boolean</i>,
    "<a href="#israc" title="IsRac">IsRac</a>" : <i>Boolean</i>,
    "<a href="#nationalcharacterset" title="NationalCharacterSet">NationalCharacterSet</a>" : <i>String</i>,
    "<a href="#pdbname" title="PdbName">PdbName</a>" : <i>String</i>,
    "<a href="#sid" title="Sid">Sid</a>" : <i>String</i>,
    "<a href="#snapshotname" title="SnapshotName">SnapshotName</a>" : <i>String</i>,
    "<a href="#sourceservicename" title="SourceServiceName">SourceServiceName</a>" : <i>String</i>,
    "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#usablestorage" title="UsableStorage">UsableStorage</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
<a href="#backupdestination" title="BackupDestination">BackupDestination</a>: <i>String</i>
<a href="#backupstoragevolumesize" title="BackupStorageVolumeSize">BackupStorageVolumeSize</a>: <i>Double</i>
<a href="#characterset" title="CharacterSet">CharacterSet</a>: <i>String</i>
<a href="#datastoragevolumesize" title="DataStorageVolumeSize">DataStorageVolumeSize</a>: <i>Double</i>
<a href="#dbdemo" title="DbDemo">DbDemo</a>: <i>String</i>
<a href="#disasterrecovery" title="DisasterRecovery">DisasterRecovery</a>: <i>Boolean</i>
<a href="#failoverdatabase" title="FailoverDatabase">FailoverDatabase</a>: <i>Boolean</i>
<a href="#goldengate" title="GoldenGate">GoldenGate</a>: <i>Boolean</i>
<a href="#israc" title="IsRac">IsRac</a>: <i>Boolean</i>
<a href="#nationalcharacterset" title="NationalCharacterSet">NationalCharacterSet</a>: <i>String</i>
<a href="#pdbname" title="PdbName">PdbName</a>: <i>String</i>
<a href="#sid" title="Sid">Sid</a>: <i>String</i>
<a href="#snapshotname" title="SnapshotName">SnapshotName</a>: <i>String</i>
<a href="#sourceservicename" title="SourceServiceName">SourceServiceName</a>: <i>String</i>
<a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#usablestorage" title="UsableStorage">UsableStorage</a>: <i>Double</i>
</pre>

## Properties

#### AdminPassword

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupDestination

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupStorageVolumeSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CharacterSet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataStorageVolumeSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbDemo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisasterRecovery

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverDatabase

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoldenGate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsRac

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NationalCharacterSet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdbName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceServiceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableStorage

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

