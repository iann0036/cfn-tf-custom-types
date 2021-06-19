# TF::ACI::BdDhcpLabel

Manages ACI BD DHCP Label

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::BdDhcpLabel",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#bridgedomaindn" title="BridgeDomainDn">BridgeDomainDn</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#relationdhcprsdhcpoptionpol" title="RelationDhcpRsDhcpOptionPol">RelationDhcpRsDhcpOptionPol</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::BdDhcpLabel
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#bridgedomaindn" title="BridgeDomainDn">BridgeDomainDn</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#relationdhcprsdhcpoptionpol" title="RelationDhcpRsDhcpOptionPol">RelationDhcpRsDhcpOptionPol</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object BD DHCP Label.
- `name_alias` - (Optional) Name alias for object BD DHCP Label.
- `owner` - (Optional) Owner of the target relay servers.
Allowed values: "infra", "tenant". Default value: "infra".
- `tag` - (Optional) Label color.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BridgeDomainDn

Distinguished name of parent Bridge Domain object.
- `name` - (Required) The Bridge Domain DHCP label name. This name can be up to 64 alphanumeric characters.
- `annotation` - (Optional) Annotation for object BD DHCP Label.
- `name_alias` - (Optional) Name alias for object BD DHCP Label.
- `owner` - (Optional) Owner of the target relay servers.
Allowed values: "infra", "tenant". Default value: "infra".
- `tag` - (Optional) Label color.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Bridge Domain DHCP label name. This name can be up to 64 alphanumeric characters.
- `annotation` - (Optional) Annotation for object BD DHCP Label.
- `name_alias` - (Optional) Name alias for object BD DHCP Label.
- `owner` - (Optional) Owner of the target relay servers.
Allowed values: "infra", "tenant". Default value: "infra".
- `tag` - (Optional) Label color.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object BD DHCP Label.
- `owner` - (Optional) Owner of the target relay servers.
Allowed values: "infra", "tenant". Default value: "infra".
- `tag` - (Optional) Label color.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

Owner of the target relay servers.
Allowed values: "infra", "tenant". Default value: "infra".
- `tag` - (Optional) Label color.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationDhcpRsDhcpOptionPol

Relation to class dhcpOptionPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

Label color.

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

