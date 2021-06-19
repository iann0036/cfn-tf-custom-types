# TF::Panos::PanoramaDeviceGroupEntry

This resource allows you to add/update/delete a specific device in a Panorama
device group.

This resource has some overlap with the `panos_panorama_device_group`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_panorama_device_group` spec does not define any
`device` blocks, and just stays as "computed".

This is the appropriate resource to use if you have a pre-existing device group
in Panorama and don't want Terraform to delete it on `terraform destroy`.

An interesting side effect of the underlying XML API - if the device group does
not already exist, then this resource can actually create it.  However, since
only the single entry for the specific serial number is deleted, then a
`terraform destroy` would not remove the device group itself in this situation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::PanoramaDeviceGroupEntry",
    "Properties" : {
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#serial" title="Serial">Serial</a>" : <i>String</i>,
        "<a href="#vsyslist" title="VsysList">VsysList</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::PanoramaDeviceGroupEntry
Properties:
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#serial" title="Serial">Serial</a>: <i>String</i>
    <a href="#vsyslist" title="VsysList">VsysList</a>: <i>
      - String</i>
</pre>

## Properties

#### DeviceGroup

The device group's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Serial

The serial number of the firewall.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsysList

A subset of all available vsys on the firewall
that should be in this device group.  If the firewall is a virtual firewall,
then this parameter should just be omitted.

_Required_: No

_Type_: List of String

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

