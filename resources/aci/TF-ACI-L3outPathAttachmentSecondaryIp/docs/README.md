# TF::ACI::L3outPathAttachmentSecondaryIp

Manages ACI L3-out Path Attachment Secondary IP

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outPathAttachmentSecondaryIp",
    "Properties" : {
        "<a href="#addr" title="Addr">Addr</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ipv6dad" title="Ipv6Dad">Ipv6Dad</a>" : <i>String</i>,
        "<a href="#l3outpathattachmentdn" title="L3outPathAttachmentDn">L3outPathAttachmentDn</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outPathAttachmentSecondaryIp
Properties:
    <a href="#addr" title="Addr">Addr</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ipv6dad" title="Ipv6Dad">Ipv6Dad</a>: <i>String</i>
    <a href="#l3outpathattachmentdn" title="L3outPathAttachmentDn">L3outPathAttachmentDn</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
</pre>

## Properties

#### Addr

The peer IP address.
- `annotation` - (Optional) Annotation for object L3-out path attachment secondary IP.
- `ipv6_dad` - (Optional) IPv6-DAD for object L3-out path attachment secondary IP.
Allowed values: "disabled", "enabled". Default value: "disabled".
- `name_alias` - (Optional) Name alias for object L3-out path attachment secondary IP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

Annotation for object L3-out path attachment secondary IP.
- `ipv6_dad` - (Optional) IPv6-DAD for object L3-out path attachment secondary IP.
Allowed values: "disabled", "enabled". Default value: "disabled".
- `name_alias` - (Optional) Name alias for object L3-out path attachment secondary IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Dad

IPv6-DAD for object L3-out path attachment secondary IP.
Allowed values: "disabled", "enabled". Default value: "disabled".
- `name_alias` - (Optional) Name alias for object L3-out path attachment secondary IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3outPathAttachmentDn

Distinguished name of parent L3-out path attachment object.
- `addr` - (Required) The peer IP address.
- `annotation` - (Optional) Annotation for object L3-out path attachment secondary IP.
- `ipv6_dad` - (Optional) IPv6-DAD for object L3-out path attachment secondary IP.
Allowed values: "disabled", "enabled". Default value: "disabled".
- `name_alias` - (Optional) Name alias for object L3-out path attachment secondary IP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object L3-out path attachment secondary IP.

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

