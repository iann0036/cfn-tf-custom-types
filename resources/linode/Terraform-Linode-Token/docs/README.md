# Terraform::Linode::Token

Provides a Linode Token resource.  This can be used to create, modify, and delete Linode API Personal Access Tokens.  Personal Access Tokens proxy user credentials for Linode API access.  This is necessary for tools, such as Terraform, to interact with Linode services on a user's behalf.

It is common for Terraform itself to be configured with broadly scoped Personal Access Tokens.  Provisioning scripts or tools configured within a Linode Instance should follow the principle of least privilege to afford only the required roles for tools to perform their necessary tasks.  The `linode_token` resource allows for the management of Personal Access Tokens with scopes mirroring or narrowing the scope of the parent token.

For more information, see the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/getTokens).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Linode::Token",
    "Properties" : {
        "<a href="#expiry" title="Expiry">Expiry</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#scopes" title="Scopes">Scopes</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Linode::Token
Properties:
    <a href="#expiry" title="Expiry">Expiry</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#scopes" title="Scopes">Scopes</a>: <i>String</i>
</pre>

## Properties

#### Expiry

When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with 'null' as their expiry and will never expire unless revoked.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

A label for the Token.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scopes

The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to *. Tokens with more restrictive scopes are generally more secure.

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

#### Created

Returns the <code>Created</code> value.

#### Id

Returns the <code>Id</code> value.

#### Token

Returns the <code>Token</code> value.

