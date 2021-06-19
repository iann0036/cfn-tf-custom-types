# TF::Aviatrix::Site2cloud

The **aviatrix_site2cloud** resource creates and manages Aviatrix-created Site2Cloud connections.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::Site2cloud",
    "Properties" : {
        "<a href="#backupgatewayname" title="BackupGatewayName">BackupGatewayName</a>" : <i>String</i>,
        "<a href="#backuplocaltunnelip" title="BackupLocalTunnelIp">BackupLocalTunnelIp</a>" : <i>String</i>,
        "<a href="#backuppresharedkey" title="BackupPreSharedKey">BackupPreSharedKey</a>" : <i>String</i>,
        "<a href="#backupremotegatewayip" title="BackupRemoteGatewayIp">BackupRemoteGatewayIp</a>" : <i>String</i>,
        "<a href="#backupremotegatewaylatitude" title="BackupRemoteGatewayLatitude">BackupRemoteGatewayLatitude</a>" : <i>Double</i>,
        "<a href="#backupremotegatewaylongitude" title="BackupRemoteGatewayLongitude">BackupRemoteGatewayLongitude</a>" : <i>Double</i>,
        "<a href="#backupremotetunnelip" title="BackupRemoteTunnelIp">BackupRemoteTunnelIp</a>" : <i>String</i>,
        "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
        "<a href="#connectiontype" title="ConnectionType">ConnectionType</a>" : <i>String</i>,
        "<a href="#customalgorithms" title="CustomAlgorithms">CustomAlgorithms</a>" : <i>Boolean</i>,
        "<a href="#custommapped" title="CustomMapped">CustomMapped</a>" : <i>Boolean</i>,
        "<a href="#enableactiveactive" title="EnableActiveActive">EnableActiveActive</a>" : <i>Boolean</i>,
        "<a href="#enabledeadpeerdetection" title="EnableDeadPeerDetection">EnableDeadPeerDetection</a>" : <i>Boolean</i>,
        "<a href="#enableeventtriggeredha" title="EnableEventTriggeredHa">EnableEventTriggeredHa</a>" : <i>Boolean</i>,
        "<a href="#enableikev2" title="EnableIkev2">EnableIkev2</a>" : <i>Boolean</i>,
        "<a href="#enablesingleipha" title="EnableSingleIpHa">EnableSingleIpHa</a>" : <i>Boolean</i>,
        "<a href="#forwardtraffictotransit" title="ForwardTrafficToTransit">ForwardTrafficToTransit</a>" : <i>Boolean</i>,
        "<a href="#haenabled" title="HaEnabled">HaEnabled</a>" : <i>Boolean</i>,
        "<a href="#localdestinationrealcidrs" title="LocalDestinationRealCidrs">LocalDestinationRealCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#localdestinationvirtualcidrs" title="LocalDestinationVirtualCidrs">LocalDestinationVirtualCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#localsourcerealcidrs" title="LocalSourceRealCidrs">LocalSourceRealCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#localsourcevirtualcidrs" title="LocalSourceVirtualCidrs">LocalSourceVirtualCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#localsubnetcidr" title="LocalSubnetCidr">LocalSubnetCidr</a>" : <i>String</i>,
        "<a href="#localsubnetvirtual" title="LocalSubnetVirtual">LocalSubnetVirtual</a>" : <i>String</i>,
        "<a href="#localtunnelip" title="LocalTunnelIp">LocalTunnelIp</a>" : <i>String</i>,
        "<a href="#phase1remoteidentifier" title="Phase1RemoteIdentifier">Phase1RemoteIdentifier</a>" : <i>[ String, ... ]</i>,
        "<a href="#phase1authentication" title="Phase1Authentication">Phase1Authentication</a>" : <i>String</i>,
        "<a href="#phase1dhgroups" title="Phase1DhGroups">Phase1DhGroups</a>" : <i>String</i>,
        "<a href="#phase1encryption" title="Phase1Encryption">Phase1Encryption</a>" : <i>String</i>,
        "<a href="#phase2authentication" title="Phase2Authentication">Phase2Authentication</a>" : <i>String</i>,
        "<a href="#phase2dhgroups" title="Phase2DhGroups">Phase2DhGroups</a>" : <i>String</i>,
        "<a href="#phase2encryption" title="Phase2Encryption">Phase2Encryption</a>" : <i>String</i>,
        "<a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>" : <i>String</i>,
        "<a href="#primarycloudgatewayname" title="PrimaryCloudGatewayName">PrimaryCloudGatewayName</a>" : <i>String</i>,
        "<a href="#privaterouteencryption" title="PrivateRouteEncryption">PrivateRouteEncryption</a>" : <i>Boolean</i>,
        "<a href="#remotedestinationrealcidrs" title="RemoteDestinationRealCidrs">RemoteDestinationRealCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#remotedestinationvirtualcidrs" title="RemoteDestinationVirtualCidrs">RemoteDestinationVirtualCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#remotegatewayip" title="RemoteGatewayIp">RemoteGatewayIp</a>" : <i>String</i>,
        "<a href="#remotegatewaylatitude" title="RemoteGatewayLatitude">RemoteGatewayLatitude</a>" : <i>Double</i>,
        "<a href="#remotegatewaylongitude" title="RemoteGatewayLongitude">RemoteGatewayLongitude</a>" : <i>Double</i>,
        "<a href="#remotegatewaytype" title="RemoteGatewayType">RemoteGatewayType</a>" : <i>String</i>,
        "<a href="#remotesourcerealcidrs" title="RemoteSourceRealCidrs">RemoteSourceRealCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#remotesourcevirtualcidrs" title="RemoteSourceVirtualCidrs">RemoteSourceVirtualCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#remotesubnetcidr" title="RemoteSubnetCidr">RemoteSubnetCidr</a>" : <i>String</i>,
        "<a href="#remotesubnetvirtual" title="RemoteSubnetVirtual">RemoteSubnetVirtual</a>" : <i>String</i>,
        "<a href="#remotetunnelip" title="RemoteTunnelIp">RemoteTunnelIp</a>" : <i>String</i>,
        "<a href="#routetablelist" title="RouteTableList">RouteTableList</a>" : <i>[ String, ... ]</i>,
        "<a href="#sslserverpool" title="SslServerPool">SslServerPool</a>" : <i>String</i>,
        "<a href="#tunneltype" title="TunnelType">TunnelType</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::Site2cloud
Properties:
    <a href="#backupgatewayname" title="BackupGatewayName">BackupGatewayName</a>: <i>String</i>
    <a href="#backuplocaltunnelip" title="BackupLocalTunnelIp">BackupLocalTunnelIp</a>: <i>String</i>
    <a href="#backuppresharedkey" title="BackupPreSharedKey">BackupPreSharedKey</a>: <i>String</i>
    <a href="#backupremotegatewayip" title="BackupRemoteGatewayIp">BackupRemoteGatewayIp</a>: <i>String</i>
    <a href="#backupremotegatewaylatitude" title="BackupRemoteGatewayLatitude">BackupRemoteGatewayLatitude</a>: <i>Double</i>
    <a href="#backupremotegatewaylongitude" title="BackupRemoteGatewayLongitude">BackupRemoteGatewayLongitude</a>: <i>Double</i>
    <a href="#backupremotetunnelip" title="BackupRemoteTunnelIp">BackupRemoteTunnelIp</a>: <i>String</i>
    <a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
    <a href="#connectiontype" title="ConnectionType">ConnectionType</a>: <i>String</i>
    <a href="#customalgorithms" title="CustomAlgorithms">CustomAlgorithms</a>: <i>Boolean</i>
    <a href="#custommapped" title="CustomMapped">CustomMapped</a>: <i>Boolean</i>
    <a href="#enableactiveactive" title="EnableActiveActive">EnableActiveActive</a>: <i>Boolean</i>
    <a href="#enabledeadpeerdetection" title="EnableDeadPeerDetection">EnableDeadPeerDetection</a>: <i>Boolean</i>
    <a href="#enableeventtriggeredha" title="EnableEventTriggeredHa">EnableEventTriggeredHa</a>: <i>Boolean</i>
    <a href="#enableikev2" title="EnableIkev2">EnableIkev2</a>: <i>Boolean</i>
    <a href="#enablesingleipha" title="EnableSingleIpHa">EnableSingleIpHa</a>: <i>Boolean</i>
    <a href="#forwardtraffictotransit" title="ForwardTrafficToTransit">ForwardTrafficToTransit</a>: <i>Boolean</i>
    <a href="#haenabled" title="HaEnabled">HaEnabled</a>: <i>Boolean</i>
    <a href="#localdestinationrealcidrs" title="LocalDestinationRealCidrs">LocalDestinationRealCidrs</a>: <i>
      - String</i>
    <a href="#localdestinationvirtualcidrs" title="LocalDestinationVirtualCidrs">LocalDestinationVirtualCidrs</a>: <i>
      - String</i>
    <a href="#localsourcerealcidrs" title="LocalSourceRealCidrs">LocalSourceRealCidrs</a>: <i>
      - String</i>
    <a href="#localsourcevirtualcidrs" title="LocalSourceVirtualCidrs">LocalSourceVirtualCidrs</a>: <i>
      - String</i>
    <a href="#localsubnetcidr" title="LocalSubnetCidr">LocalSubnetCidr</a>: <i>String</i>
    <a href="#localsubnetvirtual" title="LocalSubnetVirtual">LocalSubnetVirtual</a>: <i>String</i>
    <a href="#localtunnelip" title="LocalTunnelIp">LocalTunnelIp</a>: <i>String</i>
    <a href="#phase1remoteidentifier" title="Phase1RemoteIdentifier">Phase1RemoteIdentifier</a>: <i>
      - String</i>
    <a href="#phase1authentication" title="Phase1Authentication">Phase1Authentication</a>: <i>String</i>
    <a href="#phase1dhgroups" title="Phase1DhGroups">Phase1DhGroups</a>: <i>String</i>
    <a href="#phase1encryption" title="Phase1Encryption">Phase1Encryption</a>: <i>String</i>
    <a href="#phase2authentication" title="Phase2Authentication">Phase2Authentication</a>: <i>String</i>
    <a href="#phase2dhgroups" title="Phase2DhGroups">Phase2DhGroups</a>: <i>String</i>
    <a href="#phase2encryption" title="Phase2Encryption">Phase2Encryption</a>: <i>String</i>
    <a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>: <i>String</i>
    <a href="#primarycloudgatewayname" title="PrimaryCloudGatewayName">PrimaryCloudGatewayName</a>: <i>String</i>
    <a href="#privaterouteencryption" title="PrivateRouteEncryption">PrivateRouteEncryption</a>: <i>Boolean</i>
    <a href="#remotedestinationrealcidrs" title="RemoteDestinationRealCidrs">RemoteDestinationRealCidrs</a>: <i>
      - String</i>
    <a href="#remotedestinationvirtualcidrs" title="RemoteDestinationVirtualCidrs">RemoteDestinationVirtualCidrs</a>: <i>
      - String</i>
    <a href="#remotegatewayip" title="RemoteGatewayIp">RemoteGatewayIp</a>: <i>String</i>
    <a href="#remotegatewaylatitude" title="RemoteGatewayLatitude">RemoteGatewayLatitude</a>: <i>Double</i>
    <a href="#remotegatewaylongitude" title="RemoteGatewayLongitude">RemoteGatewayLongitude</a>: <i>Double</i>
    <a href="#remotegatewaytype" title="RemoteGatewayType">RemoteGatewayType</a>: <i>String</i>
    <a href="#remotesourcerealcidrs" title="RemoteSourceRealCidrs">RemoteSourceRealCidrs</a>: <i>
      - String</i>
    <a href="#remotesourcevirtualcidrs" title="RemoteSourceVirtualCidrs">RemoteSourceVirtualCidrs</a>: <i>
      - String</i>
    <a href="#remotesubnetcidr" title="RemoteSubnetCidr">RemoteSubnetCidr</a>: <i>String</i>
    <a href="#remotesubnetvirtual" title="RemoteSubnetVirtual">RemoteSubnetVirtual</a>: <i>String</i>
    <a href="#remotetunnelip" title="RemoteTunnelIp">RemoteTunnelIp</a>: <i>String</i>
    <a href="#routetablelist" title="RouteTableList">RouteTableList</a>: <i>
      - String</i>
    <a href="#sslserverpool" title="SslServerPool">SslServerPool</a>: <i>String</i>
    <a href="#tunneltype" title="TunnelType">TunnelType</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### BackupGatewayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupLocalTunnelIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupPreSharedKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRemoteGatewayIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRemoteGatewayLatitude

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRemoteGatewayLongitude

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRemoteTunnelIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAlgorithms

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomMapped

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableActiveActive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDeadPeerDetection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEventTriggeredHa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIkev2

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSingleIpHa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardTrafficToTransit

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalDestinationRealCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalDestinationVirtualCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSourceRealCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSourceVirtualCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSubnetCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSubnetVirtual

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalTunnelIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase1RemoteIdentifier

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase1Authentication

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase1DhGroups

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase1Encryption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase2Authentication

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase2DhGroups

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase2Encryption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreSharedKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryCloudGatewayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateRouteEncryption

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteDestinationRealCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteDestinationVirtualCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGatewayIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGatewayLatitude

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGatewayLongitude

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGatewayType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSourceRealCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSourceVirtualCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSubnetCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSubnetVirtual

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteTunnelIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTableList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslServerPool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

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

