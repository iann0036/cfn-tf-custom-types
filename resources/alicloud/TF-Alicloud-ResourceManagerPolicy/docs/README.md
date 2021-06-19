# TF::Alicloud::ResourceManagerPolicy

Provides a Resource Manager Policy resource.  
For information about Resource Manager Policy and how to use it, see [What is Resource Manager Policy](https://www.alibabacloud.com/help/en/doc-detail/93732.htm).

-> **NOTE:** Available in v1.83.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ResourceManagerPolicy",
    "Properties" : {
        "<a href="#defaultversion" title="DefaultVersion">DefaultVersion</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#policydocument" title="PolicyDocument">PolicyDocument</a>" : <i>String</i>,
        "<a href="#policyname" title="PolicyName">PolicyName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ResourceManagerPolicy
Properties:
    <a href="#defaultversion" title="DefaultVersion">DefaultVersion</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#policydocument" title="PolicyDocument">PolicyDocument</a>: <i>String</i>
    <a href="#policyname" title="PolicyName">PolicyName</a>: <i>String</i>
</pre>

## Properties

#### DefaultVersion

The version of the policy. Default to v1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the policy. The description must be 1 to 1,024 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyDocument

The content of the policy. The content must be 1 to 2,048 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyName

The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).

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

#### PolicyType

Returns the <code>PolicyType</code> value.

