# Terraform::Vault::ApproleAuthBackendRoleSecretId

Manages an AppRole auth backend SecretID in a Vault server. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/approle.html) for more
information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::ApproleAuthBackendRoleSecretId",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#cidrlist" title="CidrList">CidrList</a>" : <i>[ String, ... ]</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>String</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>,
        "<a href="#secretid" title="SecretId">SecretId</a>" : <i>String</i>,
        "<a href="#wrappingttl" title="WrappingTtl">WrappingTtl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::ApproleAuthBackendRoleSecretId
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#cidrlist" title="CidrList">CidrList</a>: <i>
      - String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>String</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
    <a href="#secretid" title="SecretId">SecretId</a>: <i>String</i>
    <a href="#wrappingttl" title="WrappingTtl">WrappingTtl</a>: <i>String</i>
</pre>

## Properties

#### Backend

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrList

If set, specifies blocks of IP addresses which can
perform the login operation using this SecretID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

A JSON-encoded string containing metadata in
key-value pairs to be set on tokens issued with this SecretID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

The name of the role to create the SecretID for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretId

The SecretID to be created. If set, uses "Push"
mode.  Defaults to Vault auto-generating SecretIDs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WrappingTtl

If set, the SecretID response will be
[response-wrapped](https://www.vaultproject.io/docs/concepts/response-wrapping.html)
and available for the duration specified. Only a single unwrapping of the
token is allowed.

_Required_: No

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

#### Accessor

Returns the <code>Accessor</code> value.

#### WrappingAccessor

Returns the <code>WrappingAccessor</code> value.

#### WrappingToken

Returns the <code>WrappingToken</code> value.

