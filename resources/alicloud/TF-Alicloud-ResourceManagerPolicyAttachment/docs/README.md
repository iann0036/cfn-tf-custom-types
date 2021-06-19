# TF::Alicloud::ResourceManagerPolicyAttachment

Provides a Resource Manager Policy Attachment resource to attaches a policy to an object. After you attach a policy to an object, the object has the operation permissions on the current resource group or the resources under the current account. 
For information about Resource Manager Policy Attachment and how to use it, see [How to authorize and manage resource groups](https://www.alibabacloud.com/help/en/doc-detail/94490.htm).

-> **NOTE:** Available in v1.93.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ResourceManagerPolicyAttachment",
    "Properties" : {
        "<a href="#policyname" title="PolicyName">PolicyName</a>" : <i>String</i>,
        "<a href="#policytype" title="PolicyType">PolicyType</a>" : <i>String</i>,
        "<a href="#principalname" title="PrincipalName">PrincipalName</a>" : <i>String</i>,
        "<a href="#principaltype" title="PrincipalType">PrincipalType</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ResourceManagerPolicyAttachment
Properties:
    <a href="#policyname" title="PolicyName">PolicyName</a>: <i>String</i>
    <a href="#policytype" title="PolicyType">PolicyType</a>: <i>String</i>
    <a href="#principalname" title="PrincipalName">PrincipalName</a>: <i>String</i>
    <a href="#principaltype" title="PrincipalType">PrincipalType</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
</pre>

## Properties

#### PolicyName

The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyType

- (Required, ForceNew) The type of the policy. Valid values: `Custom`, `System`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrincipalName

The name of the object to which you want to attach the policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrincipalType

The type of the object to which you want to attach the policy. Valid values: `IMSUser`: RAM user, `IMSGroup`: RAM user group, `ServiceRole`: RAM role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The ID of the resource group or the ID of the Alibaba Cloud account to which the resource group belongs.

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

