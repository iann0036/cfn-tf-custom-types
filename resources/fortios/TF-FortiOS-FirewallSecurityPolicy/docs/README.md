# TF::FortiOS::FirewallSecurityPolicy

Configure NGFW IPv4/IPv6 application policies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallSecurityPolicy",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#applicationlist" title="ApplicationList">ApplicationList</a>" : <i>String</i>,
        "<a href="#avprofile" title="AvProfile">AvProfile</a>" : <i>String</i>,
        "<a href="#cifsprofile" title="CifsProfile">CifsProfile</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#dlpsensor" title="DlpSensor">DlpSensor</a>" : <i>String</i>,
        "<a href="#dnsfilterprofile" title="DnsfilterProfile">DnsfilterProfile</a>" : <i>String</i>,
        "<a href="#dstaddrnegate" title="DstaddrNegate">DstaddrNegate</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#emailfilterprofile" title="EmailfilterProfile">EmailfilterProfile</a>" : <i>String</i>,
        "<a href="#enforcedefaultappport" title="EnforceDefaultAppPort">EnforceDefaultAppPort</a>" : <i>String</i>,
        "<a href="#filefilterprofile" title="FileFilterProfile">FileFilterProfile</a>" : <i>String</i>,
        "<a href="#icapprofile" title="IcapProfile">IcapProfile</a>" : <i>String</i>,
        "<a href="#internetservice" title="InternetService">InternetService</a>" : <i>String</i>,
        "<a href="#internetservicenegate" title="InternetServiceNegate">InternetServiceNegate</a>" : <i>String</i>,
        "<a href="#internetservicesrc" title="InternetServiceSrc">InternetServiceSrc</a>" : <i>String</i>,
        "<a href="#internetservicesrcnegate" title="InternetServiceSrcNegate">InternetServiceSrcNegate</a>" : <i>String</i>,
        "<a href="#ipssensor" title="IpsSensor">IpsSensor</a>" : <i>String</i>,
        "<a href="#logtraffic" title="Logtraffic">Logtraffic</a>" : <i>String</i>,
        "<a href="#logtrafficstart" title="LogtrafficStart">LogtrafficStart</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policyid" title="Policyid">Policyid</a>" : <i>Double</i>,
        "<a href="#profilegroup" title="ProfileGroup">ProfileGroup</a>" : <i>String</i>,
        "<a href="#profileprotocoloptions" title="ProfileProtocolOptions">ProfileProtocolOptions</a>" : <i>String</i>,
        "<a href="#profiletype" title="ProfileType">ProfileType</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#senddenypacket" title="SendDenyPacket">SendDenyPacket</a>" : <i>String</i>,
        "<a href="#servicenegate" title="ServiceNegate">ServiceNegate</a>" : <i>String</i>,
        "<a href="#srcaddrnegate" title="SrcaddrNegate">SrcaddrNegate</a>" : <i>String</i>,
        "<a href="#sshfilterprofile" title="SshFilterProfile">SshFilterProfile</a>" : <i>String</i>,
        "<a href="#sslsshprofile" title="SslSshProfile">SslSshProfile</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#voipprofile" title="VoipProfile">VoipProfile</a>" : <i>String</i>,
        "<a href="#webfilterprofile" title="WebfilterProfile">WebfilterProfile</a>" : <i>String</i>,
        "<a href="#appcategory" title="AppCategory">AppCategory</a>" : <i>[ <a href="appcategorydefinition.md">AppCategoryDefinition</a>, ... ]</i>,
        "<a href="#appgroup" title="AppGroup">AppGroup</a>" : <i>[ <a href="appgroupdefinition.md">AppGroupDefinition</a>, ... ]</i>,
        "<a href="#application" title="Application">Application</a>" : <i>[ <a href="applicationdefinition.md">ApplicationDefinition</a>, ... ]</i>,
        "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>[ <a href="dstaddrdefinition.md">DstaddrDefinition</a>, ... ]</i>,
        "<a href="#dstaddr4" title="Dstaddr4">Dstaddr4</a>" : <i>[ <a href="dstaddr4definition.md">Dstaddr4Definition</a>, ... ]</i>,
        "<a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>" : <i>[ <a href="dstaddr6definition.md">Dstaddr6Definition</a>, ... ]</i>,
        "<a href="#dstintf" title="Dstintf">Dstintf</a>" : <i>[ <a href="dstintfdefinition.md">DstintfDefinition</a>, ... ]</i>,
        "<a href="#fssogroups" title="FssoGroups">FssoGroups</a>" : <i>[ <a href="fssogroupsdefinition.md">FssoGroupsDefinition</a>, ... ]</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ <a href="groupsdefinition.md">GroupsDefinition</a>, ... ]</i>,
        "<a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>" : <i>[ <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a>, ... ]</i>,
        "<a href="#internetservicecustomgroup" title="InternetServiceCustomGroup">InternetServiceCustomGroup</a>" : <i>[ <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a>, ... ]</i>,
        "<a href="#internetservicegroup" title="InternetServiceGroup">InternetServiceGroup</a>" : <i>[ <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a>, ... ]</i>,
        "<a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>" : <i>[ <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a>, ... ]</i>,
        "<a href="#internetservicename" title="InternetServiceName">InternetServiceName</a>" : <i>[ <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrccustom" title="InternetServiceSrcCustom">InternetServiceSrcCustom</a>" : <i>[ <a href="internetservicesrccustomdefinition.md">InternetServiceSrcCustomDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrccustomgroup" title="InternetServiceSrcCustomGroup">InternetServiceSrcCustomGroup</a>" : <i>[ <a href="internetservicesrccustomgroupdefinition.md">InternetServiceSrcCustomGroupDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrcgroup" title="InternetServiceSrcGroup">InternetServiceSrcGroup</a>" : <i>[ <a href="internetservicesrcgroupdefinition.md">InternetServiceSrcGroupDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrcid" title="InternetServiceSrcId">InternetServiceSrcId</a>" : <i>[ <a href="internetservicesrciddefinition.md">InternetServiceSrcIdDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrcname" title="InternetServiceSrcName">InternetServiceSrcName</a>" : <i>[ <a href="internetservicesrcnamedefinition.md">InternetServiceSrcNameDefinition</a>, ... ]</i>,
        "<a href="#service" title="Service">Service</a>" : <i>[ <a href="servicedefinition.md">ServiceDefinition</a>, ... ]</i>,
        "<a href="#srcaddr" title="Srcaddr">Srcaddr</a>" : <i>[ <a href="srcaddrdefinition.md">SrcaddrDefinition</a>, ... ]</i>,
        "<a href="#srcaddr4" title="Srcaddr4">Srcaddr4</a>" : <i>[ <a href="srcaddr4definition.md">Srcaddr4Definition</a>, ... ]</i>,
        "<a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>" : <i>[ <a href="srcaddr6definition.md">Srcaddr6Definition</a>, ... ]</i>,
        "<a href="#srcintf" title="Srcintf">Srcintf</a>" : <i>[ <a href="srcintfdefinition.md">SrcintfDefinition</a>, ... ]</i>,
        "<a href="#urlcategory" title="UrlCategory">UrlCategory</a>" : <i>[ <a href="urlcategorydefinition.md">UrlCategoryDefinition</a>, ... ]</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ <a href="usersdefinition.md">UsersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallSecurityPolicy
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#applicationlist" title="ApplicationList">ApplicationList</a>: <i>String</i>
    <a href="#avprofile" title="AvProfile">AvProfile</a>: <i>String</i>
    <a href="#cifsprofile" title="CifsProfile">CifsProfile</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#dlpsensor" title="DlpSensor">DlpSensor</a>: <i>String</i>
    <a href="#dnsfilterprofile" title="DnsfilterProfile">DnsfilterProfile</a>: <i>String</i>
    <a href="#dstaddrnegate" title="DstaddrNegate">DstaddrNegate</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#emailfilterprofile" title="EmailfilterProfile">EmailfilterProfile</a>: <i>String</i>
    <a href="#enforcedefaultappport" title="EnforceDefaultAppPort">EnforceDefaultAppPort</a>: <i>String</i>
    <a href="#filefilterprofile" title="FileFilterProfile">FileFilterProfile</a>: <i>String</i>
    <a href="#icapprofile" title="IcapProfile">IcapProfile</a>: <i>String</i>
    <a href="#internetservice" title="InternetService">InternetService</a>: <i>String</i>
    <a href="#internetservicenegate" title="InternetServiceNegate">InternetServiceNegate</a>: <i>String</i>
    <a href="#internetservicesrc" title="InternetServiceSrc">InternetServiceSrc</a>: <i>String</i>
    <a href="#internetservicesrcnegate" title="InternetServiceSrcNegate">InternetServiceSrcNegate</a>: <i>String</i>
    <a href="#ipssensor" title="IpsSensor">IpsSensor</a>: <i>String</i>
    <a href="#logtraffic" title="Logtraffic">Logtraffic</a>: <i>String</i>
    <a href="#logtrafficstart" title="LogtrafficStart">LogtrafficStart</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policyid" title="Policyid">Policyid</a>: <i>Double</i>
    <a href="#profilegroup" title="ProfileGroup">ProfileGroup</a>: <i>String</i>
    <a href="#profileprotocoloptions" title="ProfileProtocolOptions">ProfileProtocolOptions</a>: <i>String</i>
    <a href="#profiletype" title="ProfileType">ProfileType</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#senddenypacket" title="SendDenyPacket">SendDenyPacket</a>: <i>String</i>
    <a href="#servicenegate" title="ServiceNegate">ServiceNegate</a>: <i>String</i>
    <a href="#srcaddrnegate" title="SrcaddrNegate">SrcaddrNegate</a>: <i>String</i>
    <a href="#sshfilterprofile" title="SshFilterProfile">SshFilterProfile</a>: <i>String</i>
    <a href="#sslsshprofile" title="SslSshProfile">SslSshProfile</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#voipprofile" title="VoipProfile">VoipProfile</a>: <i>String</i>
    <a href="#webfilterprofile" title="WebfilterProfile">WebfilterProfile</a>: <i>String</i>
    <a href="#appcategory" title="AppCategory">AppCategory</a>: <i>
      - <a href="appcategorydefinition.md">AppCategoryDefinition</a></i>
    <a href="#appgroup" title="AppGroup">AppGroup</a>: <i>
      - <a href="appgroupdefinition.md">AppGroupDefinition</a></i>
    <a href="#application" title="Application">Application</a>: <i>
      - <a href="applicationdefinition.md">ApplicationDefinition</a></i>
    <a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>
      - <a href="dstaddrdefinition.md">DstaddrDefinition</a></i>
    <a href="#dstaddr4" title="Dstaddr4">Dstaddr4</a>: <i>
      - <a href="dstaddr4definition.md">Dstaddr4Definition</a></i>
    <a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>: <i>
      - <a href="dstaddr6definition.md">Dstaddr6Definition</a></i>
    <a href="#dstintf" title="Dstintf">Dstintf</a>: <i>
      - <a href="dstintfdefinition.md">DstintfDefinition</a></i>
    <a href="#fssogroups" title="FssoGroups">FssoGroups</a>: <i>
      - <a href="fssogroupsdefinition.md">FssoGroupsDefinition</a></i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - <a href="groupsdefinition.md">GroupsDefinition</a></i>
    <a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>: <i>
      - <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a></i>
    <a href="#internetservicecustomgroup" title="InternetServiceCustomGroup">InternetServiceCustomGroup</a>: <i>
      - <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a></i>
    <a href="#internetservicegroup" title="InternetServiceGroup">InternetServiceGroup</a>: <i>
      - <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a></i>
    <a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>: <i>
      - <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a></i>
    <a href="#internetservicename" title="InternetServiceName">InternetServiceName</a>: <i>
      - <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a></i>
    <a href="#internetservicesrccustom" title="InternetServiceSrcCustom">InternetServiceSrcCustom</a>: <i>
      - <a href="internetservicesrccustomdefinition.md">InternetServiceSrcCustomDefinition</a></i>
    <a href="#internetservicesrccustomgroup" title="InternetServiceSrcCustomGroup">InternetServiceSrcCustomGroup</a>: <i>
      - <a href="internetservicesrccustomgroupdefinition.md">InternetServiceSrcCustomGroupDefinition</a></i>
    <a href="#internetservicesrcgroup" title="InternetServiceSrcGroup">InternetServiceSrcGroup</a>: <i>
      - <a href="internetservicesrcgroupdefinition.md">InternetServiceSrcGroupDefinition</a></i>
    <a href="#internetservicesrcid" title="InternetServiceSrcId">InternetServiceSrcId</a>: <i>
      - <a href="internetservicesrciddefinition.md">InternetServiceSrcIdDefinition</a></i>
    <a href="#internetservicesrcname" title="InternetServiceSrcName">InternetServiceSrcName</a>: <i>
      - <a href="internetservicesrcnamedefinition.md">InternetServiceSrcNameDefinition</a></i>
    <a href="#service" title="Service">Service</a>: <i>
      - <a href="servicedefinition.md">ServiceDefinition</a></i>
    <a href="#srcaddr" title="Srcaddr">Srcaddr</a>: <i>
      - <a href="srcaddrdefinition.md">SrcaddrDefinition</a></i>
    <a href="#srcaddr4" title="Srcaddr4">Srcaddr4</a>: <i>
      - <a href="srcaddr4definition.md">Srcaddr4Definition</a></i>
    <a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>: <i>
      - <a href="srcaddr6definition.md">Srcaddr6Definition</a></i>
    <a href="#srcintf" title="Srcintf">Srcintf</a>: <i>
      - <a href="srcintfdefinition.md">SrcintfDefinition</a></i>
    <a href="#urlcategory" title="UrlCategory">UrlCategory</a>: <i>
      - <a href="urlcategorydefinition.md">UrlCategoryDefinition</a></i>
    <a href="#users" title="Users">Users</a>: <i>
      - <a href="usersdefinition.md">UsersDefinition</a></i>
</pre>

## Properties

#### Action

Policy action (accept/deny). Valid values: `accept`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationList

Name of an existing Application list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvProfile

Name of an existing Antivirus profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CifsProfile

Name of an existing CIFS profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DlpSensor

Name of an existing DLP sensor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsfilterProfile

Name of an existing DNS filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstaddrNegate

When enabled dstaddr/dstaddr6 specifies what the destination address must NOT be. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailfilterProfile

Name of an existing email filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceDefaultAppPort

Enable/disable default application port enforcement for allowed applications. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileFilterProfile

Name of an existing file-filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcapProfile

Name of an existing ICAP profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetService

Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceNegate

When enabled internet-service specifies what the service must NOT be. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrc

Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcNegate

When enabled internet-service-src specifies what the service must NOT be. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsSensor

Name of an existing IPS sensor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logtraffic

Enable or disable logging. Log all sessions or security profile sessions. Valid values: `all`, `utm`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogtrafficStart

Record logs when a session starts. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Policy name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policyid

Policy ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileGroup

Name of profile group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileProtocolOptions

Name of an existing Protocol options profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileType

Determine whether the firewall policy allows security profile groups or single profiles only. Valid values: `single`, `group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

Schedule name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendDenyPacket

Enable to send a reply when a session is denied or blocked by a firewall policy. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceNegate

When enabled service specifies what the service must NOT be. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcaddrNegate

When enabled srcaddr/srcaddr6 specifies what the source address must NOT be. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshFilterProfile

Name of an existing SSH filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSshProfile

Name of an existing SSL SSH profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable or disable this policy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

Universally Unique Identifier (UUID; automatically assigned but can be manually reset).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VoipProfile

Name of an existing VoIP profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterProfile

Name of an existing Web filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppCategory

_Required_: No

_Type_: List of <a href="appcategorydefinition.md">AppCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppGroup

_Required_: No

_Type_: List of <a href="appgroupdefinition.md">AppGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Application

_Required_: No

_Type_: List of <a href="applicationdefinition.md">ApplicationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

_Required_: No

_Type_: List of <a href="dstaddrdefinition.md">DstaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr4

_Required_: No

_Type_: List of <a href="dstaddr4definition.md">Dstaddr4Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr6

_Required_: No

_Type_: List of <a href="dstaddr6definition.md">Dstaddr6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstintf

_Required_: No

_Type_: List of <a href="dstintfdefinition.md">DstintfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FssoGroups

_Required_: No

_Type_: List of <a href="fssogroupsdefinition.md">FssoGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of <a href="groupsdefinition.md">GroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCustom

_Required_: No

_Type_: List of <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCustomGroup

_Required_: No

_Type_: List of <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceGroup

_Required_: No

_Type_: List of <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceId

_Required_: No

_Type_: List of <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceName

_Required_: No

_Type_: List of <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcCustom

_Required_: No

_Type_: List of <a href="internetservicesrccustomdefinition.md">InternetServiceSrcCustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcCustomGroup

_Required_: No

_Type_: List of <a href="internetservicesrccustomgroupdefinition.md">InternetServiceSrcCustomGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcGroup

_Required_: No

_Type_: List of <a href="internetservicesrcgroupdefinition.md">InternetServiceSrcGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcId

_Required_: No

_Type_: List of <a href="internetservicesrciddefinition.md">InternetServiceSrcIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcName

_Required_: No

_Type_: List of <a href="internetservicesrcnamedefinition.md">InternetServiceSrcNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="servicedefinition.md">ServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr

_Required_: No

_Type_: List of <a href="srcaddrdefinition.md">SrcaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr4

_Required_: No

_Type_: List of <a href="srcaddr4definition.md">Srcaddr4Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr6

_Required_: No

_Type_: List of <a href="srcaddr6definition.md">Srcaddr6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcintf

_Required_: No

_Type_: List of <a href="srcintfdefinition.md">SrcintfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlCategory

_Required_: No

_Type_: List of <a href="urlcategorydefinition.md">UrlCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of <a href="usersdefinition.md">UsersDefinition</a>

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

