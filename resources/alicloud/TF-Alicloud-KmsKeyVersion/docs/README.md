# TF::Alicloud::KmsKeyVersion

Provides a Alikms Key Version resource. For information about Alikms Key Version and how to use it, see [What is Resource Alikms Key Version](https://www.alibabacloud.com/help/doc-detail/133838.htm).

-> **NOTE:** Available in v1.85.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::KmsKeyVersion",
    "Properties" : {
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::KmsKeyVersion
Properties:
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
</pre>

## Properties

#### KeyId

The id of the master key (CMK).

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

#### CreationDate

Returns the <code>CreationDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeyVersionId

Returns the <code>KeyVersionId</code> value.

