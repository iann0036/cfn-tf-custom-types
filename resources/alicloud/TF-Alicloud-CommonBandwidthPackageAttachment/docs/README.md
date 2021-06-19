# TF::Alicloud::CommonBandwidthPackageAttachment

Provides an Alicloud Common Bandwidth Package Attachment resource for associating Common Bandwidth Package to EIP Instance.

-> **NOTE:** Terraform will auto build common bandwidth package attachment while it uses `alicloud_common_bandwidth_package_attachment` to build a common bandwidth package attachment resource.

For information about common bandwidth package and how to use it, see [What is Common Bandwidth Package](https://www.alibabacloud.com/help/product/55092.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::CommonBandwidthPackageAttachment",
    "Properties" : {
        "<a href="#bandwidthpackageid" title="BandwidthPackageId">BandwidthPackageId</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::CommonBandwidthPackageAttachment
Properties:
    <a href="#bandwidthpackageid" title="BandwidthPackageId">BandwidthPackageId</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
</pre>

## Properties

#### BandwidthPackageId

The bandwidth_package_id of the common bandwidth package attachment, the field can't be changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The instance_id of the common bandwidth package attachment, the field can't be changed.

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

