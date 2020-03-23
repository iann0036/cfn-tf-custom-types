# Terraform::AWS::VolumeAttachment

Provides an AWS EBS Volume Attachment as a top level resource, to attach and
detach volumes from AWS Instances.

~> **NOTE on EBS block devices:** If you use `ebs_block_device` on an `aws_instance`, Terraform will assume management over the full set of non-root EBS block devices for the instance, and treats additional block devices as drift. For this reason, `ebs_block_device` cannot be mixed with external `aws_ebs_volume` + `aws_ebs_volume_attachment` resources for a given instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::VolumeAttachment",
    "Properties" : {
        "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
        "<a href="#forcedetach" title="ForceDetach">ForceDetach</a>" : <i>Boolean</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#skipdestroy" title="SkipDestroy">SkipDestroy</a>" : <i>Boolean</i>,
        "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::VolumeAttachment
Properties:
    <a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
    <a href="#forcedetach" title="ForceDetach">ForceDetach</a>: <i>Boolean</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#skipdestroy" title="SkipDestroy">SkipDestroy</a>: <i>Boolean</i>
    <a href="#volumeid" title="VolumeId">VolumeId</a>: <i>String</i>
</pre>

## Properties

#### DeviceName

The device name to expose to the instance (for
example, `/dev/sdh` or `xvdh`).  See [Device Naming on Linux Instances][1] and [Device Naming on Windows Instances][2] for more information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDetach

Set to `true` if you want to force the
volume to detach. Useful if previous attempts failed, but use this option only
as a last resort, as this can result in **data loss**. See
[Detaching an Amazon EBS Volume from an Instance][3] for more information.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

ID of the Instance to attach to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipDestroy

Set this to true if you do not wish
to detach the volume from the instance to which it is attached at destroy
time, and instead just remove the attachment from Terraform state. This is
useful when destroying an instance which has volumes created by some other
means attached.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeId

ID of the Volume to be attached.

_Required_: Yes

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

