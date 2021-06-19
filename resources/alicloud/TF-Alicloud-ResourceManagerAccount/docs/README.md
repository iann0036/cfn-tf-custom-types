# TF::Alicloud::ResourceManagerAccount

Provides a Resource Manager Account resource. Member accounts are containers for resources in a resource directory. These accounts isolate resources and serve as organizational units in the resource directory. You can create member accounts in a folder and then manage them in a unified manner.
For information about Resource Manager Account and how to use it, see [What is Resource Manager Account](https://www.alibabacloud.com/help/en/doc-detail/111231.htm).

-> **NOTE:** Available in v1.83.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ResourceManagerAccount",
    "Properties" : {
        "<a href="#accountnameprefix" title="AccountNamePrefix">AccountNamePrefix</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#folderid" title="FolderId">FolderId</a>" : <i>String</i>,
        "<a href="#payeraccountid" title="PayerAccountId">PayerAccountId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ResourceManagerAccount
Properties:
    <a href="#accountnameprefix" title="AccountNamePrefix">AccountNamePrefix</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#folderid" title="FolderId">FolderId</a>: <i>String</i>
    <a href="#payeraccountid" title="PayerAccountId">PayerAccountId</a>: <i>String</i>
</pre>

## Properties

#### AccountNamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (_), dots (.) And dashes (-).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FolderId

The ID of the parent folder.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PayerAccountId

Settlement account ID. If the value is empty, the current account will be used for settlement.

_Required_: No

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

#### JoinMethod

Returns the <code>JoinMethod</code> value.

#### JoinTime

Returns the <code>JoinTime</code> value.

#### ModifyTime

Returns the <code>ModifyTime</code> value.

#### ResourceDirectoryId

Returns the <code>ResourceDirectoryId</code> value.

#### Status

Returns the <code>Status</code> value.

#### Type

Returns the <code>Type</code> value.

