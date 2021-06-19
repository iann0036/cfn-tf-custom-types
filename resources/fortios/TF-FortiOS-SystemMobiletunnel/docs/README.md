# TF::FortiOS::SystemMobiletunnel

Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemMobiletunnel",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#hashalgorithm" title="HashAlgorithm">HashAlgorithm</a>" : <i>String</i>,
        "<a href="#homeaddress" title="HomeAddress">HomeAddress</a>" : <i>String</i>,
        "<a href="#homeagent" title="HomeAgent">HomeAgent</a>" : <i>String</i>,
        "<a href="#lifetime" title="Lifetime">Lifetime</a>" : <i>Double</i>,
        "<a href="#nmhaekey" title="NMhaeKey">NMhaeKey</a>" : <i>String</i>,
        "<a href="#nmhaekeytype" title="NMhaeKeyType">NMhaeKeyType</a>" : <i>String</i>,
        "<a href="#nmhaespi" title="NMhaeSpi">NMhaeSpi</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reginterval" title="RegInterval">RegInterval</a>" : <i>Double</i>,
        "<a href="#regretry" title="RegRetry">RegRetry</a>" : <i>Double</i>,
        "<a href="#renewinterval" title="RenewInterval">RenewInterval</a>" : <i>Double</i>,
        "<a href="#roaminginterface" title="RoamingInterface">RoamingInterface</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tunnelmode" title="TunnelMode">TunnelMode</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemMobiletunnel
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#hashalgorithm" title="HashAlgorithm">HashAlgorithm</a>: <i>String</i>
    <a href="#homeaddress" title="HomeAddress">HomeAddress</a>: <i>String</i>
    <a href="#homeagent" title="HomeAgent">HomeAgent</a>: <i>String</i>
    <a href="#lifetime" title="Lifetime">Lifetime</a>: <i>Double</i>
    <a href="#nmhaekey" title="NMhaeKey">NMhaeKey</a>: <i>String</i>
    <a href="#nmhaekeytype" title="NMhaeKeyType">NMhaeKeyType</a>: <i>String</i>
    <a href="#nmhaespi" title="NMhaeSpi">NMhaeSpi</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reginterval" title="RegInterval">RegInterval</a>: <i>Double</i>
    <a href="#regretry" title="RegRetry">RegRetry</a>: <i>Double</i>
    <a href="#renewinterval" title="RenewInterval">RenewInterval</a>: <i>Double</i>
    <a href="#roaminginterface" title="RoamingInterface">RoamingInterface</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tunnelmode" title="TunnelMode">TunnelMode</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashAlgorithm

Hash Algorithm (Keyed MD5). Valid values: `hmac-md5`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomeAddress

Home IP address (Format: xxx.xxx.xxx.xxx).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomeAgent

IPv4 address of the NEMO HA (Format: xxx.xxx.xxx.xxx).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifetime

NMMO HA registration request lifetime (180 - 65535 sec, default = 65535).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NMhaeKey

NEMO authentication key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NMhaeKeyType

NEMO authentication key type (ascii or base64). Valid values: `ascii`, `base64`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NMhaeSpi

NEMO authentication SPI (default: 256).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Tunnel name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegInterval

NMMO HA registration interval (5 - 300, default = 5).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegRetry

Maximum number of NMMO HA registration retries (1 to 30, default = 3).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenewInterval

Time before lifetime expiraton to send NMMO HA re-registration (5 - 60, default = 60).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoamingInterface

Select the associated interface name from available options.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this mobile tunnel. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelMode

NEMO tunnnel mode (GRE tunnel). Valid values: `gre`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

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

