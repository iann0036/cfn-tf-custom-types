# Terraform::Vault::IdentityEntityPolicies

Manages policies for an Identity Entity for Vault. The [Identity secrets engine](https://www.vaultproject.io/docs/secrets/identity/index.html) is the identity management solution for Vault.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::IdentityEntityPolicies",
    "Properties" : {
        "<a href="#entityid" title="EntityId">EntityId</a>" : <i>String</i>,
        "<a href="#exclusive" title="Exclusive">Exclusive</a>" : <i>Boolean</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::IdentityEntityPolicies
Properties:
    <a href="#entityid" title="EntityId">EntityId</a>: <i>String</i>
    <a href="#exclusive" title="Exclusive">Exclusive</a>: <i>Boolean</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
</pre>

## Properties

#### EntityId

Entity ID to assign policies to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusive

Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

List of policies to assign to the entity.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### EntityName

Returns the <code>EntityName</code> value.

#### Id

Returns the <code>Id</code> value.

