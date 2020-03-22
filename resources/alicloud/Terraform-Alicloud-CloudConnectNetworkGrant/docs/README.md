# Terraform::Alicloud::CloudConnectNetworkGrant

Provides a Cloud Connect Network Grant resource. If the CEN instance to be attached belongs to another account, authorization by the CEN instance is required.

For information about Cloud Connect Network Grant and how to use it, see [What is Cloud Connect Network Grant](https://www.alibabacloud.com/help/doc-detail/94543.htm).

-> **NOTE:** Available in 1.63.0+

-> **NOTE:** Only the following regions support create Cloud Connect Network Grant. [`cn-shanghai`, `cn-shanghai-finance-1`, `cn-hongkong`, `ap-southeast-1`, `ap-southeast-2`, `ap-southeast-3`, `ap-southeast-5`, `ap-northeast-1`, `eu-central-1`]

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CloudConnectNetworkGrant",
    "Properties" : {
        "<a href="#ccnid" title="CcnId">CcnId</a>" : <i>String</i>,
        "<a href="#cenid" title="CenId">CenId</a>" : <i>String</i>,
        "<a href="#cenuid" title="CenUid">CenUid</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CloudConnectNetworkGrant
Properties:
    <a href="#ccnid" title="CcnId">CcnId</a>: <i>String</i>
    <a href="#cenid" title="CenId">CenId</a>: <i>String</i>
    <a href="#cenuid" title="CenUid">CenUid</a>: <i>String</i>
</pre>

## Properties

#### CcnId

The ID of the CCN instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CenId

The ID of the CEN instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CenUid

The ID of the account to which the CEN instance belongs.

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

#### Id

Returns the <code>Id</code> value.

