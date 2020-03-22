# Terraform::Vault::Namespace

Provides a resource to manage [Namespaces](https://www.vaultproject.io/docs/enterprise/namespaces/index.html).

**Note** this feature is available only with Vault Enterprise.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::Namespace",
    "Properties" : {
        "<a href="#path" title="Path">Path</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::Namespace
Properties:
    <a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### Path

The path of the namespace. Must not have a trailing `/`.

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

#### NamespaceId

Returns the <code>NamespaceId</code> value.

