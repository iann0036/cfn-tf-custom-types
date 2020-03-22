# Terraform::Rundeck::PublicKey

The public key resource allows SSH public keys to be stored into Rundeck's key store.
The key store is where Rundeck keeps credentials that are needed to access the nodes on which
it runs commands.

This resource also allows the retrieval of an existing public key from the store, so that it
may be used in the configuration of other resources such as ``aws_key_pair``.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Rundeck::PublicKey",
    "Properties" : {
        "<a href="#keymaterial" title="KeyMaterial">KeyMaterial</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Rundeck::PublicKey
Properties:
    <a href="#keymaterial" title="KeyMaterial">KeyMaterial</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### KeyMaterial

The public key string to store, serialized in any way that is accepted
by OpenSSH. If this is not included, ``key_material`` becomes an attribute that can be used
to read the already-existing key material in the Rundeck store.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path within the key store where the key will be stored. By convention
this path name normally ends with ".pub" and otherwise has the same name as the associated
private key.

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

#### Delete

True if the key should be deleted when the resource is deleted.
Defaults to true if key_material is provided in the configuration.

#### Id

Returns the <code>Id</code> value.

#### Url

Returns the <code>Url</code> value.

