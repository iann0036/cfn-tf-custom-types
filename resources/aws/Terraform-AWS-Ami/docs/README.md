# Terraform::AWS::Ami

The AMI resource allows the creation and management of a completely-custom
*Amazon Machine Image* (AMI).

If you just want to duplicate an existing AMI, possibly copying it to another
region, it's better to use `aws_ami_copy` instead.

If you just want to share an existing AMI with another AWS account,
it's better to use `aws_ami_launch_permission` instead.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Ami",
    "Properties" : {
        "<a href="#architecture" title="Architecture">Architecture</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enasupport" title="EnaSupport">EnaSupport</a>" : <i>Boolean</i>,
        "<a href="#imagelocation" title="ImageLocation">ImageLocation</a>" : <i>String</i>,
        "<a href="#kernelid" title="KernelId">KernelId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ramdiskid" title="RamdiskId">RamdiskId</a>" : <i>String</i>,
        "<a href="#rootdevicename" title="RootDeviceName">RootDeviceName</a>" : <i>String</i>,
        "<a href="#sriovnetsupport" title="SriovNetSupport">SriovNetSupport</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#virtualizationtype" title="VirtualizationType">VirtualizationType</a>" : <i>String</i>,
        "<a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>" : <i>[ <a href="ebsblockdevice.md">EbsBlockDevice</a>, ... ]</i>,
        "<a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>" : <i>[ <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Ami
Properties:
    <a href="#architecture" title="Architecture">Architecture</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enasupport" title="EnaSupport">EnaSupport</a>: <i>Boolean</i>
    <a href="#imagelocation" title="ImageLocation">ImageLocation</a>: <i>String</i>
    <a href="#kernelid" title="KernelId">KernelId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ramdiskid" title="RamdiskId">RamdiskId</a>: <i>String</i>
    <a href="#rootdevicename" title="RootDeviceName">RootDeviceName</a>: <i>String</i>
    <a href="#sriovnetsupport" title="SriovNetSupport">SriovNetSupport</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#virtualizationtype" title="VirtualizationType">VirtualizationType</a>: <i>String</i>
    <a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>: <i>
      - <a href="ebsblockdevice.md">EbsBlockDevice</a></i>
    <a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>: <i>
      - <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Architecture

Machine architecture for created instances. Defaults to "x86_64".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A longer, human-readable description for the AMI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnaSupport

Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A region-unique name for the AMI.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RamdiskId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootDeviceName

The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SriovNetSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualizationType

Keyword to choose what virtualization mode created instances
will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
changes the set of further arguments that are required, as described below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsBlockDevice

_Required_: No

_Type_: List of <a href="ebsblockdevice.md">EbsBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralBlockDevice

_Required_: No

_Type_: List of <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

#### ManageEbsSnapshots

Returns the <code>ManageEbsSnapshots</code> value.

#### RootSnapshotId

Returns the <code>RootSnapshotId</code> value.

