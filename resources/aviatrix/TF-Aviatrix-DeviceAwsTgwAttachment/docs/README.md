# TF::Aviatrix::DeviceAwsTgwAttachment

The **aviatrix_device_aws_tgw_attachment** resource allows the creation and management of a device and AWS TGW attachment

~> **NOTE:** Before creating this attachment the device must have its WAN interface and IP configured via the `aviatrix_device_interface_config` resource. To avoid attempting to create the attachment before the interface and IP are configured use a `depends_on` meta-argument so that the `aviatrix_device_interface_config` resource is created before the attachment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::DeviceAwsTgwAttachment",
    "Properties" : {
        "<a href="#awstgwname" title="AwsTgwName">AwsTgwName</a>" : <i>String</i>,
        "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
        "<a href="#devicebgpasn" title="DeviceBgpAsn">DeviceBgpAsn</a>" : <i>Double</i>,
        "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
        "<a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::DeviceAwsTgwAttachment
Properties:
    <a href="#awstgwname" title="AwsTgwName">AwsTgwName</a>: <i>String</i>
    <a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
    <a href="#devicebgpasn" title="DeviceBgpAsn">DeviceBgpAsn</a>: <i>Double</i>
    <a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
    <a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>: <i>String</i>
</pre>

## Properties

#### AwsTgwName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceBgpAsn

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityDomainName

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

