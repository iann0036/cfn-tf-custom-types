# TF::ACI::DhcpOptionPolicy

Manages ACI DHCP Option Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::DhcpOptionPolicy",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dhcpoptionids" title="DhcpOptionIds">DhcpOptionIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>,
        "<a href="#dhcpoption" title="DhcpOption">DhcpOption</a>" : <i>[ <a href="dhcpoptiondefinition.md">DhcpOptionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::DhcpOptionPolicy
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dhcpoptionids" title="DhcpOptionIds">DhcpOptionIds</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
    <a href="#dhcpoption" title="DhcpOption">DhcpOption</a>: <i>
      - <a href="dhcpoptiondefinition.md">DhcpOptionDefinition</a></i>
</pre>

## Properties

#### Annotation

Annotation for object DHCP Option Policy.
- `name_alias` - (Optional) Name alias for object DHCP Option Policy.
- `dhcp_option` - (Optional) to manage DHCP Option from the DHCP Option Policy resource. It has the attributes like name, annotation,data,dhcp_option_id and name_alias.
- `dhcp_option.name` - (Required) Name of Object DHCP Option.
- `dhcp_option.annotation` - (Optional) Annotation for object DHCP Option.
- `dhcp_option.data` - (Optional) DHCP Option data.
- `dhcp_option.dhcp_option_id` - (Optional) DHCP Option id (Unsigned Integer).
- `dhcp_option.name_alias` - (Optional) Name alias for object DHCP Option.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOptionIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of Object DHCP Option Policy.
- `annotation` - (Optional) Annotation for object DHCP Option Policy.
- `name_alias` - (Optional) Name alias for object DHCP Option Policy.
- `dhcp_option` - (Optional) to manage DHCP Option from the DHCP Option Policy resource. It has the attributes like name, annotation,data,dhcp_option_id and name_alias.
- `dhcp_option.name` - (Required) Name of Object DHCP Option.
- `dhcp_option.annotation` - (Optional) Annotation for object DHCP Option.
- `dhcp_option.data` - (Optional) DHCP Option data.
- `dhcp_option.dhcp_option_id` - (Optional) DHCP Option id (Unsigned Integer).
- `dhcp_option.name_alias` - (Optional) Name alias for object DHCP Option.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object DHCP Option Policy.
- `dhcp_option` - (Optional) to manage DHCP Option from the DHCP Option Policy resource. It has the attributes like name, annotation,data,dhcp_option_id and name_alias.
- `dhcp_option.name` - (Required) Name of Object DHCP Option.
- `dhcp_option.annotation` - (Optional) Annotation for object DHCP Option.
- `dhcp_option.data` - (Optional) DHCP Option data.
- `dhcp_option.dhcp_option_id` - (Optional) DHCP Option id (Unsigned Integer).
- `dhcp_option.name_alias` - (Optional) Name alias for object DHCP Option.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

Distinguished name of parent Tenant object.
- `name` - (Required) Name of Object DHCP Option Policy.
- `annotation` - (Optional) Annotation for object DHCP Option Policy.
- `name_alias` - (Optional) Name alias for object DHCP Option Policy.
- `dhcp_option` - (Optional) to manage DHCP Option from the DHCP Option Policy resource. It has the attributes like name, annotation,data,dhcp_option_id and name_alias.
- `dhcp_option.name` - (Required) Name of Object DHCP Option.
- `dhcp_option.annotation` - (Optional) Annotation for object DHCP Option.
- `dhcp_option.data` - (Optional) DHCP Option data.
- `dhcp_option.dhcp_option_id` - (Optional) DHCP Option id (Unsigned Integer).
- `dhcp_option.name_alias` - (Optional) Name alias for object DHCP Option.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOption

_Required_: No

_Type_: List of <a href="dhcpoptiondefinition.md">DhcpOptionDefinition</a>

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

