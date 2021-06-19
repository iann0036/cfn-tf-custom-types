# TF::Aviatrix::SpokeGateway

The **aviatrix_spoke_gateway** resource allows the creation and management of Aviatrix spoke gateways.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::SpokeGateway",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#allocateneweip" title="AllocateNewEip">AllocateNewEip</a>" : <i>Boolean</i>,
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>Double</i>,
        "<a href="#customermanagedkeys" title="CustomerManagedKeys">CustomerManagedKeys</a>" : <i>String</i>,
        "<a href="#customizedspokevpcroutes" title="CustomizedSpokeVpcRoutes">CustomizedSpokeVpcRoutes</a>" : <i>String</i>,
        "<a href="#eip" title="Eip">Eip</a>" : <i>String</i>,
        "<a href="#enableactivemesh" title="EnableActiveMesh">EnableActiveMesh</a>" : <i>Boolean</i>,
        "<a href="#enableautoadvertises2ccidrs" title="EnableAutoAdvertiseS2cCidrs">EnableAutoAdvertiseS2cCidrs</a>" : <i>Boolean</i>,
        "<a href="#enableencryptvolume" title="EnableEncryptVolume">EnableEncryptVolume</a>" : <i>Boolean</i>,
        "<a href="#enablejumboframe" title="EnableJumboFrame">EnableJumboFrame</a>" : <i>Boolean</i>,
        "<a href="#enablemonitorgatewaysubnets" title="EnableMonitorGatewaySubnets">EnableMonitorGatewaySubnets</a>" : <i>Boolean</i>,
        "<a href="#enableprivateoob" title="EnablePrivateOob">EnablePrivateOob</a>" : <i>Boolean</i>,
        "<a href="#enableprivatevpcdefaultroute" title="EnablePrivateVpcDefaultRoute">EnablePrivateVpcDefaultRoute</a>" : <i>Boolean</i>,
        "<a href="#enableskippublicroutetableupdate" title="EnableSkipPublicRouteTableUpdate">EnableSkipPublicRouteTableUpdate</a>" : <i>Boolean</i>,
        "<a href="#enablevpcdnsserver" title="EnableVpcDnsServer">EnableVpcDnsServer</a>" : <i>Boolean</i>,
        "<a href="#faultdomain" title="FaultDomain">FaultDomain</a>" : <i>String</i>,
        "<a href="#filteredspokevpcroutes" title="FilteredSpokeVpcRoutes">FilteredSpokeVpcRoutes</a>" : <i>String</i>,
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#gwsize" title="GwSize">GwSize</a>" : <i>String</i>,
        "<a href="#haavailabilitydomain" title="HaAvailabilityDomain">HaAvailabilityDomain</a>" : <i>String</i>,
        "<a href="#haeip" title="HaEip">HaEip</a>" : <i>String</i>,
        "<a href="#hafaultdomain" title="HaFaultDomain">HaFaultDomain</a>" : <i>String</i>,
        "<a href="#hagwsize" title="HaGwSize">HaGwSize</a>" : <i>String</i>,
        "<a href="#hainsanemodeaz" title="HaInsaneModeAz">HaInsaneModeAz</a>" : <i>String</i>,
        "<a href="#haoobavailabilityzone" title="HaOobAvailabilityZone">HaOobAvailabilityZone</a>" : <i>String</i>,
        "<a href="#haoobmanagementsubnet" title="HaOobManagementSubnet">HaOobManagementSubnet</a>" : <i>String</i>,
        "<a href="#hasubnet" title="HaSubnet">HaSubnet</a>" : <i>String</i>,
        "<a href="#hazone" title="HaZone">HaZone</a>" : <i>String</i>,
        "<a href="#includedadvertisedspokeroutes" title="IncludedAdvertisedSpokeRoutes">IncludedAdvertisedSpokeRoutes</a>" : <i>String</i>,
        "<a href="#insanemode" title="InsaneMode">InsaneMode</a>" : <i>Boolean</i>,
        "<a href="#insanemodeaz" title="InsaneModeAz">InsaneModeAz</a>" : <i>String</i>,
        "<a href="#managetransitgatewayattachment" title="ManageTransitGatewayAttachment">ManageTransitGatewayAttachment</a>" : <i>Boolean</i>,
        "<a href="#monitorexcludelist" title="MonitorExcludeList">MonitorExcludeList</a>" : <i>[ String, ... ]</i>,
        "<a href="#oobavailabilityzone" title="OobAvailabilityZone">OobAvailabilityZone</a>" : <i>String</i>,
        "<a href="#oobmanagementsubnet" title="OobManagementSubnet">OobManagementSubnet</a>" : <i>String</i>,
        "<a href="#singleazha" title="SingleAzHa">SingleAzHa</a>" : <i>Boolean</i>,
        "<a href="#singleipsnat" title="SingleIpSnat">SingleIpSnat</a>" : <i>Boolean</i>,
        "<a href="#storagename" title="StorageName">StorageName</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#taglist" title="TagList">TagList</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#transitgw" title="TransitGw">TransitGw</a>" : <i>String</i>,
        "<a href="#tunneldetectiontime" title="TunnelDetectionTime">TunnelDetectionTime</a>" : <i>Double</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpcreg" title="VpcReg">VpcReg</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::SpokeGateway
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#allocateneweip" title="AllocateNewEip">AllocateNewEip</a>: <i>Boolean</i>
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#cloudtype" title="CloudType">CloudType</a>: <i>Double</i>
    <a href="#customermanagedkeys" title="CustomerManagedKeys">CustomerManagedKeys</a>: <i>String</i>
    <a href="#customizedspokevpcroutes" title="CustomizedSpokeVpcRoutes">CustomizedSpokeVpcRoutes</a>: <i>String</i>
    <a href="#eip" title="Eip">Eip</a>: <i>String</i>
    <a href="#enableactivemesh" title="EnableActiveMesh">EnableActiveMesh</a>: <i>Boolean</i>
    <a href="#enableautoadvertises2ccidrs" title="EnableAutoAdvertiseS2cCidrs">EnableAutoAdvertiseS2cCidrs</a>: <i>Boolean</i>
    <a href="#enableencryptvolume" title="EnableEncryptVolume">EnableEncryptVolume</a>: <i>Boolean</i>
    <a href="#enablejumboframe" title="EnableJumboFrame">EnableJumboFrame</a>: <i>Boolean</i>
    <a href="#enablemonitorgatewaysubnets" title="EnableMonitorGatewaySubnets">EnableMonitorGatewaySubnets</a>: <i>Boolean</i>
    <a href="#enableprivateoob" title="EnablePrivateOob">EnablePrivateOob</a>: <i>Boolean</i>
    <a href="#enableprivatevpcdefaultroute" title="EnablePrivateVpcDefaultRoute">EnablePrivateVpcDefaultRoute</a>: <i>Boolean</i>
    <a href="#enableskippublicroutetableupdate" title="EnableSkipPublicRouteTableUpdate">EnableSkipPublicRouteTableUpdate</a>: <i>Boolean</i>
    <a href="#enablevpcdnsserver" title="EnableVpcDnsServer">EnableVpcDnsServer</a>: <i>Boolean</i>
    <a href="#faultdomain" title="FaultDomain">FaultDomain</a>: <i>String</i>
    <a href="#filteredspokevpcroutes" title="FilteredSpokeVpcRoutes">FilteredSpokeVpcRoutes</a>: <i>String</i>
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#gwsize" title="GwSize">GwSize</a>: <i>String</i>
    <a href="#haavailabilitydomain" title="HaAvailabilityDomain">HaAvailabilityDomain</a>: <i>String</i>
    <a href="#haeip" title="HaEip">HaEip</a>: <i>String</i>
    <a href="#hafaultdomain" title="HaFaultDomain">HaFaultDomain</a>: <i>String</i>
    <a href="#hagwsize" title="HaGwSize">HaGwSize</a>: <i>String</i>
    <a href="#hainsanemodeaz" title="HaInsaneModeAz">HaInsaneModeAz</a>: <i>String</i>
    <a href="#haoobavailabilityzone" title="HaOobAvailabilityZone">HaOobAvailabilityZone</a>: <i>String</i>
    <a href="#haoobmanagementsubnet" title="HaOobManagementSubnet">HaOobManagementSubnet</a>: <i>String</i>
    <a href="#hasubnet" title="HaSubnet">HaSubnet</a>: <i>String</i>
    <a href="#hazone" title="HaZone">HaZone</a>: <i>String</i>
    <a href="#includedadvertisedspokeroutes" title="IncludedAdvertisedSpokeRoutes">IncludedAdvertisedSpokeRoutes</a>: <i>String</i>
    <a href="#insanemode" title="InsaneMode">InsaneMode</a>: <i>Boolean</i>
    <a href="#insanemodeaz" title="InsaneModeAz">InsaneModeAz</a>: <i>String</i>
    <a href="#managetransitgatewayattachment" title="ManageTransitGatewayAttachment">ManageTransitGatewayAttachment</a>: <i>Boolean</i>
    <a href="#monitorexcludelist" title="MonitorExcludeList">MonitorExcludeList</a>: <i>
      - String</i>
    <a href="#oobavailabilityzone" title="OobAvailabilityZone">OobAvailabilityZone</a>: <i>String</i>
    <a href="#oobmanagementsubnet" title="OobManagementSubnet">OobManagementSubnet</a>: <i>String</i>
    <a href="#singleazha" title="SingleAzHa">SingleAzHa</a>: <i>Boolean</i>
    <a href="#singleipsnat" title="SingleIpSnat">SingleIpSnat</a>: <i>Boolean</i>
    <a href="#storagename" title="StorageName">StorageName</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#taglist" title="TagList">TagList</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#transitgw" title="TransitGw">TransitGw</a>: <i>String</i>
    <a href="#tunneldetectiontime" title="TunnelDetectionTime">TunnelDetectionTime</a>: <i>Double</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpcreg" title="VpcReg">VpcReg</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### AccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllocateNewEip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudType

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerManagedKeys

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomizedSpokeVpcRoutes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Eip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableActiveMesh

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoAdvertiseS2cCidrs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEncryptVolume

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableJumboFrame

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMonitorGatewaySubnets

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePrivateOob

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePrivateVpcDefaultRoute

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSkipPublicRouteTableUpdate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVpcDnsServer

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilteredSpokeVpcRoutes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwSize

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaEip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaFaultDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaGwSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaInsaneModeAz

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaOobAvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaOobManagementSubnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaSubnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludedAdvertisedSpokeRoutes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsaneMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsaneModeAz

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageTransitGatewayAttachment

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorExcludeList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OobAvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OobManagementSubnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleAzHa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleIpSnat

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelDetectionTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcReg

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

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

#### CloudInstanceId

Returns the <code>CloudInstanceId</code> value.

#### HaCloudInstanceId

Returns the <code>HaCloudInstanceId</code> value.

#### HaGwName

Returns the <code>HaGwName</code> value.

#### HaPrivateIp

Returns the <code>HaPrivateIp</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrivateIp

Returns the <code>PrivateIp</code> value.

#### SecurityGroupId

Returns the <code>SecurityGroupId</code> value.

