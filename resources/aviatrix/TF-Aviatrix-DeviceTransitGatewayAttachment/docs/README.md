# TF::Aviatrix::DeviceTransitGatewayAttachment

The **aviatrix_device_transit_gateway_attachment** resource allows the creation and management of a device and Aviatrix Transit Gateway attachment for use in CloudWAN.

~> **NOTE:** Before creating this attachment the device must have its WAN interface and IP configured via the `aviatrix_device_interface_config` resource. To avoid attempting to create the attachment before the interface and IP are configured use a `depends_on` meta-argument so that the `aviatrix_device_interface_config` resource is created before the attachment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::DeviceTransitGatewayAttachment",
    "Properties" : {
        "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
        "<a href="#devicebgpasn" title="DeviceBgpAsn">DeviceBgpAsn</a>" : <i>Double</i>,
        "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
        "<a href="#enableeventtriggeredha" title="EnableEventTriggeredHa">EnableEventTriggeredHa</a>" : <i>Boolean</i>,
        "<a href="#enableglobalaccelerator" title="EnableGlobalAccelerator">EnableGlobalAccelerator</a>" : <i>Boolean</i>,
        "<a href="#enablelearnedcidrsapproval" title="EnableLearnedCidrsApproval">EnableLearnedCidrsApproval</a>" : <i>Boolean</i>,
        "<a href="#localtunnelip" title="LocalTunnelIp">LocalTunnelIp</a>" : <i>String</i>,
        "<a href="#manualbgpadvertisedcidrs" title="ManualBgpAdvertisedCidrs">ManualBgpAdvertisedCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#phase1authentication" title="Phase1Authentication">Phase1Authentication</a>" : <i>String</i>,
        "<a href="#phase1dhgroups" title="Phase1DhGroups">Phase1DhGroups</a>" : <i>String</i>,
        "<a href="#phase1encryption" title="Phase1Encryption">Phase1Encryption</a>" : <i>String</i>,
        "<a href="#phase2authentication" title="Phase2Authentication">Phase2Authentication</a>" : <i>String</i>,
        "<a href="#phase2dhgroups" title="Phase2DhGroups">Phase2DhGroups</a>" : <i>String</i>,
        "<a href="#phase2encryption" title="Phase2Encryption">Phase2Encryption</a>" : <i>String</i>,
        "<a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>" : <i>String</i>,
        "<a href="#remotetunnelip" title="RemoteTunnelIp">RemoteTunnelIp</a>" : <i>String</i>,
        "<a href="#transitgatewaybgpasn" title="TransitGatewayBgpAsn">TransitGatewayBgpAsn</a>" : <i>Double</i>,
        "<a href="#transitgatewayname" title="TransitGatewayName">TransitGatewayName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::DeviceTransitGatewayAttachment
Properties:
    <a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
    <a href="#devicebgpasn" title="DeviceBgpAsn">DeviceBgpAsn</a>: <i>Double</i>
    <a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
    <a href="#enableeventtriggeredha" title="EnableEventTriggeredHa">EnableEventTriggeredHa</a>: <i>Boolean</i>
    <a href="#enableglobalaccelerator" title="EnableGlobalAccelerator">EnableGlobalAccelerator</a>: <i>Boolean</i>
    <a href="#enablelearnedcidrsapproval" title="EnableLearnedCidrsApproval">EnableLearnedCidrsApproval</a>: <i>Boolean</i>
    <a href="#localtunnelip" title="LocalTunnelIp">LocalTunnelIp</a>: <i>String</i>
    <a href="#manualbgpadvertisedcidrs" title="ManualBgpAdvertisedCidrs">ManualBgpAdvertisedCidrs</a>: <i>
      - String</i>
    <a href="#phase1authentication" title="Phase1Authentication">Phase1Authentication</a>: <i>String</i>
    <a href="#phase1dhgroups" title="Phase1DhGroups">Phase1DhGroups</a>: <i>String</i>
    <a href="#phase1encryption" title="Phase1Encryption">Phase1Encryption</a>: <i>String</i>
    <a href="#phase2authentication" title="Phase2Authentication">Phase2Authentication</a>: <i>String</i>
    <a href="#phase2dhgroups" title="Phase2DhGroups">Phase2DhGroups</a>: <i>String</i>
    <a href="#phase2encryption" title="Phase2Encryption">Phase2Encryption</a>: <i>String</i>
    <a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>: <i>String</i>
    <a href="#remotetunnelip" title="RemoteTunnelIp">RemoteTunnelIp</a>: <i>String</i>
    <a href="#transitgatewaybgpasn" title="TransitGatewayBgpAsn">TransitGatewayBgpAsn</a>: <i>Double</i>
    <a href="#transitgatewayname" title="TransitGatewayName">TransitGatewayName</a>: <i>String</i>
</pre>

## Properties

#### ConnectionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceBgpAsn

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEventTriggeredHa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableGlobalAccelerator

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLearnedCidrsApproval

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalTunnelIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManualBgpAdvertisedCidrs

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

#### RemoteTunnelIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayBgpAsn

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayName

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

#### VpcId

Returns the <code>VpcId</code> value.

