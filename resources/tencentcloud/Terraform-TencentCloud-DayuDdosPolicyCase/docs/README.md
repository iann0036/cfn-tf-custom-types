# Terraform::TencentCloud::DayuDdosPolicyCase

Use this resource to create dayu DDoS policy case

~> **NOTE:** when a dayu DDoS policy case is created, there will be a dayu DDoS policy created with the same prefix name in the same time. This resource only supports Anti-DDoS of type `bgp`, `bgp-multip` and `bgpip`. One Anti-DDoS resource can only has one DDoS policy case resource. When there is only one Anti-DDoS resource and one policy case, those two resource will be bind automatically.

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

App protocol set of the DDoS policy case.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppType

App type of the DDoS policy case, and valid values are `WEB`, `GAME`, `APP` and `OTHER`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasAbroad

Indicate whether the service involves overseas or not, valid values are `no` and `yes`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasInitiateTcp

Indicate whether the service actively initiates TCP requests or not, valid values are `no` and `yes`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasInitiateUdp

Indicate whether the actively initiate UDP requests or not, valid values are `no` and `yes`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasVpn

Indicate whether the service involves VPN service or not, valid values are `no` and `yes`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTcpPackageLen

The max length of TCP message package, valid value length should be greater than 0 and less than 1500. It should be greater than `min_tcp_package_len`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUdpPackageLen

The max length of UDP message package, valid value length should be greater than 0 and less than 1500. It should be greater than `min_udp_package_len`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTcpPackageLen

The minimum length of TCP message package, valid value length should be greater than 0 and less than 1500.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinUdpPackageLen

The minimum length of UDP message package, valid value length should be greater than 0 and less than 1500.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the DDoS policy case. Length should between 1 and 64.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerTcpPort

The port that actively initiates TCP requests, valid value is range from 1 to 65535.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerUdpPort

The port that actively initiates UDP requests, valid value is range from 1 to 65535.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformTypes

Platform set of the DDoS policy case.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

Type of the resource that the DDoS policy case works for, valid values are `bgpip`, `bgp` and `bgp-multip`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpEndPort

End port of the TCP service, valid value is range from 0 to 65535. It must be greater than `tcp_start_port`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpFootprint

The fixed signature of TCP protocol load, valid value length is range from 1 to 512.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpStartPort

Start port of the TCP service, valid value is range from 0 to 65535.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpEndPort

End port of the UDP service, valid value is range from 0 to 65535. It must be greater than `udp_start_port`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpFootprint

The fixed signature of TCP protocol load, valid value length is range from 1 to 512.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpStartPort

Start port of the UDP service, valid value is range from 0 to 65535.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebApiUrls

Web API url set.

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

#### Id

Returns the <code>Id</code> value.

#### SceneId

Returns the <code>SceneId</code> value.

