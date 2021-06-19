# TF::FortiOS::SystemDdns

Configure DDNS.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemDdns",
    "Properties" : {
        "<a href="#boundip" title="BoundIp">BoundIp</a>" : <i>String</i>,
        "<a href="#cleartext" title="ClearText">ClearText</a>" : <i>String</i>,
        "<a href="#ddnsauth" title="DdnsAuth">DdnsAuth</a>" : <i>String</i>,
        "<a href="#ddnsdomain" title="DdnsDomain">DdnsDomain</a>" : <i>String</i>,
        "<a href="#ddnskey" title="DdnsKey">DdnsKey</a>" : <i>String</i>,
        "<a href="#ddnskeyname" title="DdnsKeyname">DdnsKeyname</a>" : <i>String</i>,
        "<a href="#ddnspassword" title="DdnsPassword">DdnsPassword</a>" : <i>String</i>,
        "<a href="#ddnsserver" title="DdnsServer">DdnsServer</a>" : <i>String</i>,
        "<a href="#ddnsserverip" title="DdnsServerIp">DdnsServerIp</a>" : <i>String</i>,
        "<a href="#ddnssn" title="DdnsSn">DdnsSn</a>" : <i>String</i>,
        "<a href="#ddnsttl" title="DdnsTtl">DdnsTtl</a>" : <i>Double</i>,
        "<a href="#ddnsusername" title="DdnsUsername">DdnsUsername</a>" : <i>String</i>,
        "<a href="#ddnszone" title="DdnsZone">DdnsZone</a>" : <i>String</i>,
        "<a href="#ddnsid" title="Ddnsid">Ddnsid</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#sslcertificate" title="SslCertificate">SslCertificate</a>" : <i>String</i>,
        "<a href="#updateinterval" title="UpdateInterval">UpdateInterval</a>" : <i>Double</i>,
        "<a href="#usepublicip" title="UsePublicIp">UsePublicIp</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#monitorinterface" title="MonitorInterface">MonitorInterface</a>" : <i>[ <a href="monitorinterfacedefinition.md">MonitorInterfaceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemDdns
Properties:
    <a href="#boundip" title="BoundIp">BoundIp</a>: <i>String</i>
    <a href="#cleartext" title="ClearText">ClearText</a>: <i>String</i>
    <a href="#ddnsauth" title="DdnsAuth">DdnsAuth</a>: <i>String</i>
    <a href="#ddnsdomain" title="DdnsDomain">DdnsDomain</a>: <i>String</i>
    <a href="#ddnskey" title="DdnsKey">DdnsKey</a>: <i>String</i>
    <a href="#ddnskeyname" title="DdnsKeyname">DdnsKeyname</a>: <i>String</i>
    <a href="#ddnspassword" title="DdnsPassword">DdnsPassword</a>: <i>String</i>
    <a href="#ddnsserver" title="DdnsServer">DdnsServer</a>: <i>String</i>
    <a href="#ddnsserverip" title="DdnsServerIp">DdnsServerIp</a>: <i>String</i>
    <a href="#ddnssn" title="DdnsSn">DdnsSn</a>: <i>String</i>
    <a href="#ddnsttl" title="DdnsTtl">DdnsTtl</a>: <i>Double</i>
    <a href="#ddnsusername" title="DdnsUsername">DdnsUsername</a>: <i>String</i>
    <a href="#ddnszone" title="DdnsZone">DdnsZone</a>: <i>String</i>
    <a href="#ddnsid" title="Ddnsid">Ddnsid</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#sslcertificate" title="SslCertificate">SslCertificate</a>: <i>String</i>
    <a href="#updateinterval" title="UpdateInterval">UpdateInterval</a>: <i>Double</i>
    <a href="#usepublicip" title="UsePublicIp">UsePublicIp</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#monitorinterface" title="MonitorInterface">MonitorInterface</a>: <i>
      - <a href="monitorinterfacedefinition.md">MonitorInterfaceDefinition</a></i>
</pre>

## Properties

#### BoundIp

Bound IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClearText

Enable/disable use of clear text connections. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsAuth

Enable/disable TSIG authentication for your DDNS server. Valid values: `disable`, `tsig`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsDomain

Your fully qualified domain name (for example, yourname.DDNS.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsKey

DDNS update key (base 64 encoding).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsKeyname

DDNS update key name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsPassword

DDNS password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsServer

Select a DDNS service provider. Valid values: `dyndns.org`, `dyns.net`, `tzo.com`, `vavic.com`, `dipdns.net`, `now.net.cn`, `dhs.org`, `easydns.com`, `genericDDNS`, `FortiGuardDDNS`, `noip.com`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsServerIp

Generic DDNS server IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsSn

DDNS Serial Number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsTtl

Time-to-live for DDNS packets.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsUsername

DDNS user name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsZone

Zone of your domain name (for example, DDNS.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ddnsid

DDNS ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificate

Name of local certificate for SSL connections.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateInterval

DDNS update interval (60 - 2592000 sec, default = 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePublicIp

Enable/disable use of public IP address. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorInterface

_Required_: No

_Type_: List of <a href="monitorinterfacedefinition.md">MonitorInterfaceDefinition</a>

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

