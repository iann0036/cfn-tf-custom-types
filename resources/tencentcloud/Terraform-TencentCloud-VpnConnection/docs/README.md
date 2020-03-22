# Terraform::TencentCloud::VpnConnection

Provides a resource to create a VPN connection.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::VpnConnection",
    "Properties" : {
        "<a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>" : <i>String</i>,
        "<a href="#ikedhgroupname" title="IkeDhGroupName">IkeDhGroupName</a>" : <i>String</i>,
        "<a href="#ikeexchangemode" title="IkeExchangeMode">IkeExchangeMode</a>" : <i>String</i>,
        "<a href="#ikelocaladdress" title="IkeLocalAddress">IkeLocalAddress</a>" : <i>String</i>,
        "<a href="#ikelocalfqdnname" title="IkeLocalFqdnName">IkeLocalFqdnName</a>" : <i>String</i>,
        "<a href="#ikelocalidentity" title="IkeLocalIdentity">IkeLocalIdentity</a>" : <i>String</i>,
        "<a href="#ikeprotoauthenalgorithm" title="IkeProtoAuthenAlgorithm">IkeProtoAuthenAlgorithm</a>" : <i>String</i>,
        "<a href="#ikeprotoencryalgorithm" title="IkeProtoEncryAlgorithm">IkeProtoEncryAlgorithm</a>" : <i>String</i>,
        "<a href="#ikeremoteaddress" title="IkeRemoteAddress">IkeRemoteAddress</a>" : <i>String</i>,
        "<a href="#ikeremotefqdnname" title="IkeRemoteFqdnName">IkeRemoteFqdnName</a>" : <i>String</i>,
        "<a href="#ikeremoteidentity" title="IkeRemoteIdentity">IkeRemoteIdentity</a>" : <i>String</i>,
        "<a href="#ikesalifetimeseconds" title="IkeSaLifetimeSeconds">IkeSaLifetimeSeconds</a>" : <i>Double</i>,
        "<a href="#ikeversion" title="IkeVersion">IkeVersion</a>" : <i>String</i>,
        "<a href="#ipsecencryptalgorithm" title="IpsecEncryptAlgorithm">IpsecEncryptAlgorithm</a>" : <i>String</i>,
        "<a href="#ipsecintegrityalgorithm" title="IpsecIntegrityAlgorithm">IpsecIntegrityAlgorithm</a>" : <i>String</i>,
        "<a href="#ipsecpfsdhgroup" title="IpsecPfsDhGroup">IpsecPfsDhGroup</a>" : <i>String</i>,
        "<a href="#ipsecsalifetimeseconds" title="IpsecSaLifetimeSeconds">IpsecSaLifetimeSeconds</a>" : <i>Double</i>,
        "<a href="#ipsecsalifetimetraffic" title="IpsecSaLifetimeTraffic">IpsecSaLifetimeTraffic</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#presharekey" title="PreShareKey">PreShareKey</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>,
        "<a href="#securitygrouppolicy" title="SecurityGroupPolicy">SecurityGroupPolicy</a>" : <i>[ <a href="securitygrouppolicy.md">SecurityGroupPolicy</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::VpnConnection
Properties:
    <a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>: <i>String</i>
    <a href="#ikedhgroupname" title="IkeDhGroupName">IkeDhGroupName</a>: <i>String</i>
    <a href="#ikeexchangemode" title="IkeExchangeMode">IkeExchangeMode</a>: <i>String</i>
    <a href="#ikelocaladdress" title="IkeLocalAddress">IkeLocalAddress</a>: <i>String</i>
    <a href="#ikelocalfqdnname" title="IkeLocalFqdnName">IkeLocalFqdnName</a>: <i>String</i>
    <a href="#ikelocalidentity" title="IkeLocalIdentity">IkeLocalIdentity</a>: <i>String</i>
    <a href="#ikeprotoauthenalgorithm" title="IkeProtoAuthenAlgorithm">IkeProtoAuthenAlgorithm</a>: <i>String</i>
    <a href="#ikeprotoencryalgorithm" title="IkeProtoEncryAlgorithm">IkeProtoEncryAlgorithm</a>: <i>String</i>
    <a href="#ikeremoteaddress" title="IkeRemoteAddress">IkeRemoteAddress</a>: <i>String</i>
    <a href="#ikeremotefqdnname" title="IkeRemoteFqdnName">IkeRemoteFqdnName</a>: <i>String</i>
    <a href="#ikeremoteidentity" title="IkeRemoteIdentity">IkeRemoteIdentity</a>: <i>String</i>
    <a href="#ikesalifetimeseconds" title="IkeSaLifetimeSeconds">IkeSaLifetimeSeconds</a>: <i>Double</i>
    <a href="#ikeversion" title="IkeVersion">IkeVersion</a>: <i>String</i>
    <a href="#ipsecencryptalgorithm" title="IpsecEncryptAlgorithm">IpsecEncryptAlgorithm</a>: <i>String</i>
    <a href="#ipsecintegrityalgorithm" title="IpsecIntegrityAlgorithm">IpsecIntegrityAlgorithm</a>: <i>String</i>
    <a href="#ipsecpfsdhgroup" title="IpsecPfsDhGroup">IpsecPfsDhGroup</a>: <i>String</i>
    <a href="#ipsecsalifetimeseconds" title="IpsecSaLifetimeSeconds">IpsecSaLifetimeSeconds</a>: <i>Double</i>
    <a href="#ipsecsalifetimetraffic" title="IpsecSaLifetimeTraffic">IpsecSaLifetimeTraffic</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#presharekey" title="PreShareKey">PreShareKey</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
    <a href="#securitygrouppolicy" title="SecurityGroupPolicy">SecurityGroupPolicy</a>: <i>
      - <a href="securitygrouppolicy.md">SecurityGroupPolicy</a></i>
</pre>

## Properties

#### CustomerGatewayId

ID of the customer gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeDhGroupName

DH group name of the IKE operation specification, valid values are `GROUP1`, `GROUP2`, `GROUP5`, `GROUP14`, `GROUP24`. Default value is `GROUP1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeExchangeMode

Exchange mode of the IKE operation specification, valid values are `AGGRESSIVE`, `MAIN`. Default value is `MAIN`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLocalAddress

Local address of IKE operation specification, valid when ike_local_identity is `ADDRESS`, generally the value is public_ip_address of the related VPN gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLocalFqdnName

Local FQDN name of the IKE operation specification.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLocalIdentity

Local identity way of IKE operation specification, valid values are `ADDRESS`, `FQDN`. Default value is `ADDRESS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeProtoAuthenAlgorithm

Proto authenticate algorithm of the IKE operation specification, valid values are `MD5`, `SHA`. Default Value is `MD5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeProtoEncryAlgorithm

Proto encrypt algorithm of the IKE operation specification, valid values are `3DES-CBC`, `AES-CBC-128`, `AES-CBC-128`, `AES-CBC-256`, `DES-CBC`. Default value is `3DES-CBC`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeRemoteAddress

Remote address of IKE operation specification, valid when ike_remote_identity is `ADDRESS`, generally the value is public_ip_address of the related customer gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeRemoteFqdnName

Remote FQDN name of the IKE operation specification.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeRemoteIdentity

Remote identity way of IKE operation specification, valid values are `ADDRESS`, `FQDN`. Default value is `ADDRESS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeSaLifetimeSeconds

SA lifetime of the IKE operation specification, unit is `second`. The value ranges from 60 to 604800. Default value is 86400 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeVersion

Version of the IKE operation specification. Default value is `IKEV1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecEncryptAlgorithm

Encrypt algorithm of the IPSEC operation specification, valid values are `3DES-CBC`, `AES-CBC-128`, `AES-CBC-128`, `AES-CBC-256`, `DES-CBC`. Default value is `3DES-CBC`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecIntegrityAlgorithm

Integrity algorithm of the IPSEC operation specification, valid values are `SHA1`, `MD5`. Default value is `MD5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPfsDhGroup

PFS DH group, valid values are `GROUP1`, `GROUP2`, `GROUP5`, `GROUP14`, `GROUP24`, `NULL`. Default value is `NULL`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecSaLifetimeSeconds

SA lifetime of the IPSEC operation specification, unit is `second`. The value ranges from 180 to 604800. Default value is 3600 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecSaLifetimeTraffic

SA lifetime of the IPSEC operation specification, unit is `KB`. The value should not be less then 2560. Default value is 1843200.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the VPN connection. The length of character is limited to 1-60.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreShareKey

Pre-shared key of the VPN connection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags used to associate different resources.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

ID of the VPC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

ID of the VPN gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupPolicy

_Required_: No

_Type_: List of <a href="securitygrouppolicy.md">SecurityGroupPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### EncryptProto

Returns the <code>EncryptProto</code> value.

#### Id

Returns the <code>Id</code> value.

#### NetStatus

Returns the <code>NetStatus</code> value.

#### RouteType

Returns the <code>RouteType</code> value.

#### State

Returns the <code>State</code> value.

#### VpnProto

Returns the <code>VpnProto</code> value.

