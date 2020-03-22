# Terraform::Rundeck::PrivateKey

The private key resource allows SSH private keys to be stored into Rundeck's key store.
The key store is where Rundeck keeps credentials that are needed to access the nodes on which
it runs commands.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Rundeck::PrivateKey",
    "Properties" : {
        "<a href="#keymaterial" title="KeyMaterial">KeyMaterial</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Rundeck::PrivateKey
Properties:
    <a href="#keymaterial" title="KeyMaterial">KeyMaterial</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### KeyMaterial

The private key material to store, serialized in any way that is
accepted by OpenSSH.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path within the key store where the key will be stored.

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

