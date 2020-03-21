# Terraform::OPC::ComputeImageListEntry

The ``opc_compute_image_list_entry`` resource creates and manages an Image List Entry in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::ComputeImageListEntry",
    "Properties" : {
        "<a href="#attributes" title="Attributes">Attributes</a>" : <i>String</i>,
        "<a href="#machineimages" title="MachineImages">MachineImages</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::ComputeImageListEntry
Properties:
    <a href="#attributes" title="Attributes">Attributes</a>: <i>String</i>
    <a href="#machineimages" title="MachineImages">MachineImages</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### Attributes

JSON String of optional data that will be passed to an instance of this machine image when it is launched.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineImages

An array of machine images.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Image List.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The unique version of the image list entry, as an integer.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Uri

Returns the <code>Uri</code> value.

