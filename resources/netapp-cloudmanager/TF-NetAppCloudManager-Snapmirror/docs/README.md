# TF::NetAppCloudManager::Snapmirror

Provides a netapp-cloudmanager_snapmirror resource. This can be used to create a new snapmirror relationship on Cloud Volumes ONTAP.
Requires existence of a Cloud Manager Connector and a Cloud Volumes ONTAP system.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::Snapmirror",
    "Properties" : {
        "<a href="#capacitytier" title="CapacityTier">CapacityTier</a>" : <i>String</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#destinationaggregatename" title="DestinationAggregateName">DestinationAggregateName</a>" : <i>String</i>,
        "<a href="#destinationsvmname" title="DestinationSvmName">DestinationSvmName</a>" : <i>String</i>,
        "<a href="#destinationvolumename" title="DestinationVolumeName">DestinationVolumeName</a>" : <i>String</i>,
        "<a href="#destinationworkingenvironmentid" title="DestinationWorkingEnvironmentId">DestinationWorkingEnvironmentId</a>" : <i>String</i>,
        "<a href="#destinationworkingenvironmentname" title="DestinationWorkingEnvironmentName">DestinationWorkingEnvironmentName</a>" : <i>String</i>,
        "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
        "<a href="#maxtransferrate" title="MaxTransferRate">MaxTransferRate</a>" : <i>Double</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#providervolumetype" title="ProviderVolumeType">ProviderVolumeType</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#sourcesvmname" title="SourceSvmName">SourceSvmName</a>" : <i>String</i>,
        "<a href="#sourcevolumename" title="SourceVolumeName">SourceVolumeName</a>" : <i>String</i>,
        "<a href="#sourceworkingenvironmentid" title="SourceWorkingEnvironmentId">SourceWorkingEnvironmentId</a>" : <i>String</i>,
        "<a href="#sourceworkingenvironmentname" title="SourceWorkingEnvironmentName">SourceWorkingEnvironmentName</a>" : <i>String</i>,
        "<a href="#throughput" title="Throughput">Throughput</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::Snapmirror
Properties:
    <a href="#capacitytier" title="CapacityTier">CapacityTier</a>: <i>String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#destinationaggregatename" title="DestinationAggregateName">DestinationAggregateName</a>: <i>String</i>
    <a href="#destinationsvmname" title="DestinationSvmName">DestinationSvmName</a>: <i>String</i>
    <a href="#destinationvolumename" title="DestinationVolumeName">DestinationVolumeName</a>: <i>String</i>
    <a href="#destinationworkingenvironmentid" title="DestinationWorkingEnvironmentId">DestinationWorkingEnvironmentId</a>: <i>String</i>
    <a href="#destinationworkingenvironmentname" title="DestinationWorkingEnvironmentName">DestinationWorkingEnvironmentName</a>: <i>String</i>
    <a href="#iops" title="Iops">Iops</a>: <i>Double</i>
    <a href="#maxtransferrate" title="MaxTransferRate">MaxTransferRate</a>: <i>Double</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#providervolumetype" title="ProviderVolumeType">ProviderVolumeType</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#sourcesvmname" title="SourceSvmName">SourceSvmName</a>: <i>String</i>
    <a href="#sourcevolumename" title="SourceVolumeName">SourceVolumeName</a>: <i>String</i>
    <a href="#sourceworkingenvironmentid" title="SourceWorkingEnvironmentId">SourceWorkingEnvironmentId</a>: <i>String</i>
    <a href="#sourceworkingenvironmentname" title="SourceWorkingEnvironmentName">SourceWorkingEnvironmentName</a>: <i>String</i>
    <a href="#throughput" title="Throughput">Throughput</a>: <i>Double</i>
</pre>

## Properties

#### CapacityTier

The volume's capacity tier for tiering cold data to object storage: ['S3', 'Blob', 'cloudStorage']. The default values for each cloud provider are as follows: Amazon => 'S3', Azure => 'Blob', GCP => 'cloudStorage'. If none, the capacity tier won't be set on volume creation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

The client ID of the Cloud Manager Connector. You can find the ID from a previous create Connector action as shown in the example, or from the Connector tab on [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAggregateName

The aggregate in which the volume will be created. If not provided, Cloud Manager chooses the best aggregate for you.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationSvmName

The name of the destination SVM. The default SVM name is used, if a name isn't provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationVolumeName

The name of the destination volume to be created for snapmirror relationship.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationWorkingEnvironmentId

The public ID of the destination working environment where the snapmirror relationship will be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationWorkingEnvironmentName

The destination working environment name where the snapmirror relationship will be created. It will be ignored if working_environment_id is provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iops

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTransferRate

Maximum transfer rate limit (KB/s). Use 0 for no limit, otherwise use number between 1024 and 2,147,482,624.  The default is 100000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

The SnapMirror policy name. The default is 'MirrorAllSnapshots'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderVolumeType

The underlying cloud provider volume type. For AWS: ['gp3', 'gp2', 'io1', 'st1', 'sc1']. For Azure: ['Premium_LRS','Standard_LRS','StandardSSD_LRS']. For GCP: ['pd-ssd','pd-standard'].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

Schedule name. The default is '1hour'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSvmName

The name of the source SVM. The default SVM name is used, if a name isn't provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceVolumeName

The name of the source volume.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceWorkingEnvironmentId

The public ID of the source working environment where the snapmirror relationship will be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceWorkingEnvironmentName

The source working environment name where the snapmirror relationship will be created. It will be ignored if working_environment_id is provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throughput

_Required_: No

_Type_: Double

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

