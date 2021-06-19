# TF::Aviatrix::TransitGatewayPeering

The **aviatrix_transit_gateway_peering** resource allows the creation and management of peerings between Aviatrix transit gateways.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::TransitGatewayPeering",
    "Properties" : {
        "<a href="#enableinsanemodeencryptionoverinternet" title="EnableInsaneModeEncryptionOverInternet">EnableInsaneModeEncryptionOverInternet</a>" : <i>Boolean</i>,
        "<a href="#enablepeeringoverprivatenetwork" title="EnablePeeringOverPrivateNetwork">EnablePeeringOverPrivateNetwork</a>" : <i>Boolean</i>,
        "<a href="#enablesingletunnelmode" title="EnableSingleTunnelMode">EnableSingleTunnelMode</a>" : <i>Boolean</i>,
        "<a href="#gateway1excludednetworkcidrs" title="Gateway1ExcludedNetworkCidrs">Gateway1ExcludedNetworkCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#gateway1excludedtgwconnections" title="Gateway1ExcludedTgwConnections">Gateway1ExcludedTgwConnections</a>" : <i>[ String, ... ]</i>,
        "<a href="#gateway2excludednetworkcidrs" title="Gateway2ExcludedNetworkCidrs">Gateway2ExcludedNetworkCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#gateway2excludedtgwconnections" title="Gateway2ExcludedTgwConnections">Gateway2ExcludedTgwConnections</a>" : <i>[ String, ... ]</i>,
        "<a href="#prependaspath1" title="PrependAsPath1">PrependAsPath1</a>" : <i>[ String, ... ]</i>,
        "<a href="#prependaspath2" title="PrependAsPath2">PrependAsPath2</a>" : <i>[ String, ... ]</i>,
        "<a href="#transitgatewayname1" title="TransitGatewayName1">TransitGatewayName1</a>" : <i>String</i>,
        "<a href="#transitgatewayname2" title="TransitGatewayName2">TransitGatewayName2</a>" : <i>String</i>,
        "<a href="#tunnelcount" title="TunnelCount">TunnelCount</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::TransitGatewayPeering
Properties:
    <a href="#enableinsanemodeencryptionoverinternet" title="EnableInsaneModeEncryptionOverInternet">EnableInsaneModeEncryptionOverInternet</a>: <i>Boolean</i>
    <a href="#enablepeeringoverprivatenetwork" title="EnablePeeringOverPrivateNetwork">EnablePeeringOverPrivateNetwork</a>: <i>Boolean</i>
    <a href="#enablesingletunnelmode" title="EnableSingleTunnelMode">EnableSingleTunnelMode</a>: <i>Boolean</i>
    <a href="#gateway1excludednetworkcidrs" title="Gateway1ExcludedNetworkCidrs">Gateway1ExcludedNetworkCidrs</a>: <i>
      - String</i>
    <a href="#gateway1excludedtgwconnections" title="Gateway1ExcludedTgwConnections">Gateway1ExcludedTgwConnections</a>: <i>
      - String</i>
    <a href="#gateway2excludednetworkcidrs" title="Gateway2ExcludedNetworkCidrs">Gateway2ExcludedNetworkCidrs</a>: <i>
      - String</i>
    <a href="#gateway2excludedtgwconnections" title="Gateway2ExcludedTgwConnections">Gateway2ExcludedTgwConnections</a>: <i>
      - String</i>
    <a href="#prependaspath1" title="PrependAsPath1">PrependAsPath1</a>: <i>
      - String</i>
    <a href="#prependaspath2" title="PrependAsPath2">PrependAsPath2</a>: <i>
      - String</i>
    <a href="#transitgatewayname1" title="TransitGatewayName1">TransitGatewayName1</a>: <i>String</i>
    <a href="#transitgatewayname2" title="TransitGatewayName2">TransitGatewayName2</a>: <i>String</i>
    <a href="#tunnelcount" title="TunnelCount">TunnelCount</a>: <i>Double</i>
</pre>

## Properties

#### EnableInsaneModeEncryptionOverInternet

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePeeringOverPrivateNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSingleTunnelMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway1ExcludedNetworkCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway1ExcludedTgwConnections

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway2ExcludedNetworkCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway2ExcludedTgwConnections

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrependAsPath1

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrependAsPath2

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayName1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayName2

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelCount

_Required_: No

_Type_: Double

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

