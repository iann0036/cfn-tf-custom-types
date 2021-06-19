# TF::Gridscale::Server

Provides a server resource. This can be used to create, modify, and delete servers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gridscale::Server",
    "Properties" : {
        "<a href="#autorecovery" title="AutoRecovery">AutoRecovery</a>" : <i>Boolean</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#cores" title="Cores">Cores</a>" : <i>Double</i>,
        "<a href="#hardwareprofile" title="HardwareProfile">HardwareProfile</a>" : <i>String</i>,
        "<a href="#ipv4" title="Ipv4">Ipv4</a>" : <i>String</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>String</i>,
        "<a href="#isoimage" title="Isoimage">Isoimage</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#power" title="Power">Power</a>" : <i>Boolean</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
        "<a href="#storage" title="Storage">Storage</a>" : <i>[ <a href="storagedefinition.md">StorageDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gridscale::Server
Properties:
    <a href="#autorecovery" title="AutoRecovery">AutoRecovery</a>: <i>Boolean</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#cores" title="Cores">Cores</a>: <i>Double</i>
    <a href="#hardwareprofile" title="HardwareProfile">HardwareProfile</a>: <i>String</i>
    <a href="#ipv4" title="Ipv4">Ipv4</a>: <i>String</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>String</i>
    <a href="#isoimage" title="Isoimage">Isoimage</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#power" title="Power">Power</a>: <i>Boolean</i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
    <a href="#storage" title="Storage">Storage</a>: <i>
      - <a href="storagedefinition.md">StorageDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AutoRecovery

If the server should be auto-started in case of a failure (default=true).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

Defines which Availability-Zone the Server is placed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cores

The number of server cores.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwareProfile

The hardware profile of the Server. Options are default, legacy, nested, cisco_csr, sophos_utm, f5_bigip and q35 at the moment of writing. Check the.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4

The UUID of the IPv4 address of the server. (***NOTE: The server will NOT automatically be connected to the public network; to give it access to the internet, please add server to the public network.).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

The UUID of the IPv6 address of the server. (***NOTE: The server will NOT automatically be connected to the public network; to give it access to the internet, please add server to the public network.).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Isoimage

The UUID of an ISO image in gridscale. The server will automatically boot from the ISO if one was added. The UUIDs of ISO images can be found in [the expert panel](https://my.gridscale.io/Expert/ISOImage).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

List of labels in the format [ "label1", "label2" ].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

The amount of server memory in GB.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The human-readable name of the object. It supports the full UTF-8 character set, with a maximum of 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Power

The power state of the server. Set this to true to will boot the server, false will shut it down.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

_Required_: No

_Type_: List of <a href="storagedefinition.md">StorageDefinition</a>

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

#### ChangeTime

Returns the <code>ChangeTime</code> value.

#### ConsoleToken

Returns the <code>ConsoleToken</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### CurrentPrice

Returns the <code>CurrentPrice</code> value.

#### Id

Returns the <code>Id</code> value.

#### Legacy

Returns the <code>Legacy</code> value.

#### LocationUuid

Returns the <code>LocationUuid</code> value.

#### Status

Returns the <code>Status</code> value.

#### UsageInMinutesCores

Returns the <code>UsageInMinutesCores</code> value.

#### UsageInMinutesMemory

Returns the <code>UsageInMinutesMemory</code> value.

