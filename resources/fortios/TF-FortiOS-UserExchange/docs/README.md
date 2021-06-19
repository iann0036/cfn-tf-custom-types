# TF::FortiOS::UserExchange

Configure MS Exchange server entries.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::UserExchange",
    "Properties" : {
        "<a href="#authlevel" title="AuthLevel">AuthLevel</a>" : <i>String</i>,
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#autodiscoverkdc" title="AutoDiscoverKdc">AutoDiscoverKdc</a>" : <i>String</i>,
        "<a href="#connectprotocol" title="ConnectProtocol">ConnectProtocol</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#httpauthtype" title="HttpAuthType">HttpAuthType</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#sslminprotoversion" title="SslMinProtoVersion">SslMinProtoVersion</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#kdcip" title="KdcIp">KdcIp</a>" : <i>[ <a href="kdcipdefinition.md">KdcIpDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::UserExchange
Properties:
    <a href="#authlevel" title="AuthLevel">AuthLevel</a>: <i>String</i>
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#autodiscoverkdc" title="AutoDiscoverKdc">AutoDiscoverKdc</a>: <i>String</i>
    <a href="#connectprotocol" title="ConnectProtocol">ConnectProtocol</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#httpauthtype" title="HttpAuthType">HttpAuthType</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#sslminprotoversion" title="SslMinProtoVersion">SslMinProtoVersion</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#kdcip" title="KdcIp">KdcIp</a>: <i>
      - <a href="kdcipdefinition.md">KdcIpDefinition</a></i>
</pre>

## Properties

#### AuthLevel

Authentication security level used for the RPC protocol layer. Valid values: `connect`, `call`, `packet`, `integrity`, `privacy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

Authentication security type used for the RPC protocol layer. Valid values: `spnego`, `ntlm`, `kerberos`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoDiscoverKdc

Enable/disable automatic discovery of KDC IP addresses. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectProtocol

Connection protocol used to connect to MS Exchange service. Valid values: `rpc-over-tcp`, `rpc-over-http`, `rpc-over-https`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

MS Exchange server fully qualified domain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpAuthType

Authentication security type used for the HTTP transport. Valid values: `basic`, `ntlm`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

Server IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

MS Exchange server entry name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password for the specified username.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

MS Exchange server hostname.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinProtoVersion

Minimum SSL/TLS protocol version for HTTPS transport (default is to follow system global setting). Valid values: `default`, `SSLv3`, `TLSv1`, `TLSv1-1`, `TLSv1-2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

User name used to sign in to the server. Must have proper permissions for service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KdcIp

_Required_: No

_Type_: List of <a href="kdcipdefinition.md">KdcIpDefinition</a>

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

