# Terraform::TencentCloud::CbsStorageAttachment

Provides a CBS storage attachment resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::CbsStorageAttachment",
    "Properties" : {
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#storageid" title="StorageId">StorageId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::CbsStorageAttachment
Properties:
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#storageid" title="StorageId">StorageId</a>: <i>String</i>
</pre>

## Properties

#### InstanceId

ID of the CVM instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageId

ID of the mounted CBS.

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

