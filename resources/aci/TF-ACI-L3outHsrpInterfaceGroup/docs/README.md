# TF::ACI::L3outHsrpInterfaceGroup

Manages ACI L3out HSRP Interface Group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outHsrpInterfaceGroup",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#configissues" title="ConfigIssues">ConfigIssues</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#groupaf" title="GroupAf">GroupAf</a>" : <i>String</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#ipobtainmode" title="IpObtainMode">IpObtainMode</a>" : <i>String</i>,
        "<a href="#l3outhsrpinterfaceprofiledn" title="L3outHsrpInterfaceProfileDn">L3outHsrpInterfaceProfileDn</a>" : <i>String</i>,
        "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationhsrprsgrouppol" title="RelationHsrpRsGroupPol">RelationHsrpRsGroupPol</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outHsrpInterfaceGroup
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#configissues" title="ConfigIssues">ConfigIssues</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#groupaf" title="GroupAf">GroupAf</a>: <i>String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#ipobtainmode" title="IpObtainMode">IpObtainMode</a>: <i>String</i>
    <a href="#l3outhsrpinterfaceprofiledn" title="L3outHsrpInterfaceProfileDn">L3outHsrpInterfaceProfileDn</a>: <i>String</i>
    <a href="#mac" title="Mac">Mac</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationhsrprsgrouppol" title="RelationHsrpRsGroupPol">RelationHsrpRsGroupPol</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for L3out HSRP interface group object.
- `description` - (Optional) Description for L3out HSRP interface group object.
- `config_issues` - (Optional) Configuration issues for L3out HSRP interface group object. Allowed values are "GroupMac-Conflicts-Other-Group", "GroupName-Conflicts-Other-Group", "GroupVIP-Conflicts-Other-Group", "Multiple-Version-On-Interface", "Secondary-vip-conflicts-if-ip", "Secondary-vip-subnet-mismatch", "group-vip-conflicts-if-ip", "group-vip-subnet-mismatch" and "none". Default value is "none".
- `group_af` - (Optional) Group type for L3out HSRP interface group object. Allowed values are "ipv4" and "ipv6". Default value is "ipv4".
- `group_id` - (Optional) Group id for L3out HSRP interface group object.
- `group_name` - (Optional) Group name for L3out HSRP interface group object.
- `ip` - (Optional) IP address for L3out HSRP interface group object.
- `ip_obtain_mode` - (Optional) IP obtain mode for L3out HSRP interface group object. Allowed values are "admin", "auto" and "learn". Default value is "admin".
- `mac` - (Optional) MAC address for L3out HSRP interface group object.
- `name_alias` - (Optional) Name alias for L3out HSRP interface group object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigIssues

Configuration issues for L3out HSRP interface group object. Allowed values are "GroupMac-Conflicts-Other-Group", "GroupName-Conflicts-Other-Group", "GroupVIP-Conflicts-Other-Group", "Multiple-Version-On-Interface", "Secondary-vip-conflicts-if-ip", "Secondary-vip-subnet-mismatch", "group-vip-conflicts-if-ip", "group-vip-subnet-mismatch" and "none". Default value is "none".
- `group_af` - (Optional) Group type for L3out HSRP interface group object. Allowed values are "ipv4" and "ipv6". Default value is "ipv4".
- `group_id` - (Optional) Group id for L3out HSRP interface group object.
- `group_name` - (Optional) Group name for L3out HSRP interface group object.
- `ip` - (Optional) IP address for L3out HSRP interface group object.
- `ip_obtain_mode` - (Optional) IP obtain mode for L3out HSRP interface group object. Allowed values are "admin", "auto" and "learn". Default value is "admin".
- `mac` - (Optional) MAC address for L3out HSRP interface group object.
- `name_alias` - (Optional) Name alias for L3out HSRP interface group object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for L3out HSRP interface group object.
- `config_issues` - (Optional) Configuration issues for L3out HSRP interface group object. Allowed values are "GroupMac-Conflicts-Other-Group", "GroupName-Conflicts-Other-Group", "GroupVIP-Conflicts-Other-Group", "Multiple-Version-On-Interface", "Secondary-vip-conflicts-if-ip", "Secondary-vip-subnet-mismatch", "group-vip-conflicts-if-ip", "group-vip-subnet-mismatch" and "none". Default value is "none".
- `group_af` - (Optional) Group type for L3out HSRP interface group object. Allowed values are "ipv4" and "ipv6". Default value is "ipv4".
- `group_id` - (Optional) Group id for L3out HSRP interface group object.
- `group_name` - (Optional) Group name for L3out HSRP interface group object.
- `ip` - (Optional) IP address for L3out HSRP interface group object.
- `ip_obtain_mode` - (Optional) IP obtain mode for L3out HSRP interface group object. Allowed values are "admin", "auto" and "learn". Default value is "admin".
- `mac` - (Optional) MAC address for L3out HSRP interface group object.
- `name_alias` - (Optional) Name alias for L3out HSRP interface group object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupAf

Group type for L3out HSRP interface group object. Allowed values are "ipv4" and "ipv6". Default value is "ipv4".
- `group_id` - (Optional) Group id for L3out HSRP interface group object.
- `group_name` - (Optional) Group name for L3out HSRP interface group object.
- `ip` - (Optional) IP address for L3out HSRP interface group object.
- `ip_obtain_mode` - (Optional) IP obtain mode for L3out HSRP interface group object. Allowed values are "admin", "auto" and "learn". Default value is "admin".
- `mac` - (Optional) MAC address for L3out HSRP interface group object.
- `name_alias` - (Optional) Name alias for L3out HSRP interface group object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

Group id for L3out HSRP interface group object.
- `group_name` - (Optional) Group name for L3out HSRP interface group object.
- `ip` - (Optional) IP address for L3out HSRP interface group object.
- `ip_obtain_mode` - (Optional) IP obtain mode for L3out HSRP interface group object. Allowed values are "admin", "auto" and "learn". Default value is "admin".
- `mac` - (Optional) MAC address for L3out HSRP interface group object.
- `name_alias` - (Optional) Name alias for L3out HSRP interface group object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupName

Group name for L3out HSRP interface group object.
- `ip` - (Optional) IP address for L3out HSRP interface group object.
- `ip_obtain_mode` - (Optional) IP obtain mode for L3out HSRP interface group object. Allowed values are "admin", "auto" and "learn". Default value is "admin".
- `mac` - (Optional) MAC address for L3out HSRP interface group object.
- `name_alias` - (Optional) Name alias for L3out HSRP interface group object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IP address for L3out HSRP interface group object.
- `ip_obtain_mode` - (Optional) IP obtain mode for L3out HSRP interface group object. Allowed values are "admin", "auto" and "learn". Default value is "admin".
- `mac` - (Optional) MAC address for L3out HSRP interface group object.
- `name_alias` - (Optional) Name alias for L3out HSRP interface group object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpObtainMode

IP obtain mode for L3out HSRP interface group object. Allowed values are "admin", "auto" and "learn". Default value is "admin".
- `mac` - (Optional) MAC address for L3out HSRP interface group object.
- `name_alias` - (Optional) Name alias for L3out HSRP interface group object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3outHsrpInterfaceProfileDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

MAC address for L3out HSRP interface group object.
- `name_alias` - (Optional) Name alias for L3out HSRP interface group object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of L3out HSRP interface group object.
- `annotation` - (Optional) Annotation for L3out HSRP interface group object.
- `description` - (Optional) Description for L3out HSRP interface group object.
- `config_issues` - (Optional) Configuration issues for L3out HSRP interface group object. Allowed values are "GroupMac-Conflicts-Other-Group", "GroupName-Conflicts-Other-Group", "GroupVIP-Conflicts-Other-Group", "Multiple-Version-On-Interface", "Secondary-vip-conflicts-if-ip", "Secondary-vip-subnet-mismatch", "group-vip-conflicts-if-ip", "group-vip-subnet-mismatch" and "none". Default value is "none".
- `group_af` - (Optional) Group type for L3out HSRP interface group object. Allowed values are "ipv4" and "ipv6". Default value is "ipv4".
- `group_id` - (Optional) Group id for L3out HSRP interface group object.
- `group_name` - (Optional) Group name for L3out HSRP interface group object.
- `ip` - (Optional) IP address for L3out HSRP interface group object.
- `ip_obtain_mode` - (Optional) IP obtain mode for L3out HSRP interface group object. Allowed values are "admin", "auto" and "learn". Default value is "admin".
- `mac` - (Optional) MAC address for L3out HSRP interface group object.
- `name_alias` - (Optional) Name alias for L3out HSRP interface group object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for L3out HSRP interface group object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationHsrpRsGroupPol

Relation to class hsrpGroupPol. Cardinality - N_TO_ONE. Type - String.

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

