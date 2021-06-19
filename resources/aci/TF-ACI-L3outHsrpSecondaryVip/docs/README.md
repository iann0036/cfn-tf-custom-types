# TF::ACI::L3outHsrpSecondaryVip

Manages ACI L3out HSRP Secondary VIP

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outHsrpSecondaryVip",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#configissues" title="ConfigIssues">ConfigIssues</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#l3outhsrpinterfacegroupdn" title="L3outHsrpInterfaceGroupDn">L3outHsrpInterfaceGroupDn</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outHsrpSecondaryVip
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#configissues" title="ConfigIssues">ConfigIssues</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#l3outhsrpinterfacegroupdn" title="L3outHsrpInterfaceGroupDn">L3outHsrpInterfaceGroupDn</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object L3out HSRP Secondary VIP.
- `description` - (Optional) Description for object L3out HSRP Secondary VIP.
- `config_issues` - (Optional) Configuration Issues.
Allowed values: "GroupMac-Conflicts-Other-Group", "GroupName-Conflicts-Other-Group", "GroupVIP-Conflicts-Other-Group", "Multiple-Version-On-Interface", "Secondary-vip-conflicts-if-ip", "Secondary-vip-subnet-mismatch", "group-vip-conflicts-if-ip", "group-vip-subnet-mismatch", "none". Default value: "none".
- `ip` - (Optional) IP address.
- `name_alias` - (Optional) Name alias for object L3out HSRP Secondary VIP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigIssues

Configuration Issues.
Allowed values: "GroupMac-Conflicts-Other-Group", "GroupName-Conflicts-Other-Group", "GroupVIP-Conflicts-Other-Group", "Multiple-Version-On-Interface", "Secondary-vip-conflicts-if-ip", "Secondary-vip-subnet-mismatch", "group-vip-conflicts-if-ip", "group-vip-subnet-mismatch", "none". Default value: "none".
- `ip` - (Optional) IP address.
- `name_alias` - (Optional) Name alias for object L3out HSRP Secondary VIP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for object L3out HSRP Secondary VIP.
- `config_issues` - (Optional) Configuration Issues.
Allowed values: "GroupMac-Conflicts-Other-Group", "GroupName-Conflicts-Other-Group", "GroupVIP-Conflicts-Other-Group", "Multiple-Version-On-Interface", "Secondary-vip-conflicts-if-ip", "Secondary-vip-subnet-mismatch", "group-vip-conflicts-if-ip", "group-vip-subnet-mismatch", "none". Default value: "none".
- `ip` - (Optional) IP address.
- `name_alias` - (Optional) Name alias for object L3out HSRP Secondary VIP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IP address.
- `name_alias` - (Optional) Name alias for object L3out HSRP Secondary VIP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3outHsrpInterfaceGroupDn

Distinguished name of parent hsrp group profile object.
- `ip` - (Required) IP of Object L3out HSRP Secondary VIP.
- `annotation` - (Optional) Annotation for object L3out HSRP Secondary VIP.
- `description` - (Optional) Description for object L3out HSRP Secondary VIP.
- `config_issues` - (Optional) Configuration Issues.
Allowed values: "GroupMac-Conflicts-Other-Group", "GroupName-Conflicts-Other-Group", "GroupVIP-Conflicts-Other-Group", "Multiple-Version-On-Interface", "Secondary-vip-conflicts-if-ip", "Secondary-vip-subnet-mismatch", "group-vip-conflicts-if-ip", "group-vip-subnet-mismatch", "none". Default value: "none".
- `ip` - (Optional) IP address.
- `name_alias` - (Optional) Name alias for object L3out HSRP Secondary VIP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object L3out HSRP Secondary VIP.

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

