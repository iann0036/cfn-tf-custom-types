# TF::AzureRM::DataboxEdgeOrder

Manages a Databox Edge Order.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::DataboxEdgeOrder",
    "Properties" : {
        "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#contact" title="Contact">Contact</a>" : <i>[ <a href="contactdefinition.md">ContactDefinition</a>, ... ]</i>,
        "<a href="#shipmentaddress" title="ShipmentAddress">ShipmentAddress</a>" : <i>[ <a href="shipmentaddressdefinition.md">ShipmentAddressDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::DataboxEdgeOrder
Properties:
    <a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#contact" title="Contact">Contact</a>: <i>
      - <a href="contactdefinition.md">ContactDefinition</a></i>
    <a href="#shipmentaddress" title="ShipmentAddress">ShipmentAddress</a>: <i>
      - <a href="shipmentaddressdefinition.md">ShipmentAddressDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DeviceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Contact

_Required_: No

_Type_: List of <a href="contactdefinition.md">ContactDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShipmentAddress

_Required_: No

_Type_: List of <a href="shipmentaddressdefinition.md">ShipmentAddressDefinition</a>

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

#### Name

Returns the <code>Name</code> value.

#### ReturnTracking

Returns the <code>ReturnTracking</code> value.

#### SerialNumber

Returns the <code>SerialNumber</code> value.

#### ShipmentHistory

Returns the <code>ShipmentHistory</code> value.

#### ShipmentTracking

Returns the <code>ShipmentTracking</code> value.

#### Status

Returns the <code>Status</code> value.

