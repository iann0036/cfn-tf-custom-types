# TF::Thunder::InterfaceManagement

`thunder_interface_management` Provides details about thunder interface management

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::InterfaceManagement",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#duplexity" title="Duplexity">Duplexity</a>" : <i>String</i>,
        "<a href="#flowcontrol" title="FlowControl">FlowControl</a>" : <i>Double</i>,
        "<a href="#speed" title="Speed">Speed</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#accesslist" title="AccessList">AccessList</a>" : <i>[ <a href="accesslistdefinition.md">AccessListDefinition</a>, ... ]</i>,
        "<a href="#broadcastratelimit" title="BroadcastRateLimit">BroadcastRateLimit</a>" : <i>[ <a href="broadcastratelimitdefinition.md">BroadcastRateLimitDefinition</a>, ... ]</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>[ <a href="ipdefinition.md">IpDefinition</a>, ... ]</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>[ <a href="ipv6definition.md">Ipv6Definition</a>, ... ]</i>,
        "<a href="#lldp" title="Lldp">Lldp</a>" : <i>[ <a href="lldpdefinition.md">LldpDefinition</a>, ... ]</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>,
        "<a href="#secondaryip" title="SecondaryIp">SecondaryIp</a>" : <i>[ <a href="secondaryipdefinition.md">SecondaryIpDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::InterfaceManagement
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#duplexity" title="Duplexity">Duplexity</a>: <i>String</i>
    <a href="#flowcontrol" title="FlowControl">FlowControl</a>: <i>Double</i>
    <a href="#speed" title="Speed">Speed</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#accesslist" title="AccessList">AccessList</a>: <i>
      - <a href="accesslistdefinition.md">AccessListDefinition</a></i>
    <a href="#broadcastratelimit" title="BroadcastRateLimit">BroadcastRateLimit</a>: <i>
      - <a href="broadcastratelimitdefinition.md">BroadcastRateLimitDefinition</a></i>
    <a href="#ip" title="Ip">Ip</a>: <i>
      - <a href="ipdefinition.md">IpDefinition</a></i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>
      - <a href="ipv6definition.md">Ipv6Definition</a></i>
    <a href="#lldp" title="Lldp">Lldp</a>: <i>
      - <a href="lldpdefinition.md">LldpDefinition</a></i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
    <a href="#secondaryip" title="SecondaryIp">SecondaryIp</a>: <i>
      - <a href="secondaryipdefinition.md">SecondaryIpDefinition</a></i>
</pre>

## Properties

#### Action

‘enable’: Enable Management Port; ‘disable’: Disable Management Port;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duplexity

‘Full’: Full; ‘Half’: Half; ‘auto’: Auto;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowControl

Enable 802.3x flow control on full duplex port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Speed

‘10’: 10 Mbs/sec; ‘100’: 100 Mbs/sec; ‘1000’: 1 Gb/sec; ‘auto’: Auto Negotiate Speed;  (Interface Speed).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessList

_Required_: No

_Type_: List of <a href="accesslistdefinition.md">AccessListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BroadcastRateLimit

_Required_: No

_Type_: List of <a href="broadcastratelimitdefinition.md">BroadcastRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of <a href="ipdefinition.md">IpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: List of <a href="ipv6definition.md">Ipv6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lldp

_Required_: No

_Type_: List of <a href="lldpdefinition.md">LldpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryIp

_Required_: No

_Type_: List of <a href="secondaryipdefinition.md">SecondaryIpDefinition</a>

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

