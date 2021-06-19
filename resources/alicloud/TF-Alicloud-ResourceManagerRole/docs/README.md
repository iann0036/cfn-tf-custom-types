# TF::Alicloud::ResourceManagerRole

Provides a Resource Manager role resource. Members are resource containers in the resource directory, which can physically isolate resources to form an independent resource grouping unit. You can create members in the resource folder to manage them in a unified manner.
For information about Resource Manager role and how to use it, see [What is Resource Manager role](https://www.alibabacloud.com/help/en/doc-detail/111231.htm).

-> **NOTE:** Available in v1.82.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ResourceManagerRole",
    "Properties" : {
        "<a href="#assumerolepolicydocument" title="AssumeRolePolicyDocument">AssumeRolePolicyDocument</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#maxsessionduration" title="MaxSessionDuration">MaxSessionDuration</a>" : <i>Double</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ResourceManagerRole
Properties:
    <a href="#assumerolepolicydocument" title="AssumeRolePolicyDocument">AssumeRolePolicyDocument</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#maxsessionduration" title="MaxSessionDuration">MaxSessionDuration</a>: <i>Double</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
</pre>

## Properties

#### AssumeRolePolicyDocument

The content of the permissions strategy that plays a role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the Resource Manager role.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSessionDuration

Role maximum session time. Valid values: [3600-43200]. Default to `3600`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

Role Name. The length is 1 ~ 64 characters, which can include English letters, numbers, dots "." and dashes "-".

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

#### Arn

Returns the <code>Arn</code> value.

#### CreateDate

Returns the <code>CreateDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### RoleId

Returns the <code>RoleId</code> value.

#### UpdateDate

Returns the <code>UpdateDate</code> value.

