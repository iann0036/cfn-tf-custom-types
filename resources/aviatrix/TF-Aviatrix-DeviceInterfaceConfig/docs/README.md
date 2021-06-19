# TF::Aviatrix::DeviceInterfaceConfig

The **aviatrix_device_interface_config** resource allows the configuration of the primary WAN interface and IP for a device, for use in CloudWAN.

~> **NOTE:** Before configuring WAN interface and IP, the device must be registered with the Aviatrix controller via the `aviatrix_device_registration` resource. To guarantee the correct order of resource creation please set an explicit or implicit dependency on the corresponding `aviatrix_device_registration` resource. For an example of an implicit dependency please see the Example Usage section below. For explicit dependency please utilize a `depends_on` meta-argument within this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::DeviceInterfaceConfig",
    "Properties" : {
        "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
        "<a href="#wanprimaryinterface" title="WanPrimaryInterface">WanPrimaryInterface</a>" : <i>String</i>,
        "<a href="#wanprimaryinterfacepublicip" title="WanPrimaryInterfacePublicIp">WanPrimaryInterfacePublicIp</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::DeviceInterfaceConfig
Properties:
    <a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
    <a href="#wanprimaryinterface" title="WanPrimaryInterface">WanPrimaryInterface</a>: <i>String</i>
    <a href="#wanprimaryinterfacepublicip" title="WanPrimaryInterfacePublicIp">WanPrimaryInterfacePublicIp</a>: <i>String</i>
</pre>

## Properties

#### DeviceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanPrimaryInterface

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanPrimaryInterfacePublicIp

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

