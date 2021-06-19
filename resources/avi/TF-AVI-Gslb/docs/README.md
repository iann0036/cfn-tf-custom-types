# TF::AVI::Gslb

The Gslb resource allows the creation and management of Avi Gslb

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Gslb",
    "Properties" : {
        "<a href="#asyncinterval" title="AsyncInterval">AsyncInterval</a>" : <i>Double</i>,
        "<a href="#clearonmaxretries" title="ClearOnMaxRetries">ClearOnMaxRetries</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enableconfigbymembers" title="EnableConfigByMembers">EnableConfigByMembers</a>" : <i>Boolean</i>,
        "<a href="#errorresyncinterval" title="ErrorResyncInterval">ErrorResyncInterval</a>" : <i>Double</i>,
        "<a href="#isfederated" title="IsFederated">IsFederated</a>" : <i>Boolean</i>,
        "<a href="#leaderclusteruuid" title="LeaderClusterUuid">LeaderClusterUuid</a>" : <i>String</i>,
        "<a href="#maintenancemode" title="MaintenanceMode">MaintenanceMode</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sendinterval" title="SendInterval">SendInterval</a>" : <i>Double</i>,
        "<a href="#sendintervalpriortomaintenancemode" title="SendIntervalPriorToMaintenanceMode">SendIntervalPriorToMaintenanceMode</a>" : <i>Double</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#tenantscoped" title="TenantScoped">TenantScoped</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#viewid" title="ViewId">ViewId</a>" : <i>Double</i>,
        "<a href="#clientipaddrgroup" title="ClientIpAddrGroup">ClientIpAddrGroup</a>" : <i>[ <a href="clientipaddrgroupdefinition.md">ClientIpAddrGroupDefinition</a>, ... ]</i>,
        "<a href="#dnsconfigs" title="DnsConfigs">DnsConfigs</a>" : <i>[ <a href="dnsconfigsdefinition.md">DnsConfigsDefinition</a>, ... ]</i>,
        "<a href="#replicationpolicy" title="ReplicationPolicy">ReplicationPolicy</a>" : <i>[ <a href="replicationpolicydefinition.md">ReplicationPolicyDefinition</a>, ... ]</i>,
        "<a href="#sites" title="Sites">Sites</a>" : <i>[ <a href="sitesdefinition.md">SitesDefinition</a>, ... ]</i>,
        "<a href="#thirdpartysites" title="ThirdPartySites">ThirdPartySites</a>" : <i>[ <a href="thirdpartysitesdefinition.md">ThirdPartySitesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Gslb
Properties:
    <a href="#asyncinterval" title="AsyncInterval">AsyncInterval</a>: <i>Double</i>
    <a href="#clearonmaxretries" title="ClearOnMaxRetries">ClearOnMaxRetries</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enableconfigbymembers" title="EnableConfigByMembers">EnableConfigByMembers</a>: <i>Boolean</i>
    <a href="#errorresyncinterval" title="ErrorResyncInterval">ErrorResyncInterval</a>: <i>Double</i>
    <a href="#isfederated" title="IsFederated">IsFederated</a>: <i>Boolean</i>
    <a href="#leaderclusteruuid" title="LeaderClusterUuid">LeaderClusterUuid</a>: <i>String</i>
    <a href="#maintenancemode" title="MaintenanceMode">MaintenanceMode</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sendinterval" title="SendInterval">SendInterval</a>: <i>Double</i>
    <a href="#sendintervalpriortomaintenancemode" title="SendIntervalPriorToMaintenanceMode">SendIntervalPriorToMaintenanceMode</a>: <i>Double</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#tenantscoped" title="TenantScoped">TenantScoped</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#viewid" title="ViewId">ViewId</a>: <i>Double</i>
    <a href="#clientipaddrgroup" title="ClientIpAddrGroup">ClientIpAddrGroup</a>: <i>
      - <a href="clientipaddrgroupdefinition.md">ClientIpAddrGroupDefinition</a></i>
    <a href="#dnsconfigs" title="DnsConfigs">DnsConfigs</a>: <i>
      - <a href="dnsconfigsdefinition.md">DnsConfigsDefinition</a></i>
    <a href="#replicationpolicy" title="ReplicationPolicy">ReplicationPolicy</a>: <i>
      - <a href="replicationpolicydefinition.md">ReplicationPolicyDefinition</a></i>
    <a href="#sites" title="Sites">Sites</a>: <i>
      - <a href="sitesdefinition.md">SitesDefinition</a></i>
    <a href="#thirdpartysites" title="ThirdPartySites">ThirdPartySites</a>: <i>
      - <a href="thirdpartysitesdefinition.md">ThirdPartySitesDefinition</a></i>
</pre>

## Properties

#### AsyncInterval

Frequency with which messages are propagated to vs mgr. Value of 0 disables async behavior and rpc are sent inline. Allowed values are 0-5. Field introduced in 18.2.3. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClearOnMaxRetries

Max retries after which the remote site is treated as a fresh start. In fresh start all the configs are downloaded. Allowed values are 1-1024.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableConfigByMembers

Allows enable/disable of gslbservice pool groups and pool members from the gslb follower members. Field introduced in 20.1.5.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorResyncInterval

Frequency with which errored messages are resynced to follower sites. Value of 0 disables resync behavior. Allowed values are 60-3600. Special values are 0 - 'disable'. Field introduced in 18.2.3. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFederated

This field indicates that this object is replicated across gslb federation. Field introduced in 17.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeaderClusterUuid

Mark this site as leader of gslb configuration. This site is the one among the avi sites.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceMode

This field disables the configuration operations on the leader for all federated objects. Cud operations on gslb, gslbservice, gslbgeodbprofile and other federated objects will be rejected. The rest-api disabling helps in upgrade scenarios where we don't want configuration sync operations to the gslb member when the member is being upgraded. This configuration programmatically blocks the leader from accepting new gslb configuration when member sites are undergoing upgrade. Field introduced in 17.2.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name for the gslb object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendInterval

Frequency with which group members communicate. Allowed values are 1-3600. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendIntervalPriorToMaintenanceMode

The user can specify a send-interval while entering maintenance mode. The validity of this 'maintenance send-interval' is only during maintenance mode. When the user leaves maintenance mode, the original send-interval is reinstated. This internal variable is used to store the original send-interval. Field introduced in 18.2.3. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantScoped

This field indicates tenant visibility for gs pool member selection across the gslb federated objects. Field introduced in 18.2.12,20.1.4.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewId

The view-id is used in change-leader mode to differentiate partitioned groups while they have the same gslb namespace. Each partitioned group will be able to operate independently by using the view-id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIpAddrGroup

_Required_: No

_Type_: List of <a href="clientipaddrgroupdefinition.md">ClientIpAddrGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfigs

_Required_: No

_Type_: List of <a href="dnsconfigsdefinition.md">DnsConfigsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationPolicy

_Required_: No

_Type_: List of <a href="replicationpolicydefinition.md">ReplicationPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sites

_Required_: No

_Type_: List of <a href="sitesdefinition.md">SitesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThirdPartySites

_Required_: No

_Type_: List of <a href="thirdpartysitesdefinition.md">ThirdPartySitesDefinition</a>

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

