# TF::Packet::SpotMarketRequest

Provides an Equinix Metal Spot Market Request resource to allow you to
manage spot market requests on your account. For more detail on Spot Market, see [this article in Equinix Metal documentation](https://metal.equinix.com/developers/docs/deploy/spot-market/).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Packet::SpotMarketRequest",
    "Properties" : {
        "<a href="#devicesmax" title="DevicesMax">DevicesMax</a>" : <i>Double</i>,
        "<a href="#devicesmin" title="DevicesMin">DevicesMin</a>" : <i>Double</i>,
        "<a href="#facilities" title="Facilities">Facilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxbidprice" title="MaxBidPrice">MaxBidPrice</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#waitfordevices" title="WaitForDevices">WaitForDevices</a>" : <i>Boolean</i>,
        "<a href="#instanceparameters" title="InstanceParameters">InstanceParameters</a>" : <i>[ <a href="instanceparametersdefinition.md">InstanceParametersDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Packet::SpotMarketRequest
Properties:
    <a href="#devicesmax" title="DevicesMax">DevicesMax</a>: <i>Double</i>
    <a href="#devicesmin" title="DevicesMin">DevicesMin</a>: <i>Double</i>
    <a href="#facilities" title="Facilities">Facilities</a>: <i>
      - String</i>
    <a href="#maxbidprice" title="MaxBidPrice">MaxBidPrice</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#waitfordevices" title="WaitForDevices">WaitForDevices</a>: <i>Boolean</i>
    <a href="#instanceparameters" title="InstanceParameters">InstanceParameters</a>: <i>
      - <a href="instanceparametersdefinition.md">InstanceParametersDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DevicesMax

Maximum number devices to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DevicesMin

Miniumum number devices to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facilities

Facility IDs where devices should be created.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBidPrice

Maximum price user is willing to pay per hour per device.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Project ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForDevices

On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceParameters

_Required_: No

_Type_: List of <a href="instanceparametersdefinition.md">InstanceParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

