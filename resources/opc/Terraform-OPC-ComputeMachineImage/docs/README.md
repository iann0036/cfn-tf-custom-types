# Terraform::OPC::ComputeMachineImage

The ``opc_compute_machine_image`` resource creates and manages a machine image template of a virtual hard disk of a specific size with an installed operating system.

Before performing this creating the Machine Image, you must upload your machine image file to Oracle Cloud Infrastructure Object Storage Classic `compute_images` container

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::ComputeMachineImage",
    "Properties" : {
        "<a href="#account" title="Account">Account</a>" : <i>String</i>,
        "<a href="#attributes" title="Attributes">Attributes</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#file" title="File">File</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::ComputeMachineImage
Properties:
    <a href="#account" title="Account">Account</a>: <i>String</i>
    <a href="#attributes" title="Attributes">Attributes</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#file" title="File">File</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Account

The two part name of the compute object storage account in the format `/Compute-{identity_domain}/cloud_storage`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attributes

An optional JSON object of arbitrary attributes to be made available to the instance. These are user-defined tags. After defining attributes, you can view them from within an instance at http://192.0.0.192/.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the Machine Image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### File

The name of the Machine Image .tar.gz file in the `compute_images` storage container.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Machine Image.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ErrorReason

Description of the state of the machine image if there is an error.

#### Hypervisor

Dictionary of hypervisor-specific attributes.

#### Id

Returns the <code>Id</code> value.

#### ImageFormat

The format of the image.

#### NoUpload

Returns the <code>NoUpload</code> value.

#### Platform

The OS platform of the image.

#### State

The state of the uploaded machine image.

#### Uri

The Uniform Resource Identifier for the Machine Image.

