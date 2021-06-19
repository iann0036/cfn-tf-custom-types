# TF::NetAppCloudManager::Volume

Provides a netapp-cloudmanager_volume resource. This can be used to create, update, and delete volumes for Cloud Volumes ONTAP.
Requires existence of a Cloud Manager Connector and a Cloud Volumes ONTAP system.
NFS, CIFS, and iSCSI volumes are supported.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::Volume",
    "Properties" : {
        "<a href="#aggregatename" title="AggregateName">AggregateName</a>" : <i>String</i>,
        "<a href="#capacitytier" title="CapacityTier">CapacityTier</a>" : <i>String</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#enablecompression" title="EnableCompression">EnableCompression</a>" : <i>Boolean</i>,
        "<a href="#enablededuplication" title="EnableDeduplication">EnableDeduplication</a>" : <i>Boolean</i>,
        "<a href="#enablethinprovisioning" title="EnableThinProvisioning">EnableThinProvisioning</a>" : <i>Boolean</i>,
        "<a href="#exportpolicyip" title="ExportPolicyIp">ExportPolicyIp</a>" : <i>[ String, ... ]</i>,
        "<a href="#exportpolicyname" title="ExportPolicyName">ExportPolicyName</a>" : <i>String</i>,
        "<a href="#exportpolicynfsversion" title="ExportPolicyNfsVersion">ExportPolicyNfsVersion</a>" : <i>[ String, ... ]</i>,
        "<a href="#exportpolicytype" title="ExportPolicyType">ExportPolicyType</a>" : <i>String</i>,
        "<a href="#igroups" title="Igroups">Igroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#osname" title="OsName">OsName</a>" : <i>String</i>,
        "<a href="#permission" title="Permission">Permission</a>" : <i>String</i>,
        "<a href="#providervolumetype" title="ProviderVolumeType">ProviderVolumeType</a>" : <i>String</i>,
        "<a href="#sharename" title="ShareName">ShareName</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#snapshotpolicyname" title="SnapshotPolicyName">SnapshotPolicyName</a>" : <i>String</i>,
        "<a href="#svmname" title="SvmName">SvmName</a>" : <i>String</i>,
        "<a href="#throughput" title="Throughput">Throughput</a>" : <i>Double</i>,
        "<a href="#tieringpolicy" title="TieringPolicy">TieringPolicy</a>" : <i>String</i>,
        "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ String, ... ]</i>,
        "<a href="#volumeprotocol" title="VolumeProtocol">VolumeProtocol</a>" : <i>String</i>,
        "<a href="#workingenvironmentid" title="WorkingEnvironmentId">WorkingEnvironmentId</a>" : <i>String</i>,
        "<a href="#workingenvironmentname" title="WorkingEnvironmentName">WorkingEnvironmentName</a>" : <i>String</i>,
        "<a href="#initiator" title="Initiator">Initiator</a>" : <i>[ <a href="initiatordefinition.md">InitiatorDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::Volume
Properties:
    <a href="#aggregatename" title="AggregateName">AggregateName</a>: <i>String</i>
    <a href="#capacitytier" title="CapacityTier">CapacityTier</a>: <i>String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#enablecompression" title="EnableCompression">EnableCompression</a>: <i>Boolean</i>
    <a href="#enablededuplication" title="EnableDeduplication">EnableDeduplication</a>: <i>Boolean</i>
    <a href="#enablethinprovisioning" title="EnableThinProvisioning">EnableThinProvisioning</a>: <i>Boolean</i>
    <a href="#exportpolicyip" title="ExportPolicyIp">ExportPolicyIp</a>: <i>
      - String</i>
    <a href="#exportpolicyname" title="ExportPolicyName">ExportPolicyName</a>: <i>String</i>
    <a href="#exportpolicynfsversion" title="ExportPolicyNfsVersion">ExportPolicyNfsVersion</a>: <i>
      - String</i>
    <a href="#exportpolicytype" title="ExportPolicyType">ExportPolicyType</a>: <i>String</i>
    <a href="#igroups" title="Igroups">Igroups</a>: <i>
      - String</i>
    <a href="#iops" title="Iops">Iops</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#osname" title="OsName">OsName</a>: <i>String</i>
    <a href="#permission" title="Permission">Permission</a>: <i>String</i>
    <a href="#providervolumetype" title="ProviderVolumeType">ProviderVolumeType</a>: <i>String</i>
    <a href="#sharename" title="ShareName">ShareName</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#snapshotpolicyname" title="SnapshotPolicyName">SnapshotPolicyName</a>: <i>String</i>
    <a href="#svmname" title="SvmName">SvmName</a>: <i>String</i>
    <a href="#throughput" title="Throughput">Throughput</a>: <i>Double</i>
    <a href="#tieringpolicy" title="TieringPolicy">TieringPolicy</a>: <i>String</i>
    <a href="#unit" title="Unit">Unit</a>: <i>String</i>
    <a href="#users" title="Users">Users</a>: <i>
      - String</i>
    <a href="#volumeprotocol" title="VolumeProtocol">VolumeProtocol</a>: <i>String</i>
    <a href="#workingenvironmentid" title="WorkingEnvironmentId">WorkingEnvironmentId</a>: <i>String</i>
    <a href="#workingenvironmentname" title="WorkingEnvironmentName">WorkingEnvironmentName</a>: <i>String</i>
    <a href="#initiator" title="Initiator">Initiator</a>: <i>
      - <a href="initiatordefinition.md">InitiatorDefinition</a></i>
</pre>

## Properties

#### AggregateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### EnableCompression

Enable compression. The default is 'true'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDeduplication

Enable deduplication. The default is 'true'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableThinProvisioning

Enable thin provisioning. The default is 'true'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportPolicyIp

Custom export policy list of IPs. (NFS protocol parameters).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportPolicyName

The export policy name. (NFS protocol parameters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportPolicyNfsVersion

Export policy protocol. (NFS protocol parameters).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportPolicyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Igroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iops

Provisioned IOPS. Needed only when 'provider_volume_type' is 'io1' or 'gp3'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the volume.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permission

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderVolumeType

The underlying cloud provider volume type. For AWS: ['gp3', 'gp2', 'io1', 'st1', 'sc1']. For Azure: ['Premium_LRS','Standard_LRS','StandardSSD_LRS']. For GCP: ['pd-ssd','pd-standard'].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The volume size, supported with decimal numbers.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotPolicyName

Snapshot policy name. The default is 'default'. (NFS protocol parameters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvmName

The name of the SVM. The default SVM name is used, if a name isn't provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throughput

Required only when 'provider_volume_type' is 'gp3'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TieringPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeProtocol

The protocol for the volume: ['nfs', 'cifs', 'iscsi']. This affects the provided parameters. The default is 'nfs'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingEnvironmentId

The public ID of the working environment where the volume will be created. The ID can be optional if working_environment_name is provided. You can find the ID from the previous create Cloud Volumes ONTAP action as shown in the example, or from the Information page of the Cloud Volumes ONTAP working environment on [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingEnvironmentName

The working environment name where the aggregate will be created. It will be ignored if working_environment_id is provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Initiator

_Required_: No

_Type_: List of <a href="initiatordefinition.md">InitiatorDefinition</a>

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

