# Terraform::NS1::User

Provides a NS1 User resource. Creating a user sends an invitation email to the
user's email address. This can be used to create, modify, and delete users.
The credentials used must have the `manage_users` permission set.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NS1::User",
    "Properties" : {
        "<a href="#accountmanageaccountsettings" title="AccountManageAccountSettings">AccountManageAccountSettings</a>" : <i>Boolean</i>,
        "<a href="#accountmanageapikeys" title="AccountManageApikeys">AccountManageApikeys</a>" : <i>Boolean</i>,
        "<a href="#accountmanagepaymentmethods" title="AccountManagePaymentMethods">AccountManagePaymentMethods</a>" : <i>Boolean</i>,
        "<a href="#accountmanageplan" title="AccountManagePlan">AccountManagePlan</a>" : <i>Boolean</i>,
        "<a href="#accountmanageteams" title="AccountManageTeams">AccountManageTeams</a>" : <i>Boolean</i>,
        "<a href="#accountmanageusers" title="AccountManageUsers">AccountManageUsers</a>" : <i>Boolean</i>,
        "<a href="#accountviewactivitylog" title="AccountViewActivityLog">AccountViewActivityLog</a>" : <i>Boolean</i>,
        "<a href="#accountviewinvoices" title="AccountViewInvoices">AccountViewInvoices</a>" : <i>Boolean</i>,
        "<a href="#datamanagedatafeeds" title="DataManageDatafeeds">DataManageDatafeeds</a>" : <i>Boolean</i>,
        "<a href="#datamanagedatasources" title="DataManageDatasources">DataManageDatasources</a>" : <i>Boolean</i>,
        "<a href="#datapushtodatafeeds" title="DataPushToDatafeeds">DataPushToDatafeeds</a>" : <i>Boolean</i>,
        "<a href="#dhcpmanagedhcp" title="DhcpManageDhcp">DhcpManageDhcp</a>" : <i>Boolean</i>,
        "<a href="#dhcpviewdhcp" title="DhcpViewDhcp">DhcpViewDhcp</a>" : <i>Boolean</i>,
        "<a href="#dnsmanagezones" title="DnsManageZones">DnsManageZones</a>" : <i>Boolean</i>,
        "<a href="#dnsviewzones" title="DnsViewZones">DnsViewZones</a>" : <i>Boolean</i>,
        "<a href="#dnszonesallow" title="DnsZonesAllow">DnsZonesAllow</a>" : <i>[ String, ... ]</i>,
        "<a href="#dnszonesallowbydefault" title="DnsZonesAllowByDefault">DnsZonesAllowByDefault</a>" : <i>Boolean</i>,
        "<a href="#dnszonesdeny" title="DnsZonesDeny">DnsZonesDeny</a>" : <i>[ String, ... ]</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#ipwhitelist" title="IpWhitelist">IpWhitelist</a>" : <i>[ String, ... ]</i>,
        "<a href="#ipwhiteliststrict" title="IpWhitelistStrict">IpWhitelistStrict</a>" : <i>Boolean</i>,
        "<a href="#ipammanageipam" title="IpamManageIpam">IpamManageIpam</a>" : <i>Boolean</i>,
        "<a href="#ipamviewipam" title="IpamViewIpam">IpamViewIpam</a>" : <i>Boolean</i>,
        "<a href="#monitoringmanagejobs" title="MonitoringManageJobs">MonitoringManageJobs</a>" : <i>Boolean</i>,
        "<a href="#monitoringmanagelists" title="MonitoringManageLists">MonitoringManageLists</a>" : <i>Boolean</i>,
        "<a href="#monitoringviewjobs" title="MonitoringViewJobs">MonitoringViewJobs</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notify" title="Notify">Notify</a>" : <i>[ <a href="notify.md">Notify</a>, ... ]</i>,
        "<a href="#securitymanageactivedirectory" title="SecurityManageActiveDirectory">SecurityManageActiveDirectory</a>" : <i>Boolean</i>,
        "<a href="#securitymanageglobal2fa" title="SecurityManageGlobal2fa">SecurityManageGlobal2fa</a>" : <i>Boolean</i>,
        "<a href="#teams" title="Teams">Teams</a>" : <i>[ String, ... ]</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NS1::User
Properties:
    <a href="#accountmanageaccountsettings" title="AccountManageAccountSettings">AccountManageAccountSettings</a>: <i>Boolean</i>
    <a href="#accountmanageapikeys" title="AccountManageApikeys">AccountManageApikeys</a>: <i>Boolean</i>
    <a href="#accountmanagepaymentmethods" title="AccountManagePaymentMethods">AccountManagePaymentMethods</a>: <i>Boolean</i>
    <a href="#accountmanageplan" title="AccountManagePlan">AccountManagePlan</a>: <i>Boolean</i>
    <a href="#accountmanageteams" title="AccountManageTeams">AccountManageTeams</a>: <i>Boolean</i>
    <a href="#accountmanageusers" title="AccountManageUsers">AccountManageUsers</a>: <i>Boolean</i>
    <a href="#accountviewactivitylog" title="AccountViewActivityLog">AccountViewActivityLog</a>: <i>Boolean</i>
    <a href="#accountviewinvoices" title="AccountViewInvoices">AccountViewInvoices</a>: <i>Boolean</i>
    <a href="#datamanagedatafeeds" title="DataManageDatafeeds">DataManageDatafeeds</a>: <i>Boolean</i>
    <a href="#datamanagedatasources" title="DataManageDatasources">DataManageDatasources</a>: <i>Boolean</i>
    <a href="#datapushtodatafeeds" title="DataPushToDatafeeds">DataPushToDatafeeds</a>: <i>Boolean</i>
    <a href="#dhcpmanagedhcp" title="DhcpManageDhcp">DhcpManageDhcp</a>: <i>Boolean</i>
    <a href="#dhcpviewdhcp" title="DhcpViewDhcp">DhcpViewDhcp</a>: <i>Boolean</i>
    <a href="#dnsmanagezones" title="DnsManageZones">DnsManageZones</a>: <i>Boolean</i>
    <a href="#dnsviewzones" title="DnsViewZones">DnsViewZones</a>: <i>Boolean</i>
    <a href="#dnszonesallow" title="DnsZonesAllow">DnsZonesAllow</a>: <i>
      - String</i>
    <a href="#dnszonesallowbydefault" title="DnsZonesAllowByDefault">DnsZonesAllowByDefault</a>: <i>Boolean</i>
    <a href="#dnszonesdeny" title="DnsZonesDeny">DnsZonesDeny</a>: <i>
      - String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#ipwhitelist" title="IpWhitelist">IpWhitelist</a>: <i>
      - String</i>
    <a href="#ipwhiteliststrict" title="IpWhitelistStrict">IpWhitelistStrict</a>: <i>Boolean</i>
    <a href="#ipammanageipam" title="IpamManageIpam">IpamManageIpam</a>: <i>Boolean</i>
    <a href="#ipamviewipam" title="IpamViewIpam">IpamViewIpam</a>: <i>Boolean</i>
    <a href="#monitoringmanagejobs" title="MonitoringManageJobs">MonitoringManageJobs</a>: <i>Boolean</i>
    <a href="#monitoringmanagelists" title="MonitoringManageLists">MonitoringManageLists</a>: <i>Boolean</i>
    <a href="#monitoringviewjobs" title="MonitoringViewJobs">MonitoringViewJobs</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notify" title="Notify">Notify</a>: <i>
      - <a href="notify.md">Notify</a></i>
    <a href="#securitymanageactivedirectory" title="SecurityManageActiveDirectory">SecurityManageActiveDirectory</a>: <i>Boolean</i>
    <a href="#securitymanageglobal2fa" title="SecurityManageGlobal2fa">SecurityManageGlobal2fa</a>: <i>Boolean</i>
    <a href="#teams" title="Teams">Teams</a>: <i>
      - String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### AccountManageAccountSettings

Whether the user can modify account settings.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountManageApikeys

Whether the user can modify account apikeys.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountManagePaymentMethods

Whether the user can modify account payment methods.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountManagePlan

Whether the user can modify the account plan.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountManageTeams

Whether the user can modify other teams in the account.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountManageUsers

Whether the user can modify account users.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountViewActivityLog

Whether the user can view activity logs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountViewInvoices

Whether the user can view invoices.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataManageDatafeeds

Whether the user can modify data feeds.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataManageDatasources

Whether the user can modify data sources.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataPushToDatafeeds

Whether the user can publish to data feeds.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpManageDhcp

Whether the user can manage DHCP.
Only relevant for the DDI product.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpViewDhcp

Whether the user can view DHCP.
Only relevant for the DDI product.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsManageZones

Whether the user can modify the accounts zones.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsViewZones

Whether the user can view the accounts zones.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsZonesAllow

List of zones that the user may access.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsZonesAllowByDefault

If true, enable the `dns_zones_allow` list, otherwise enable the `dns_zones_deny` list.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsZonesDeny

List of zones that the user may not access.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

The email address of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpWhitelist

The IP addresses to whitelist for this key.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpWhitelistStrict

Sets exclusivity on this IP whitelist.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpamManageIpam

Whether the user can manage IPAM.
Only relevant for the DDI product.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpamViewIpam

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoringManageJobs

Whether the user can modify monitoring jobs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoringManageLists

Whether the user can modify notification lists.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoringViewJobs

Whether the user can view monitoring jobs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The free form name of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notify

Whether or not to notify the user of specified events. Only `billing` is available currently.

_Required_: No

_Type_: List of <a href="notify.md">Notify</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityManageActiveDirectory

Whether the user can manage global active directory.
Only relevant for the DDI product.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityManageGlobal2fa

Whether the user can manage global two factor authentication.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Teams

The teams that the user belongs to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The users login name.

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

