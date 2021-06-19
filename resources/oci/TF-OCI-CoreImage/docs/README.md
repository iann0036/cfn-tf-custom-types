# TF::OCI::CoreImage

This resource provides the Image resource in Oracle Cloud Infrastructure Core service.

Creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object Storage service.

When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and
the OCID of the compartment containing that instance. For more information about images,
see [Managing Custom Images](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm).

When importing an exported image from Object Storage, you specify the source information
in [ImageSourceDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceDetails).

When importing an image based on the namespace, bucket name, and object name,
use [ImageSourceViaObjectStorageTupleDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceViaObjectStorageTupleDetails).

When importing an image based on the...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CoreImage",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#launchmode" title="LaunchMode">LaunchMode</a>" : <i>String</i>,
        "<a href="#imagesourcedetails" title="ImageSourceDetails">ImageSourceDetails</a>" : <i>[ <a href="imagesourcedetailsdefinition.md">ImageSourceDetailsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CoreImage
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#launchmode" title="LaunchMode">LaunchMode</a>: <i>String</i>
    <a href="#imagesourcedetails" title="ImageSourceDetails">ImageSourceDetails</a>: <i>
      - <a href="imagesourcedetailsdefinition.md">ImageSourceDetailsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
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

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name for the image. It does not have to be unique, and it's changeable. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The OCID of the instance you want to use as the basis for the image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchMode

Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
* `NATIVE` - VM instances launch with paravirtualized boot and VFIO devices. The default value for platform images.
* `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
* `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
* `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageSourceDetails

_Required_: No

_Type_: List of <a href="imagesourcedetailsdefinition.md">ImageSourceDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### BillableSizeInGbs

Returns the <code>BillableSizeInGbs</code> value.

#### CreateImageAllowed

Returns the <code>CreateImageAllowed</code> value.

#### Id

Returns the <code>Id</code> value.

#### LaunchOptions

Returns the <code>LaunchOptions</code> value.

#### ListingType

Returns the <code>ListingType</code> value.

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

