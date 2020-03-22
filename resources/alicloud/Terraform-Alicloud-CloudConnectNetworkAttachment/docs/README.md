# Terraform::Alicloud::CloudConnectNetworkAttachment

Provides a Cloud Connect Network Attachment resource. This topic describes how to associate a Smart Access Gateway (SAG) instance with a network instance. You must associate an SAG instance with a network instance if you want to connect the SAG to Alibaba Cloud. You can connect an SAG to Alibaba Cloud through a leased line, the Internet, or the active and standby links.

For information about Cloud Connect Network Attachment and how to use it, see [What is Cloud Connect Network Attachment](https://www.alibabacloud.com/help/doc-detail/124230.htm).

-> **NOTE:** Available in 1.64.0+

-> **NOTE:** Only the following regions support. [`cn-shanghai`, `cn-shanghai-finance-1`, `cn-hongkong`, `ap-southeast-1`, `ap-southeast-2`, `ap-southeast-3`, `ap-southeast-5`, `ap-northeast-1`, `eu-central-1`]

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CloudConnectNetworkAttachment",
    "Properties" : {
        "<a href="#ccnid" title="CcnId">CcnId</a>" : <i>String</i>,
        "<a href="#sagid" title="SagId">SagId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CloudConnectNetworkAttachment
Properties:
    <a href="#ccnid" title="CcnId">CcnId</a>: <i>String</i>
    <a href="#sagid" title="SagId">SagId</a>: <i>String</i>
</pre>

## Properties

#### CcnId

The ID of the CCN instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SagId

The ID of the Smart Access Gateway instance.

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

