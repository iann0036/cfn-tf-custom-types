# TF::NetAppCloudManager::Aggregate

Provides a netapp-cloudmanager_aggregate resource. This can be used to create a new aggregate on Cloud Volumes ONTAP.
Requires existence of a Cloud Manager Connector and a Cloud Volumes ONTAP system.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::Aggregate",
    "Properties" : {
        "<a href="#capacitytier" title="CapacityTier">CapacityTier</a>" : <i>String</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#disksizesize" title="DiskSizeSize">DiskSizeSize</a>" : <i>Double</i>,
        "<a href="#disksizeunit" title="DiskSizeUnit">DiskSizeUnit</a>" : <i>String</i>,
        "<a href="#homenode" title="HomeNode">HomeNode</a>" : <i>String</i>,
        "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#numberofdisks" title="NumberOfDisks">NumberOfDisks</a>" : <i>Double</i>,
        "<a href="#providervolumetype" title="ProviderVolumeType">ProviderVolumeType</a>" : <i>String</i>,
        "<a href="#throughput" title="Throughput">Throughput</a>" : <i>Double</i>,
        "<a href="#workingenvironmentid" title="WorkingEnvironmentId">WorkingEnvironmentId</a>" : <i>String</i>,
        "<a href="#workingenvironmentname" title="WorkingEnvironmentName">WorkingEnvironmentName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::Aggregate
Properties:
    <a href="#capacitytier" title="CapacityTier">CapacityTier</a>: <i>String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#disksizesize" title="DiskSizeSize">DiskSizeSize</a>: <i>Double</i>
    <a href="#disksizeunit" title="DiskSizeUnit">DiskSizeUnit</a>: <i>String</i>
    <a href="#homenode" title="HomeNode">HomeNode</a>: <i>String</i>
    <a href="#iops" title="Iops">Iops</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#numberofdisks" title="NumberOfDisks">NumberOfDisks</a>: <i>Double</i>
    <a href="#providervolumetype" title="ProviderVolumeType">ProviderVolumeType</a>: <i>String</i>
    <a href="#throughput" title="Throughput">Throughput</a>: <i>Double</i>
    <a href="#workingenvironmentid" title="WorkingEnvironmentId">WorkingEnvironmentId</a>: <i>String</i>
    <a href="#workingenvironmentname" title="WorkingEnvironmentName">WorkingEnvironmentName</a>: <i>String</i>
</pre>

## Properties

#### CapacityTier

The aggregate's capacity tier for tiering cold data to object storage: ['S3', 'Blob', 'cloudStorage']. The default values for each cloud provider are as follows: Amazon => 'S3', Azure => 'Blob', GCP => 'cloudStorage'. If NONE, the capacity tier won't be set on aggregate creation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

The client ID of the Cloud Manager Connector. You can find the ID from a previous create Connector action as shown in the example, or from the Connector tab on [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeSize

The required size of the disks. For GB, the unit can be: [100 or 500]. For TB, the unit can be: [1,2,4,8,16]. The default is '1'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeUnit

The disk size unit ['GB' or 'TB']. The default is 'TB'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomeNode

The home node that the new aggregate should belong to. The default is the first node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iops

Provisioned IOPS. Needed only when 'providerVolumeType' is 'io1' or 'gp3'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the new aggregate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfDisks

The required number of disks in the new aggregate.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderVolumeType

The cloud provider volume type. For AWS: ['gp3', 'gp2', 'io1', 'st1', 'sc1']. For Azure: ['Premium_LRS','Standard_LRS','StandardSSD_LRS']. For GCP: ['pd-ssd','pd-standard'].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throughput

Required only when 'providerVolumeType' is 'gp3'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingEnvironmentId

The public ID of the working environment where the aggregate will be created. This argument is optional if working_environment_name is provided. You can find the ID from a previous create Cloud Volumes ONTAP action as shown in the example, or from the information page of the Cloud Volumes ONTAP working environment on [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingEnvironmentName

The working environment name where the aggregate will be created. This argument will be ignored if working_environment_id is provided.

_Required_: No

_Type_: String

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

