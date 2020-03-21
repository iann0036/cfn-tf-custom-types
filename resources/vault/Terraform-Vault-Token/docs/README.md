# Terraform::Vault::Token

Provides a resource to generate a vault token with its options. The token renewing is supported through optional
arguments.

The token used by Terraform will require update access to the `auth/token/lookup-accessor`
path to create tokens and the `auth/token/revoke-accessor` path in Vault to
destroy a token.

```hcl
path "auth/token/lookup-accessor" {
  capabilities = ["update"]
}

path "auth/token/revoke-accessor" {
  capabilities = ["update"]
}
```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::Token",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#explicitmaxttl" title="ExplicitMaxTtl">ExplicitMaxTtl</a>" : <i>String</i>,
        "<a href="#nodefaultpolicy" title="NoDefaultPolicy">NoDefaultPolicy</a>" : <i>Boolean</i>,
        "<a href="#noparent" title="NoParent">NoParent</a>" : <i>Boolean</i>,
        "<a href="#numuses" title="NumUses">NumUses</a>" : <i>Double</i>,
        "<a href="#period" title="Period">Period</a>" : <i>String</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#renewincrement" title="RenewIncrement">RenewIncrement</a>" : <i>Double</i>,
        "<a href="#renewminlease" title="RenewMinLease">RenewMinLease</a>" : <i>Double</i>,
        "<a href="#renewable" title="Renewable">Renewable</a>" : <i>Boolean</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>String</i>,
        "<a href="#wrappingttl" title="WrappingTtl">WrappingTtl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::Token
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#explicitmaxttl" title="ExplicitMaxTtl">ExplicitMaxTtl</a>: <i>String</i>
    <a href="#nodefaultpolicy" title="NoDefaultPolicy">NoDefaultPolicy</a>: <i>Boolean</i>
    <a href="#noparent" title="NoParent">NoParent</a>: <i>Boolean</i>
    <a href="#numuses" title="NumUses">NumUses</a>: <i>Double</i>
    <a href="#period" title="Period">Period</a>: <i>String</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#renewincrement" title="RenewIncrement">RenewIncrement</a>: <i>Double</i>
    <a href="#renewminlease" title="RenewMinLease">RenewMinLease</a>: <i>Double</i>
    <a href="#renewable" title="Renewable">Renewable</a>: <i>Boolean</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>String</i>
    <a href="#wrappingttl" title="WrappingTtl">WrappingTtl</a>: <i>String</i>
</pre>

## Properties

#### DisplayName

String containing the token display name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExplicitMaxTtl

The explicit max TTL of this token.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoDefaultPolicy

Flag to not attach the default policy to this token.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoParent

Flag to create a token without parent.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumUses

The number of allowed uses of this token.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The period of this token.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

List of policies to attach to this token.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenewIncrement

The renew increment.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenewMinLease

The minimal lease to renew this token.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Renewable

Flag to allow to renew this token.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

The token role name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

The TTL period of this token.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WrappingTtl

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

#### ClientToken

Returns the <code>ClientToken</code> value.

#### LeaseDuration

Returns the <code>LeaseDuration</code> value.

#### LeaseStarted

Returns the <code>LeaseStarted</code> value.

#### WrappedToken

Returns the <code>WrappedToken</code> value.

#### WrappingAccessor

Returns the <code>WrappingAccessor</code> value.

