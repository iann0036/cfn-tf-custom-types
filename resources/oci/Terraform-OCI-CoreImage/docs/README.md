# Terraform::OCI::CoreImage

This resource provides the Image resource in Oracle Cloud Infrastructure Core service.

Creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object Storage service.

When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and
the OCID of the compartment containing that instance. For more information about images,
see [Managing Custom Images](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm).

When importing an exported image from Object Storage, you specify the source information
in [ImageSourceDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceDetails).

When importing an image based on the namespace, bucket name, and object name,
use [ImageSourceViaObjectStorageTupleDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceViaObjectStorageTupleDetails).

When importing an image based on the Object Storage URL, use
[ImageSourceViaObjectStorageUriDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceViaObjectStorageUriDetails).
See [Object Storage URLs](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs) and [Using Pre-Authenticated Requests](https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)
for constructing URLs for image import/export.

For more information about importing exported images, see
[Image Import/Export](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm).

You may optionally specify a *display name* for the image, which is simply a friendly name or description.
It does not have to be unique, and you can change it. See [UpdateImage](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Image/UpdateImage).
Avoid entering confidential information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreImage",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#launchmode" title="LaunchMode">LaunchMode</a>" : <i>String</i>,
        "<a href="#imagesourcedetails" title="ImageSourceDetails">ImageSourceDetails</a>" : <i>[ <a href="imagesourcedetails.md">ImageSourceDetails</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreImage
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#launchmode" title="LaunchMode">LaunchMode</a>: <i>String</i>
    <a href="#imagesourcedetails" title="ImageSourceDetails">ImageSourceDetails</a>: <i>
      - <a href="imagesourcedetails.md">ImageSourceDetails</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The OCID of the compartment you want the image to be created in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name for the image. It does not have to be unique, and it's changeable. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The OCID of the instance you want to use as the basis for the image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchMode

Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
* `NATIVE` - VM instances launch with paravirtualized boot and VFIO devices. The default value for Oracle-provided images.
* `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
* `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers.
* `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageSourceDetails

_Required_: No

_Type_: List of <a href="imagesourcedetails.md">ImageSourceDetails</a>

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

#### AgentFeatures

Returns the <code>AgentFeatures</code> value.

#### BaseImageId

Returns the <code>BaseImageId</code> value.

#### CreateImageAllowed

Returns the <code>CreateImageAllowed</code> value.

#### Id

Returns the <code>Id</code> value.

#### LaunchOptions

Returns the <code>LaunchOptions</code> value.

#### OperatingSystem

The image's operating system.  Example: `Oracle Linux`
* `operating_system_version` - (Optional) The image's operating system version.  Example: `7.2`
* `source_image_type` - (Optional) The format of the image to be imported.  Only monolithic images are supported. This attribute is not used for exported Oracle images with the Oracle Cloud Infrastructure image format. Allowed values are:
* `QCOW2`
* `VMDK`
* `source_type` - (Required) The source type for the image. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.
* `source_uri` - (Required when source_type=objectStorageUri) The Object Storage URL for the image.

#### OperatingSystemVersion

The image's operating system version.  Example: `7.2`
* `source_image_type` - (Optional) The format of the image to be imported.  Only monolithic images are supported. This attribute is not used for exported Oracle images with the Oracle Cloud Infrastructure image format. Allowed values are:
* `QCOW2`
* `VMDK`
* `source_type` - (Required) The source type for the image. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.
* `source_uri` - (Required when source_type=objectStorageUri) The Object Storage URL for the image.

#### SizeInMbs

Returns the <code>SizeInMbs</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

