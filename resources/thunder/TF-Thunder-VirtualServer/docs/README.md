# TF::Thunder::VirtualServer

`thunder_virtual_server` provides details about configuring virtual server on device

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::VirtualServer",
    "Properties" : {
        "<a href="#aclid" title="AclId">AclId</a>" : <i>Double</i>,
        "<a href="#aclidshared" title="AclIdShared">AclIdShared</a>" : <i>Double</i>,
        "<a href="#aclname" title="AclName">AclName</a>" : <i>String</i>,
        "<a href="#aclnameshared" title="AclNameShared">AclNameShared</a>" : <i>String</i>,
        "<a href="#arpdisable" title="ArpDisable">ArpDisable</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disablevipadv" title="DisableVipAdv">DisableVipAdv</a>" : <i>Double</i>,
        "<a href="#enabledisableaction" title="EnableDisableAction">EnableDisableAction</a>" : <i>String</i>,
        "<a href="#ethernet" title="Ethernet">Ethernet</a>" : <i>Double</i>,
        "<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>" : <i>Double</i>,
        "<a href="#hadynamic" title="HaDynamic">HaDynamic</a>" : <i>Double</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#ipv6acl" title="Ipv6Acl">Ipv6Acl</a>" : <i>String</i>,
        "<a href="#ipv6aclshared" title="Ipv6AclShared">Ipv6AclShared</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
        "<a href="#redistributeroutemap" title="RedistributeRouteMap">RedistributeRouteMap</a>" : <i>String</i>,
        "<a href="#redistributionflagged" title="RedistributionFlagged">RedistributionFlagged</a>" : <i>Double</i>,
        "<a href="#sharedpartitionpolicytemplate" title="SharedPartitionPolicyTemplate">SharedPartitionPolicyTemplate</a>" : <i>Double</i>,
        "<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>" : <i>String</i>,
        "<a href="#templatelogging" title="TemplateLogging">TemplateLogging</a>" : <i>String</i>,
        "<a href="#templatepolicy" title="TemplatePolicy">TemplatePolicy</a>" : <i>String</i>,
        "<a href="#templatepolicyacl" title="TemplatePolicyAcl">TemplatePolicyAcl</a>" : <i>String</i>,
        "<a href="#templatepolicyaclshared" title="TemplatePolicyAclShared">TemplatePolicyAclShared</a>" : <i>String</i>,
        "<a href="#templatepolicyaddress" title="TemplatePolicyAddress">TemplatePolicyAddress</a>" : <i>String</i>,
        "<a href="#templatepolicyshared" title="TemplatePolicyShared">TemplatePolicyShared</a>" : <i>String</i>,
        "<a href="#templatescaleout" title="TemplateScaleout">TemplateScaleout</a>" : <i>String</i>,
        "<a href="#templatevirtualserver" title="TemplateVirtualServer">TemplateVirtualServer</a>" : <i>String</i>,
        "<a href="#useifip" title="UseIfIp">UseIfIp</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vrid" title="Vrid">Vrid</a>" : <i>Double</i>,
        "<a href="#migratevip" title="MigrateVip">MigrateVip</a>" : <i>[ <a href="migratevipdefinition.md">MigrateVipDefinition</a>, ... ]</i>,
        "<a href="#portlist" title="PortList">PortList</a>" : <i>[ <a href="portlistdefinition.md">PortListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::VirtualServer
Properties:
    <a href="#aclid" title="AclId">AclId</a>: <i>Double</i>
    <a href="#aclidshared" title="AclIdShared">AclIdShared</a>: <i>Double</i>
    <a href="#aclname" title="AclName">AclName</a>: <i>String</i>
    <a href="#aclnameshared" title="AclNameShared">AclNameShared</a>: <i>String</i>
    <a href="#arpdisable" title="ArpDisable">ArpDisable</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disablevipadv" title="DisableVipAdv">DisableVipAdv</a>: <i>Double</i>
    <a href="#enabledisableaction" title="EnableDisableAction">EnableDisableAction</a>: <i>String</i>
    <a href="#ethernet" title="Ethernet">Ethernet</a>: <i>Double</i>
    <a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>: <i>Double</i>
    <a href="#hadynamic" title="HaDynamic">HaDynamic</a>: <i>Double</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#ipv6acl" title="Ipv6Acl">Ipv6Acl</a>: <i>String</i>
    <a href="#ipv6aclshared" title="Ipv6AclShared">Ipv6AclShared</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
    <a href="#redistributeroutemap" title="RedistributeRouteMap">RedistributeRouteMap</a>: <i>String</i>
    <a href="#redistributionflagged" title="RedistributionFlagged">RedistributionFlagged</a>: <i>Double</i>
    <a href="#sharedpartitionpolicytemplate" title="SharedPartitionPolicyTemplate">SharedPartitionPolicyTemplate</a>: <i>Double</i>
    <a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>: <i>String</i>
    <a href="#templatelogging" title="TemplateLogging">TemplateLogging</a>: <i>String</i>
    <a href="#templatepolicy" title="TemplatePolicy">TemplatePolicy</a>: <i>String</i>
    <a href="#templatepolicyacl" title="TemplatePolicyAcl">TemplatePolicyAcl</a>: <i>String</i>
    <a href="#templatepolicyaclshared" title="TemplatePolicyAclShared">TemplatePolicyAclShared</a>: <i>String</i>
    <a href="#templatepolicyaddress" title="TemplatePolicyAddress">TemplatePolicyAddress</a>: <i>String</i>
    <a href="#templatepolicyshared" title="TemplatePolicyShared">TemplatePolicyShared</a>: <i>String</i>
    <a href="#templatescaleout" title="TemplateScaleout">TemplateScaleout</a>: <i>String</i>
    <a href="#templatevirtualserver" title="TemplateVirtualServer">TemplateVirtualServer</a>: <i>String</i>
    <a href="#useifip" title="UseIfIp">UseIfIp</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vrid" title="Vrid">Vrid</a>: <i>Double</i>
    <a href="#migratevip" title="MigrateVip">MigrateVip</a>: <i>
      - <a href="migratevipdefinition.md">MigrateVipDefinition</a></i>
    <a href="#portlist" title="PortList">PortList</a>: <i>
      - <a href="portlistdefinition.md">PortListDefinition</a></i>
</pre>

## Properties

#### AclId

ACL id VPORT.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclIdShared

acl id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclName

Apply an access list name (Named Access List).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclNameShared

Access List name (IPv4 Access List Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArpDisable

Disable Respond to Virtual Server ARP request.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Create a description for VIP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableVipAdv

Disable virtual server GARP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDisableAction

‘enable’: Enable Virtual Server (default); ‘disable’: Disable Virtual Server; ‘disable-when-all-ports-down’: Disable Virtual Server when all member ports are down; ‘disable-when-any-port-down’: Disable Virtual Server when any member port is down;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ethernet

Ethernet interface.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStats

Enable extended statistics on virtual port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaDynamic

Dynamic failover based on vip status.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

IP Address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Acl

ipv6 acl name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6AclShared

ipv6 acl name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

SLB Virtual Service Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

IP subnet mask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedistributeRouteMap

Route map reference (Name of route-map).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedistributionFlagged

Flag VIP for special redistribution handling.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPolicyTemplate

Reference a policy template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsDataAction

‘stats-data-enable’: Enable statistical data collection for virtual port; ‘stats-data-disable’: Disable statistical data collection for virtual port;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateLogging

NAT Logging template (NAT Logging template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicy

Policy Template (Policy template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicyAcl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicyAclShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicyAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicyShared

Policy Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateScaleout

Scaleout template (Scaleout template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVirtualServer

Virtual server template (Virtual server template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseIfIp

Use Interface IP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrid

Join a vrrp group (Specify ha VRRP-A vrid).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MigrateVip

_Required_: No

_Type_: List of <a href="migratevipdefinition.md">MigrateVipDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortList

_Required_: No

_Type_: List of <a href="portlistdefinition.md">PortListDefinition</a>

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

