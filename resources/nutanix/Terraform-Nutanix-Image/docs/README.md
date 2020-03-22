# Terraform::Nutanix::Image

Provides a Nutanix Image resource to Create a image.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Nutanix::Image",
    "Properties" : {
        "<a href="#architecture" title="Architecture">Architecture</a>" : <i>String</i>,
        "<a href="#availabilityzonereference" title="AvailabilityZoneReference">AvailabilityZoneReference</a>" : <i>[ <a href="availabilityzonereference.md">AvailabilityZoneReference</a>, ... ]</i>,
        "<a href="#checksum" title="Checksum">Checksum</a>" : <i>[ <a href="checksum.md">Checksum</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#imagetype" title="ImageType">ImageType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ <a href="ownerreference.md">OwnerReference</a>, ... ]</i>,
        "<a href="#projectreference" title="ProjectReference">ProjectReference</a>" : <i>[ <a href="projectreference.md">ProjectReference</a>, ... ]</i>,
        "<a href="#sourcepath" title="SourcePath">SourcePath</a>" : <i>String</i>,
        "<a href="#sourceuri" title="SourceUri">SourceUri</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>[ <a href="version.md">Version</a>, ... ]</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categories.md">Categories</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Nutanix::Image
Properties:
    <a href="#architecture" title="Architecture">Architecture</a>: <i>String</i>
    <a href="#availabilityzonereference" title="AvailabilityZoneReference">AvailabilityZoneReference</a>: <i>
      - <a href="availabilityzonereference.md">AvailabilityZoneReference</a></i>
    <a href="#checksum" title="Checksum">Checksum</a>: <i>
      - <a href="checksum.md">Checksum</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#imagetype" title="ImageType">ImageType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - <a href="ownerreference.md">OwnerReference</a></i>
    <a href="#projectreference" title="ProjectReference">ProjectReference</a>: <i>
      - <a href="projectreference.md">ProjectReference</a></i>
    <a href="#sourcepath" title="SourcePath">SourcePath</a>: <i>String</i>
    <a href="#sourceuri" title="SourceUri">SourceUri</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>
      - <a href="version.md">Version</a></i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categories.md">Categories</a></i>
</pre>

## Properties

#### Architecture

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZoneReference

_Required_: No

_Type_: List of <a href="availabilityzonereference.md">AvailabilityZoneReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Checksum

_Required_: No

_Type_: List of <a href="checksum.md">Checksum</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerReference

_Required_: No

_Type_: List of <a href="ownerreference.md">OwnerReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectReference

_Required_: No

_Type_: List of <a href="projectreference.md">ProjectReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: List of <a href="version.md">Version</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categories.md">Categories</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiVersion

Returns the <code>ApiVersion</code> value.

#### ClusterName

Returns the <code>ClusterName</code> value.

#### ClusterUuid

Returns the <code>ClusterUuid</code> value.

#### Id

Returns the <code>Id</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### RetrievalUriList

Returns the <code>RetrievalUriList</code> value.

#### SizeBytes

Returns the <code>SizeBytes</code> value.

#### State

Returns the <code>State</code> value.

