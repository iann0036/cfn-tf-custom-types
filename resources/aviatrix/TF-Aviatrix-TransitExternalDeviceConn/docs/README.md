# TF::Aviatrix::TransitExternalDeviceConn

The **aviatrix_transit_external_device_conn** resource creates and manages the connection between the Aviatrix transit gateway and an External Device for purposes of Transit Network.

For more information on this feature, please see documentation [here](https://docs.aviatrix.com/HowTos/transitgw_external.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::TransitExternalDeviceConn",
    "Properties" : {
        "<a href="#approvedcidrs" title="ApprovedCidrs">ApprovedCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#backupbgpremoteasnum" title="BackupBgpRemoteAsNum">BackupBgpRemoteAsNum</a>" : <i>String</i>,
        "<a href="#backupdirectconnect" title="BackupDirectConnect">BackupDirectConnect</a>" : <i>Boolean</i>,
        "<a href="#backuplocallanip" title="BackupLocalLanIp">BackupLocalLanIp</a>" : <i>String</i>,
        "<a href="#backuplocaltunnelcidr" title="BackupLocalTunnelCidr">BackupLocalTunnelCidr</a>" : <i>String</i>,
        "<a href="#backuppresharedkey" title="BackupPreSharedKey">BackupPreSharedKey</a>" : <i>String</i>,
        "<a href="#backupremotegatewayip" title="BackupRemoteGatewayIp">BackupRemoteGatewayIp</a>" : <i>String</i>,
        "<a href="#backupremotelanip" title="BackupRemoteLanIp">BackupRemoteLanIp</a>" : <i>String</i>,
        "<a href="#backupremotetunnelcidr" title="BackupRemoteTunnelCidr">BackupRemoteTunnelCidr</a>" : <i>String</i>,
        "<a href="#bgplocalasnum" title="BgpLocalAsNum">BgpLocalAsNum</a>" : <i>String</i>,
        "<a href="#bgpremoteasnum" title="BgpRemoteAsNum">BgpRemoteAsNum</a>" : <i>String</i>,
        "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
        "<a href="#connectiontype" title="ConnectionType">ConnectionType</a>" : <i>String</i>,
        "<a href="#customalgorithms" title="CustomAlgorithms">CustomAlgorithms</a>" : <i>Boolean</i>,
        "<a href="#directconnect" title="DirectConnect">DirectConnect</a>" : <i>Boolean</i>,
        "<a href="#enableedgesegmentation" title="EnableEdgeSegmentation">EnableEdgeSegmentation</a>" : <i>Boolean</i>,
        "<a href="#enableeventtriggeredha" title="EnableEventTriggeredHa">EnableEventTriggeredHa</a>" : <i>Boolean</i>,
        "<a href="#enableikev2" title="EnableIkev2">EnableIkev2</a>" : <i>Boolean</i>,
        "<a href="#enablelearnedcidrsapproval" title="EnableLearnedCidrsApproval">EnableLearnedCidrsApproval</a>" : <i>Boolean</i>,
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#haenabled" title="HaEnabled">HaEnabled</a>" : <i>Boolean</i>,
        "<a href="#locallanip" title="LocalLanIp">LocalLanIp</a>" : <i>String</i>,
        "<a href="#localtunnelcidr" title="LocalTunnelCidr">LocalTunnelCidr</a>" : <i>String</i>,
        "<a href="#manualbgpadvertisedcidrs" title="ManualBgpAdvertisedCidrs">ManualBgpAdvertisedCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#phase1remoteidentifier" title="Phase1RemoteIdentifier">Phase1RemoteIdentifier</a>" : <i>[ String, ... ]</i>,
        "<a href="#phase1authentication" title="Phase1Authentication">Phase1Authentication</a>" : <i>String</i>,
        "<a href="#phase1dhgroups" title="Phase1DhGroups">Phase1DhGroups</a>" : <i>String</i>,
        "<a href="#phase1encryption" title="Phase1Encryption">Phase1Encryption</a>" : <i>String</i>,
        "<a href="#phase2authentication" title="Phase2Authentication">Phase2Authentication</a>" : <i>String</i>,
        "<a href="#phase2dhgroups" title="Phase2DhGroups">Phase2DhGroups</a>" : <i>String</i>,
        "<a href="#phase2encryption" title="Phase2Encryption">Phase2Encryption</a>" : <i>String</i>,
        "<a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>" : <i>String</i>,
        "<a href="#remotegatewayip" title="RemoteGatewayIp">RemoteGatewayIp</a>" : <i>String</i>,
        "<a href="#remotelanip" title="RemoteLanIp">RemoteLanIp</a>" : <i>String</i>,
        "<a href="#remotesubnet" title="RemoteSubnet">RemoteSubnet</a>" : <i>String</i>,
        "<a href="#remotetunnelcidr" title="RemoteTunnelCidr">RemoteTunnelCidr</a>" : <i>String</i>,
        "<a href="#remotevpcname" title="RemoteVpcName">RemoteVpcName</a>" : <i>String</i>,
        "<a href="#switchtohastandbygateway" title="SwitchToHaStandbyGateway">SwitchToHaStandbyGateway</a>" : <i>Boolean</i>,
        "<a href="#tunnelprotocol" title="TunnelProtocol">TunnelProtocol</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::TransitExternalDeviceConn
Properties:
    <a href="#approvedcidrs" title="ApprovedCidrs">ApprovedCidrs</a>: <i>
      - String</i>
    <a href="#backupbgpremoteasnum" title="BackupBgpRemoteAsNum">BackupBgpRemoteAsNum</a>: <i>String</i>
    <a href="#backupdirectconnect" title="BackupDirectConnect">BackupDirectConnect</a>: <i>Boolean</i>
    <a href="#backuplocallanip" title="BackupLocalLanIp">BackupLocalLanIp</a>: <i>String</i>
    <a href="#backuplocaltunnelcidr" title="BackupLocalTunnelCidr">BackupLocalTunnelCidr</a>: <i>String</i>
    <a href="#backuppresharedkey" title="BackupPreSharedKey">BackupPreSharedKey</a>: <i>String</i>
    <a href="#backupremotegatewayip" title="BackupRemoteGatewayIp">BackupRemoteGatewayIp</a>: <i>String</i>
    <a href="#backupremotelanip" title="BackupRemoteLanIp">BackupRemoteLanIp</a>: <i>String</i>
    <a href="#backupremotetunnelcidr" title="BackupRemoteTunnelCidr">BackupRemoteTunnelCidr</a>: <i>String</i>
    <a href="#bgplocalasnum" title="BgpLocalAsNum">BgpLocalAsNum</a>: <i>String</i>
    <a href="#bgpremoteasnum" title="BgpRemoteAsNum">BgpRemoteAsNum</a>: <i>String</i>
    <a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
    <a href="#connectiontype" title="ConnectionType">ConnectionType</a>: <i>String</i>
    <a href="#customalgorithms" title="CustomAlgorithms">CustomAlgorithms</a>: <i>Boolean</i>
    <a href="#directconnect" title="DirectConnect">DirectConnect</a>: <i>Boolean</i>
    <a href="#enableedgesegmentation" title="EnableEdgeSegmentation">EnableEdgeSegmentation</a>: <i>Boolean</i>
    <a href="#enableeventtriggeredha" title="EnableEventTriggeredHa">EnableEventTriggeredHa</a>: <i>Boolean</i>
    <a href="#enableikev2" title="EnableIkev2">EnableIkev2</a>: <i>Boolean</i>
    <a href="#enablelearnedcidrsapproval" title="EnableLearnedCidrsApproval">EnableLearnedCidrsApproval</a>: <i>Boolean</i>
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#haenabled" title="HaEnabled">HaEnabled</a>: <i>Boolean</i>
    <a href="#locallanip" title="LocalLanIp">LocalLanIp</a>: <i>String</i>
    <a href="#localtunnelcidr" title="LocalTunnelCidr">LocalTunnelCidr</a>: <i>String</i>
    <a href="#manualbgpadvertisedcidrs" title="ManualBgpAdvertisedCidrs">ManualBgpAdvertisedCidrs</a>: <i>
      - String</i>
    <a href="#phase1remoteidentifier" title="Phase1RemoteIdentifier">Phase1RemoteIdentifier</a>: <i>
      - String</i>
    <a href="#phase1authentication" title="Phase1Authentication">Phase1Authentication</a>: <i>String</i>
    <a href="#phase1dhgroups" title="Phase1DhGroups">Phase1DhGroups</a>: <i>String</i>
    <a href="#phase1encryption" title="Phase1Encryption">Phase1Encryption</a>: <i>String</i>
    <a href="#phase2authentication" title="Phase2Authentication">Phase2Authentication</a>: <i>String</i>
    <a href="#phase2dhgroups" title="Phase2DhGroups">Phase2DhGroups</a>: <i>String</i>
    <a href="#phase2encryption" title="Phase2Encryption">Phase2Encryption</a>: <i>String</i>
    <a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>: <i>String</i>
    <a href="#remotegatewayip" title="RemoteGatewayIp">RemoteGatewayIp</a>: <i>String</i>
    <a href="#remotelanip" title="RemoteLanIp">RemoteLanIp</a>: <i>String</i>
    <a href="#remotesubnet" title="RemoteSubnet">RemoteSubnet</a>: <i>String</i>
    <a href="#remotetunnelcidr" title="RemoteTunnelCidr">RemoteTunnelCidr</a>: <i>String</i>
    <a href="#remotevpcname" title="RemoteVpcName">RemoteVpcName</a>: <i>String</i>
    <a href="#switchtohastandbygateway" title="SwitchToHaStandbyGateway">SwitchToHaStandbyGateway</a>: <i>Boolean</i>
    <a href="#tunnelprotocol" title="TunnelProtocol">TunnelProtocol</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### ApprovedCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupBgpRemoteAsNum

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupDirectConnect

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupLocalLanIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupLocalTunnelCidr

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

#### BackupRemoteLanIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRemoteTunnelCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpLocalAsNum

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpRemoteAsNum

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAlgorithms

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectConnect

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEdgeSegmentation

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

#### EnableLearnedCidrsApproval

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalLanIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalTunnelCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManualBgpAdvertisedCidrs

_Required_: No

_Type_: List of String

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

#### RemoteGatewayIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteLanIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSubnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteTunnelCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteVpcName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchToHaStandbyGateway

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelProtocol

_Required_: No

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

