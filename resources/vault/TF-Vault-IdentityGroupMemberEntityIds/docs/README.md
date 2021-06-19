# TF::Vault::IdentityGroupMemberEntityIds

Manages member entities for an Identity Group for Vault. The [Identity secrets engine](https://www.vaultproject.io/docs/secrets/identity/index.html) is the identity management solution for Vault.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vault::IdentityGroupMemberEntityIds",
    "Properties" : {
        "<a href="#exclusive" title="Exclusive">Exclusive</a>" : <i>Boolean</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#memberentityids" title="MemberEntityIds">MemberEntityIds</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vault::IdentityGroupMemberEntityIds
Properties:
    <a href="#exclusive" title="Exclusive">Exclusive</a>: <i>Boolean</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#memberentityids" title="MemberEntityIds">MemberEntityIds</a>: <i>
      - String</i>
</pre>

## Properties

#### Exclusive

Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

Group ID to assign member entities to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberEntityIds

List of member entities that belong to the group.

_Required_: No

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

#### GroupName

Returns the <code>GroupName</code> value.

#### Id

Returns the <code>Id</code> value.

