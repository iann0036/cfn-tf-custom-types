# TF::TencentCloud::Image

Provide a resource to manage image.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::Image",
    "Properties" : {
        "<a href="#datadiskids" title="DataDiskIds">DataDiskIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#forcepoweroff" title="ForcePoweroff">ForcePoweroff</a>" : <i>Boolean</i>,
        "<a href="#imagedescription" title="ImageDescription">ImageDescription</a>" : <i>String</i>,
        "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#snapshotids" title="SnapshotIds">SnapshotIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#sysprep" title="Sysprep">Sysprep</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::Image
Properties:
    <a href="#datadiskids" title="DataDiskIds">DataDiskIds</a>: <i>
      - String</i>
    <a href="#forcepoweroff" title="ForcePoweroff">ForcePoweroff</a>: <i>Boolean</i>
    <a href="#imagedescription" title="ImageDescription">ImageDescription</a>: <i>String</i>
    <a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#snapshotids" title="SnapshotIds">SnapshotIds</a>: <i>
      - String</i>
    <a href="#sysprep" title="Sysprep">Sysprep</a>: <i>Boolean</i>
</pre>

## Properties

#### DataDiskIds

Cloud disk ID list, When creating a whole machine image based on an instance, specify the data disk ID contained in the image.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForcePoweroff

Set whether to force shutdown during mirroring. The default value is `false`, when set to true, it means that the mirror will be made after shutdown.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageDescription

Image Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageName

Image name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

Cloud server instance ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotIds

Cloud disk snapshot ID list; creating a mirror based on a snapshot must include a system disk snapshot. It cannot be passed in simultaneously with InstanceId.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sysprep

Sysprep function under Windows. When creating a Windows image, you can select true or false to enable or disable the Syspre function.

_Required_: No

_Type_: Boolean

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

