# Terraform::NS1::Team

CloudFormation equivalent of ns1_team

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NS1::Team",
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
        "<a href="#ipammanageipam" title="IpamManageIpam">IpamManageIpam</a>" : <i>Boolean</i>,
        "<a href="#ipamviewipam" title="IpamViewIpam">IpamViewIpam</a>" : <i>Boolean</i>,
        "<a href="#monitoringmanagejobs" title="MonitoringManageJobs">MonitoringManageJobs</a>" : <i>Boolean</i>,
        "<a href="#monitoringmanagelists" title="MonitoringManageLists">MonitoringManageLists</a>" : <i>Boolean</i>,
        "<a href="#monitoringviewjobs" title="MonitoringViewJobs">MonitoringViewJobs</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#securitymanageactivedirectory" title="SecurityManageActiveDirectory">SecurityManageActiveDirectory</a>" : <i>Boolean</i>,
        "<a href="#securitymanageglobal2fa" title="SecurityManageGlobal2fa">SecurityManageGlobal2fa</a>" : <i>Boolean</i>,
        "<a href="#ipwhitelist" title="IpWhitelist">IpWhitelist</a>" : <i>[ <a href="ipwhitelist.md">IpWhitelist</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NS1::Team
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
    <a href="#ipammanageipam" title="IpamManageIpam">IpamManageIpam</a>: <i>Boolean</i>
    <a href="#ipamviewipam" title="IpamViewIpam">IpamViewIpam</a>: <i>Boolean</i>
    <a href="#monitoringmanagejobs" title="MonitoringManageJobs">MonitoringManageJobs</a>: <i>Boolean</i>
    <a href="#monitoringmanagelists" title="MonitoringManageLists">MonitoringManageLists</a>: <i>Boolean</i>
    <a href="#monitoringviewjobs" title="MonitoringViewJobs">MonitoringViewJobs</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#securitymanageactivedirectory" title="SecurityManageActiveDirectory">SecurityManageActiveDirectory</a>: <i>Boolean</i>
    <a href="#securitymanageglobal2fa" title="SecurityManageGlobal2fa">SecurityManageGlobal2fa</a>: <i>Boolean</i>
    <a href="#ipwhitelist" title="IpWhitelist">IpWhitelist</a>: <i>
      - <a href="ipwhitelist.md">IpWhitelist</a></i>
</pre>

## Properties

#### AccountManageAccountSettings

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountManageApikeys

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountManagePaymentMethods

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountManagePlan

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountManageTeams

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountManageUsers

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountViewActivityLog

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountViewInvoices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataManageDatafeeds

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataManageDatasources

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataPushToDatafeeds

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpManageDhcp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpViewDhcp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsManageZones

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsViewZones

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsZonesAllow

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsZonesAllowByDefault

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsZonesDeny

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpamManageIpam

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpamViewIpam

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoringManageJobs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoringManageLists

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoringViewJobs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityManageActiveDirectory

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityManageGlobal2fa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpWhitelist

_Required_: No

_Type_: List of <a href="ipwhitelist.md">IpWhitelist</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

