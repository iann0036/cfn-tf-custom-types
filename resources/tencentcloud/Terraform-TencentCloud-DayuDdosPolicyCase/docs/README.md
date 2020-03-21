# Terraform::TencentCloud::DayuDdosPolicyCase

CloudFormation equivalent of tencentcloud_dayu_ddos_policy_case

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::DayuDdosPolicyCase",
    "Properties" : {
        "<a href="#appprotocols" title="AppProtocols">AppProtocols</a>" : <i>[ String, ... ]</i>,
        "<a href="#apptype" title="AppType">AppType</a>" : <i>String</i>,
        "<a href="#hasabroad" title="HasAbroad">HasAbroad</a>" : <i>String</i>,
        "<a href="#hasinitiatetcp" title="HasInitiateTcp">HasInitiateTcp</a>" : <i>String</i>,
        "<a href="#hasinitiateudp" title="HasInitiateUdp">HasInitiateUdp</a>" : <i>String</i>,
        "<a href="#hasvpn" title="HasVpn">HasVpn</a>" : <i>String</i>,
        "<a href="#maxtcppackagelen" title="MaxTcpPackageLen">MaxTcpPackageLen</a>" : <i>String</i>,
        "<a href="#maxudppackagelen" title="MaxUdpPackageLen">MaxUdpPackageLen</a>" : <i>String</i>,
        "<a href="#mintcppackagelen" title="MinTcpPackageLen">MinTcpPackageLen</a>" : <i>String</i>,
        "<a href="#minudppackagelen" title="MinUdpPackageLen">MinUdpPackageLen</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#peertcpport" title="PeerTcpPort">PeerTcpPort</a>" : <i>String</i>,
        "<a href="#peerudpport" title="PeerUdpPort">PeerUdpPort</a>" : <i>String</i>,
        "<a href="#platformtypes" title="PlatformTypes">PlatformTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#tcpendport" title="TcpEndPort">TcpEndPort</a>" : <i>String</i>,
        "<a href="#tcpfootprint" title="TcpFootprint">TcpFootprint</a>" : <i>String</i>,
        "<a href="#tcpstartport" title="TcpStartPort">TcpStartPort</a>" : <i>String</i>,
        "<a href="#udpendport" title="UdpEndPort">UdpEndPort</a>" : <i>String</i>,
        "<a href="#udpfootprint" title="UdpFootprint">UdpFootprint</a>" : <i>String</i>,
        "<a href="#udpstartport" title="UdpStartPort">UdpStartPort</a>" : <i>String</i>,
        "<a href="#webapiurls" title="WebApiUrls">WebApiUrls</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::DayuDdosPolicyCase
Properties:
    <a href="#appprotocols" title="AppProtocols">AppProtocols</a>: <i>
      - String</i>
    <a href="#apptype" title="AppType">AppType</a>: <i>String</i>
    <a href="#hasabroad" title="HasAbroad">HasAbroad</a>: <i>String</i>
    <a href="#hasinitiatetcp" title="HasInitiateTcp">HasInitiateTcp</a>: <i>String</i>
    <a href="#hasinitiateudp" title="HasInitiateUdp">HasInitiateUdp</a>: <i>String</i>
    <a href="#hasvpn" title="HasVpn">HasVpn</a>: <i>String</i>
    <a href="#maxtcppackagelen" title="MaxTcpPackageLen">MaxTcpPackageLen</a>: <i>String</i>
    <a href="#maxudppackagelen" title="MaxUdpPackageLen">MaxUdpPackageLen</a>: <i>String</i>
    <a href="#mintcppackagelen" title="MinTcpPackageLen">MinTcpPackageLen</a>: <i>String</i>
    <a href="#minudppackagelen" title="MinUdpPackageLen">MinUdpPackageLen</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#peertcpport" title="PeerTcpPort">PeerTcpPort</a>: <i>String</i>
    <a href="#peerudpport" title="PeerUdpPort">PeerUdpPort</a>: <i>String</i>
    <a href="#platformtypes" title="PlatformTypes">PlatformTypes</a>: <i>
      - String</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#tcpendport" title="TcpEndPort">TcpEndPort</a>: <i>String</i>
    <a href="#tcpfootprint" title="TcpFootprint">TcpFootprint</a>: <i>String</i>
    <a href="#tcpstartport" title="TcpStartPort">TcpStartPort</a>: <i>String</i>
    <a href="#udpendport" title="UdpEndPort">UdpEndPort</a>: <i>String</i>
    <a href="#udpfootprint" title="UdpFootprint">UdpFootprint</a>: <i>String</i>
    <a href="#udpstartport" title="UdpStartPort">UdpStartPort</a>: <i>String</i>
    <a href="#webapiurls" title="WebApiUrls">WebApiUrls</a>: <i>
      - String</i>
</pre>

## Properties

#### AppProtocols

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasAbroad

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasInitiateTcp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasInitiateUdp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasVpn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTcpPackageLen

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUdpPackageLen

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTcpPackageLen

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinUdpPackageLen

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerTcpPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerUdpPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpEndPort

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpFootprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpStartPort

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpEndPort

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpFootprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpStartPort

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebApiUrls

_Required_: Yes

_Type_: List of String

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

#### SceneId

Returns the <code>SceneId</code> value.

