# TF::Vault::IdentityGroup

Creates an Identity Group for Vault. The [Identity secrets engine](https://www.vaultproject.io/docs/secrets/identity/index.html) is the identity management solution for Vault.

A group can contain multiple entities as its members. A group can also have subgroups. Policies set on the group is granted to all members of the group. During request time, when the token's entity ID is being evaluated for the policies that it has access to; along with the policies on the entity itself, policies that are inherited due to group memberships are also granted.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vault::IdentityGroup",
    "Properties" : {
        "<a href="#externalmemberentityids" title="ExternalMemberEntityIds">ExternalMemberEntityIds</a>" : <i>Boolean</i>,
        "<a href="#externalpolicies" title="ExternalPolicies">ExternalPolicies</a>" : <i>Boolean</i>,
        "<a href="#memberentityids" title="MemberEntityIds">MemberEntityIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#membergroupids" title="MemberGroupIds">MemberGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vault::IdentityGroup
Properties:
    <a href="#externalmemberentityids" title="ExternalMemberEntityIds">ExternalMemberEntityIds</a>: <i>Boolean</i>
    <a href="#externalpolicies" title="ExternalPolicies">ExternalPolicies</a>: <i>Boolean</i>
    <a href="#memberentityids" title="MemberEntityIds">MemberEntityIds</a>: <i>
      - String</i>
    <a href="#membergroupids" title="MemberGroupIds">MemberGroupIds</a>: <i>
      - String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### ExternalMemberEntityIds

`false` by default. If set to `true`, this resource will ignore any Entity IDs returned from Vault or specified in the resource. You can use [`vault_identity_group_member_entity_ids`](identity_group_member_entity_ids.html) to manage Entity IDs for this group in a decoupled manner.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalPolicies

`false` by default. If set to `true`, this resource will ignore any policies returned from Vault or specified in the resource. You can use [`vault_identity_group_policies`](identity_group_policies.html) to manage policies for this group in a decoupled manner.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberEntityIds

A list of Entity IDs to be assigned as group members. Not allowed on `external` groups.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberGroupIds

A list of Group IDs to be assigned as group members. Not allowed on `external` groups.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

A Map of additional metadata to associate with the group.

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the identity group to create.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

A list of policies to apply to the group.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the group, internal or external. Defaults to `internal`.

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

#### Id

Returns the <code>Id</code> value.

