# TF::NetAppGCP::Volume

CloudFormation equivalent of netapp-gcp_volume

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppGCP::Volume",
    "Properties" : {
        "<a href="#deleteoncreationerror" title="DeleteOnCreationError">DeleteOnCreationError</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#protocoltypes" title="ProtocolTypes">ProtocolTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#regionalha" title="RegionalHa">RegionalHa</a>" : <i>Boolean</i>,
        "<a href="#servicelevel" title="ServiceLevel">ServiceLevel</a>" : <i>String</i>,
        "<a href="#sharedvpcprojectnumber" title="SharedVpcProjectNumber">SharedVpcProjectNumber</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>,
        "<a href="#typedp" title="TypeDp">TypeDp</a>" : <i>Boolean</i>,
        "<a href="#volumepath" title="VolumePath">VolumePath</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#exportpolicy" title="ExportPolicy">ExportPolicy</a>" : <i>[ <a href="exportpolicydefinition.md">ExportPolicyDefinition</a>, ... ]</i>,
        "<a href="#mountpoints" title="MountPoints">MountPoints</a>" : <i>[ <a href="mountpointsdefinition.md">MountPointsDefinition</a>, ... ]</i>,
        "<a href="#snapshotpolicy" title="SnapshotPolicy">SnapshotPolicy</a>" : <i>[ <a href="snapshotpolicydefinition.md">SnapshotPolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppGCP::Volume
Properties:
    <a href="#deleteoncreationerror" title="DeleteOnCreationError">DeleteOnCreationError</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#protocoltypes" title="ProtocolTypes">ProtocolTypes</a>: <i>
      - String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#regionalha" title="RegionalHa">RegionalHa</a>: <i>Boolean</i>
    <a href="#servicelevel" title="ServiceLevel">ServiceLevel</a>: <i>String</i>
    <a href="#sharedvpcprojectnumber" title="SharedVpcProjectNumber">SharedVpcProjectNumber</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
    <a href="#typedp" title="TypeDp">TypeDp</a>: <i>Boolean</i>
    <a href="#volumepath" title="VolumePath">VolumePath</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#exportpolicy" title="ExportPolicy">ExportPolicy</a>: <i>
      - <a href="exportpolicydefinition.md">ExportPolicyDefinition</a></i>
    <a href="#mountpoints" title="MountPoints">MountPoints</a>: <i>
      - <a href="mountpointsdefinition.md">MountPointsDefinition</a></i>
    <a href="#snapshotpolicy" title="SnapshotPolicy">SnapshotPolicy</a>: <i>
      - <a href="snapshotpolicydefinition.md">SnapshotPolicyDefinition</a></i>
</pre>

## Properties

#### DeleteOnCreationError

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionalHa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedVpcProjectNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeDp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportPolicy

_Required_: No

_Type_: List of <a href="exportpolicydefinition.md">ExportPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountPoints

_Required_: No

_Type_: List of <a href="mountpointsdefinition.md">MountPointsDefinition</a>

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

