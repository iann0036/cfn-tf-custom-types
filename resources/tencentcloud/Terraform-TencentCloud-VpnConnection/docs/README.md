# Terraform::TencentCloud::VpnConnection

CloudFormation equivalent of tencentcloud_vpn_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::VpnConnection",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>" : <i>String</i>,
        "<a href="#encryptproto" title="EncryptProto">EncryptProto</a>" : <i>String</i>,
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
        "<a href="#netstatus" title="NetStatus">NetStatus</a>" : <i>String</i>,
        "<a href="#presharekey" title="PreShareKey">PreShareKey</a>" : <i>String</i>,
        "<a href="#routetype" title="RouteType">RouteType</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>,
        "<a href="#vpnproto" title="VpnProto">VpnProto</a>" : <i>String</i>,
        "<a href="#securitygrouppolicy" title="SecurityGroupPolicy">SecurityGroupPolicy</a>" : <i>[ &lt;a href=&#34;securitygrouppolicy.md&#34;&gt;SecurityGroupPolicy&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::VpnConnection
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>: <i>String</i>
    <a href="#encryptproto" title="EncryptProto">EncryptProto</a>: <i>String</i>
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
    <a href="#netstatus" title="NetStatus">NetStatus</a>: <i>String</i>
    <a href="#presharekey" title="PreShareKey">PreShareKey</a>: <i>String</i>
    <a href="#routetype" title="RouteType">RouteType</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
    <a href="#vpnproto" title="VpnProto">VpnProto</a>: <i>String</i>
    <a href="#securitygrouppolicy" title="SecurityGroupPolicy">SecurityGroupPolicy</a>: <i>
      - &lt;a href=&#34;securitygrouppolicy.md&#34;&gt;SecurityGroupPolicy&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerGatewayId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptProto

_Required_: No

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

#### NetStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreShareKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnProto

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;securitygrouppolicy.md&#34;&gt;SecurityGroupPolicy&lt;/a&gt;

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

Returns the &lt;code&gt;CreateTime&lt;/code&gt; value.

#### EncryptProto

Returns the &lt;code&gt;EncryptProto&lt;/code&gt; value.

#### NetStatus

Returns the &lt;code&gt;NetStatus&lt;/code&gt; value.

#### RouteType

Returns the &lt;code&gt;RouteType&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### VpnProto

Returns the &lt;code&gt;VpnProto&lt;/code&gt; value.

