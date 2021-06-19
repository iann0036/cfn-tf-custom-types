# TF::ACI::L3outVpcMember

Manages ACI L3out VPC Member

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outVpcMember",
    "Properties" : {
        "<a href="#addr" title="Addr">Addr</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ipv6dad" title="Ipv6Dad">Ipv6Dad</a>" : <i>String</i>,
        "<a href="#leafportdn" title="LeafPortDn">LeafPortDn</a>" : <i>String</i>,
        "<a href="#lladdr" title="LlAddr">LlAddr</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#side" title="Side">Side</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outVpcMember
Properties:
    <a href="#addr" title="Addr">Addr</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ipv6dad" title="Ipv6Dad">Ipv6Dad</a>: <i>String</i>
    <a href="#leafportdn" title="LeafPortDn">LeafPortDn</a>: <i>String</i>
    <a href="#lladdr" title="LlAddr">LlAddr</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#side" title="Side">Side</a>: <i>String</i>
</pre>

## Properties

#### Addr

Peer IP address.
- `description` - (Optional) Description for object l3out VPC member.
- `annotation` - (Optional) Annotation for object l3out VPC member.
- `ipv6_dad` - (Optional) IPv6 DAD feature of l3out VPC member.
Allowed values: "disabled", "enabled". Default value: "enabled".
- `ll_addr` - (Optional) Override of system generated IPv6 link-local address.
- `name_alias` - (Optional) Name alias for object l3out vpc member.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

Annotation for object l3out VPC member.
- `ipv6_dad` - (Optional) IPv6 DAD feature of l3out VPC member.
Allowed values: "disabled", "enabled". Default value: "enabled".
- `ll_addr` - (Optional) Override of system generated IPv6 link-local address.
- `name_alias` - (Optional) Name alias for object l3out vpc member.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for object l3out VPC member.
- `annotation` - (Optional) Annotation for object l3out VPC member.
- `ipv6_dad` - (Optional) IPv6 DAD feature of l3out VPC member.
Allowed values: "disabled", "enabled". Default value: "enabled".
- `ll_addr` - (Optional) Override of system generated IPv6 link-local address.
- `name_alias` - (Optional) Name alias for object l3out vpc member.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Dad

IPv6 DAD feature of l3out VPC member.
Allowed values: "disabled", "enabled". Default value: "enabled".
- `ll_addr` - (Optional) Override of system generated IPv6 link-local address.
- `name_alias` - (Optional) Name alias for object l3out vpc member.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeafPortDn

Distinguished name of parent leaf port object.
- `side` - (Required) Side of Object l3out VPC member.
Allowed values: "A" and "B". Default value: "A".
- `addr` - (Optional) Peer IP address.
- `description` - (Optional) Description for object l3out VPC member.
- `annotation` - (Optional) Annotation for object l3out VPC member.
- `ipv6_dad` - (Optional) IPv6 DAD feature of l3out VPC member.
Allowed values: "disabled", "enabled". Default value: "enabled".
- `ll_addr` - (Optional) Override of system generated IPv6 link-local address.
- `name_alias` - (Optional) Name alias for object l3out vpc member.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LlAddr

Override of system generated IPv6 link-local address.
- `name_alias` - (Optional) Name alias for object l3out vpc member.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object l3out vpc member.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Side

Side of Object l3out VPC member.
Allowed values: "A" and "B". Default value: "A".
- `addr` - (Optional) Peer IP address.
- `description` - (Optional) Description for object l3out VPC member.
- `annotation` - (Optional) Annotation for object l3out VPC member.
- `ipv6_dad` - (Optional) IPv6 DAD feature of l3out VPC member.
Allowed values: "disabled", "enabled". Default value: "enabled".
- `ll_addr` - (Optional) Override of system generated IPv6 link-local address.
- `name_alias` - (Optional) Name alias for object l3out vpc member.

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

