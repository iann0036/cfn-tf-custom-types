# TF::NetAppCloudManager::CvsGcpVolume

Provides a netapp-cloudmanager_cvs_gcp_volume resource. This can be used to create, and delete volumes for Cloud Volume Service on GCP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::CvsGcpVolume",
    "Properties" : {
        "<a href="#account" title="Account">Account</a>" : <i>String</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#protocoltypes" title="ProtocolTypes">ProtocolTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#servicelevel" title="ServiceLevel">ServiceLevel</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#sizeunit" title="SizeUnit">SizeUnit</a>" : <i>String</i>,
        "<a href="#volumepath" title="VolumePath">VolumePath</a>" : <i>String</i>,
        "<a href="#workingenvironmentname" title="WorkingEnvironmentName">WorkingEnvironmentName</a>" : <i>String</i>,
        "<a href="#exportpolicy" title="ExportPolicy">ExportPolicy</a>" : <i>[ <a href="exportpolicydefinition.md">ExportPolicyDefinition</a>, ... ]</i>,
        "<a href="#snapshotpolicy" title="SnapshotPolicy">SnapshotPolicy</a>" : <i>[ <a href="snapshotpolicydefinition.md">SnapshotPolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::CvsGcpVolume
Properties:
    <a href="#account" title="Account">Account</a>: <i>String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#protocoltypes" title="ProtocolTypes">ProtocolTypes</a>: <i>
      - String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#servicelevel" title="ServiceLevel">ServiceLevel</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#sizeunit" title="SizeUnit">SizeUnit</a>: <i>String</i>
    <a href="#volumepath" title="VolumePath">VolumePath</a>: <i>String</i>
    <a href="#workingenvironmentname" title="WorkingEnvironmentName">WorkingEnvironmentName</a>: <i>String</i>
    <a href="#exportpolicy" title="ExportPolicy">ExportPolicy</a>: <i>
      - <a href="exportpolicydefinition.md">ExportPolicyDefinition</a></i>
    <a href="#snapshotpolicy" title="SnapshotPolicy">SnapshotPolicy</a>: <i>
      - <a href="snapshotpolicydefinition.md">SnapshotPolicyDefinition</a></i>
</pre>

## Properties

#### Account

The name of the account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

The client ID of the Cloud Manager Connector. You can find the ID from a previous create Connector action as shown in the example, or from the Connector tab on [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the volume.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

The network VPC of the volume.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region where the volume is created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceLevel

['low' or 'medium' or 'high'].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The volume size, supported with decimal numbers.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeUnit

[ 'gb' ].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumePath

The volume path.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingEnvironmentName

The working environment name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportPolicy

_Required_: No

_Type_: List of <a href="exportpolicydefinition.md">ExportPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotPolicy

_Required_: No

_Type_: List of <a href="snapshotpolicydefinition.md">SnapshotPolicyDefinition</a>

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

