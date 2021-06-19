# TF::ACI::DhcpRelayPolicy

Manages ACI DHCP Relay Policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::DhcpRelayPolicy",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#relationdhcprsprov" title="RelationDhcpRsProv">RelationDhcpRsProv</a>" : <i>[ String, ... ]</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::DhcpRelayPolicy
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#relationdhcprsprov" title="RelationDhcpRsProv">RelationDhcpRsProv</a>: <i>
      - String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object DHCP Relay Policy.
- `mode` - (Optional) DHCP relay policy mode. Allowed Values are "visible" and "not-visible". Default Value is "visible".
- `name_alias` - (Optional) Name alias for object DHCP Relay Policy.
- `owner` - (Optional) Owner of the target relay servers. Allowed values are "infra" and "tenant". Default value is "infra".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

DHCP relay policy mode. Allowed Values are "visible" and "not-visible". Default Value is "visible".
- `name_alias` - (Optional) Name alias for object DHCP Relay Policy.
- `owner` - (Optional) Owner of the target relay servers. Allowed values are "infra" and "tenant". Default value is "infra".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of Object DHCP Relay Policy.
- `annotation` - (Optional) Annotation for object DHCP Relay Policy.
- `mode` - (Optional) DHCP relay policy mode. Allowed Values are "visible" and "not-visible". Default Value is "visible".
- `name_alias` - (Optional) Name alias for object DHCP Relay Policy.
- `owner` - (Optional) Owner of the target relay servers. Allowed values are "infra" and "tenant". Default value is "infra".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object DHCP Relay Policy.
- `owner` - (Optional) Owner of the target relay servers. Allowed values are "infra" and "tenant". Default value is "infra".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

Owner of the target relay servers. Allowed values are "infra" and "tenant". Default value is "infra".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationDhcpRsProv

List of relation to class fvEPg. Cardinality - N_TO_M. Type - Set of String.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

Distinguished name of parent Tenant object.
- `name` - (Required) Name of Object DHCP Relay Policy.
- `annotation` - (Optional) Annotation for object DHCP Relay Policy.
- `mode` - (Optional) DHCP relay policy mode. Allowed Values are "visible" and "not-visible". Default Value is "visible".
- `name_alias` - (Optional) Name alias for object DHCP Relay Policy.
- `owner` - (Optional) Owner of the target relay servers. Allowed values are "infra" and "tenant". Default value is "infra".

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

