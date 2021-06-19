# TF::Alicloud::ResourceManagerPolicyVersion

Provides a Resource Manager Policy Version resource. 
For information about Resource Manager Policy Version and how to use it, see [What is Resource Manager Policy Version](https://www.alibabacloud.com/help/en/doc-detail/116817.htm).

-> **NOTE:** Available in v1.84.0+.

-> **NOTE:** It is not recommended to use this resource management policy version, it is recommended to directly use the policy resource to manage your policy. Please refer to the link for usage [resource_manager_policy](https://www.terraform.io/docs/providers/alicloud/r/resource_manager_policy.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ResourceManagerPolicyVersion",
    "Properties" : {
        "<a href="#isdefaultversion" title="IsDefaultVersion">IsDefaultVersion</a>" : <i>Boolean</i>,
        "<a href="#policydocument" title="PolicyDocument">PolicyDocument</a>" : <i>String</i>,
        "<a href="#policyname" title="PolicyName">PolicyName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ResourceManagerPolicyVersion
Properties:
    <a href="#isdefaultversion" title="IsDefaultVersion">IsDefaultVersion</a>: <i>Boolean</i>
    <a href="#policydocument" title="PolicyDocument">PolicyDocument</a>: <i>String</i>
    <a href="#policyname" title="PolicyName">PolicyName</a>: <i>String</i>
</pre>

## Properties

#### IsDefaultVersion

Specifies whether to set the policy version as the default version. Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyDocument

The content of the policy. The content must be 1 to 2,048 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyName

The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).

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

#### CreateDate

Returns the <code>CreateDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### VersionId

Returns the <code>VersionId</code> value.

