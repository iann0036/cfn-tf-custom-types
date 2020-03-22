# Terraform::GitHub::UserGpgKey

Provides a GitHub user's GPG key resource.

This resource allows you to add/remove GPG keys from your user account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::GitHub::UserGpgKey",
    "Properties" : {
        "<a href="#armoredpublickey" title="ArmoredPublicKey">ArmoredPublicKey</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::GitHub::UserGpgKey
Properties:
    <a href="#armoredpublickey" title="ArmoredPublicKey">ArmoredPublicKey</a>: <i>String</i>
</pre>

## Properties

#### ArmoredPublicKey

Your public GPG key, generated in ASCII-armored format.
See [Generating a new GPG key](https://help.github.com/articles/generating-a-new-gpg-key/) for help on creating a GPG key.

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

#### Etag

Returns the <code>Etag</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeyId

Returns the <code>KeyId</code> value.

