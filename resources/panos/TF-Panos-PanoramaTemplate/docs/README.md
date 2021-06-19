# TF::Panos::PanoramaTemplate

This resource allows you to add/update/delete Panorama templates.

This resource has some overlap with the `panos_panorama_template_entry`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_panorama_template` spec does not define any
`device` blocks, and just stays as "computed".

This is the appropriate resource to use if `terraform destroy` should delete
the template.

**Note** - In PAN-OS 8.1, it looks like the `devices` field has
been removed.  Creating a template stack and specifying devices in the template
stack is still present in PAN-OS 8.1.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::PanoramaTemplate",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#devices" title="Devices">Devices</a>" : <i>[ <a href="devicesdefinition.md">DevicesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::PanoramaTemplate
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#devices" title="Devices">Devices</a>: <i>
      - <a href="devicesdefinition.md">DevicesDefinition</a></i>
</pre>

## Properties

#### Description

The template's description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The template's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devices

_Required_: No

_Type_: List of <a href="devicesdefinition.md">DevicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DefaultVsys

Returns the <code>DefaultVsys</code> value.

#### Id

Returns the <code>Id</code> value.

