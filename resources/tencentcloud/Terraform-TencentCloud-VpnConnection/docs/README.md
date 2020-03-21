# Terraform::TencentCloud::VpnConnection

CloudFormation equivalent of tencentcloud_vpn_connection

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

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeDhGroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeExchangeMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLocalAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLocalFqdnName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLocalIdentity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeProtoAuthenAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeProtoEncryAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeRemoteAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeRemoteFqdnName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeRemoteIdentity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeSaLifetimeSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecEncryptAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecIntegrityAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPfsDhGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecSaLifetimeSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecSaLifetimeTraffic

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreShareKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupPolicy

_Required_: No

_Type_: List of <a href="securitygrouppolicy.md">SecurityGroupPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### EncryptProto

Returns the <code>EncryptProto</code> value.

#### NetStatus

Returns the <code>NetStatus</code> value.

#### RouteType

Returns the <code>RouteType</code> value.

#### State

Returns the <code>State</code> value.

#### VpnProto

Returns the <code>VpnProto</code> value.

