# Terraform::AWS::AmiCopy

The "AMI copy" resource allows duplication of an Amazon Machine Image (AMI),
including cross-region copies.

If the source AMI has associated EBS snapshots, those will also be duplicated
along with the AMI.

This is useful for taking a single AMI provisioned in one region and making
it available in another for a multi-region deployment.

Copying an AMI can take several minutes. The creation of this resource will
block until the new AMI is available for use on new instances.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AmiCopy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>Boolean</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sourceamiid" title="SourceAmiId">SourceAmiId</a>" : <i>String</i>,
        "<a href="#sourceamiregion" title="SourceAmiRegion">SourceAmiRegion</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AmiCopy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>Boolean</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sourceamiid" title="SourceAmiId">SourceAmiId</a>: <i>String</i>
    <a href="#sourceamiregion" title="SourceAmiRegion">SourceAmiRegion</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A region-unique name for the AMI.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAmiId

The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAmiRegion

The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

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

#### Architecture

Returns the <code>Architecture</code> value.

#### EnaSupport

Returns the <code>EnaSupport</code> value.

#### Id

Returns the <code>Id</code> value.

#### ImageLocation

Returns the <code>ImageLocation</code> value.

#### KernelId

Returns the <code>KernelId</code> value.

#### ManageEbsSnapshots

Returns the <code>ManageEbsSnapshots</code> value.

#### RamdiskId

Returns the <code>RamdiskId</code> value.

#### RootDeviceName

Returns the <code>RootDeviceName</code> value.

#### RootSnapshotId

Returns the <code>RootSnapshotId</code> value.

#### SriovNetSupport

Returns the <code>SriovNetSupport</code> value.

#### VirtualizationType

Returns the <code>VirtualizationType</code> value.

