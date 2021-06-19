# TF::ECL::NetworkPortV2

Manages a V2 port resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::NetworkPortV2",
    "Properties" : {
        "<a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
        "<a href="#deviceowner" title="DeviceOwner">DeviceOwner</a>" : <i>String</i>,
        "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#nofixedip" title="NoFixedIp">NoFixedIp</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#segmentationid" title="SegmentationId">SegmentationId</a>" : <i>Double</i>,
        "<a href="#segmentationtype" title="SegmentationType">SegmentationType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#allowedaddresspairs" title="AllowedAddressPairs">AllowedAddressPairs</a>" : <i>[ <a href="allowedaddresspairsdefinition.md">AllowedAddressPairsDefinition</a>, ... ]</i>,
        "<a href="#fixedip" title="FixedIp">FixedIp</a>" : <i>[ <a href="fixedipdefinition.md">FixedIpDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::NetworkPortV2
Properties:
    <a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>String</i>
    <a href="#deviceowner" title="DeviceOwner">DeviceOwner</a>: <i>String</i>
    <a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#nofixedip" title="NoFixedIp">NoFixedIp</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#segmentationid" title="SegmentationId">SegmentationId</a>: <i>Double</i>
    <a href="#segmentationtype" title="SegmentationType">SegmentationType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#allowedaddresspairs" title="AllowedAddressPairs">AllowedAddressPairs</a>: <i>
      - <a href="allowedaddresspairsdefinition.md">AllowedAddressPairsDefinition</a></i>
    <a href="#fixedip" title="FixedIp">FixedIp</a>: <i>
      - <a href="fixedipdefinition.md">FixedIpDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdminStateUp

Administrative up/down status for the port
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing port.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Port description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceId

The ID of the device attached to the port. Changing this
creates a new port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceOwner

The device owner of the Port.
Changing this creates a new port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

Specify a specific MAC address for the port. Changing
this creates a new port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the port. Changing this
updates the `name` of an existing port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

The ID of the network to attach the port to.
Changing this creates a new port.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoFixedIp

Create a port with no fixed
IP address. This will also remove any fixed IPs previously set on a port. `true`
is the only valid value for this argument.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 network client.
A network client is needed to create a port. If omitted, the
`region` argument of the provider is used.
Changing this creates a new port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentationId

The segmentation ID used for this port.
User can specify this value only in case segmentation type is "vlan".

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentationType

The segmentation type used for this port.
User can use "vlan" of "flat" as this argument.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Port tags.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The owner of the Port. Required if admin wants
to create a port for another tenant. Changing this creates a new port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedAddressPairs

_Required_: No

_Type_: List of <a href="allowedaddresspairsdefinition.md">AllowedAddressPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedIp

_Required_: No

_Type_: List of <a href="fixedipdefinition.md">FixedIpDefinition</a>

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

#### AllFixedIps

Returns the <code>AllFixedIps</code> value.

#### Id

Returns the <code>Id</code> value.

#### ManagedByService

Returns the <code>ManagedByService</code> value.

#### Status

Returns the <code>Status</code> value.

