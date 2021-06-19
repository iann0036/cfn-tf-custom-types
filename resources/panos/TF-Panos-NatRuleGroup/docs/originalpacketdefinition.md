# TF::Panos::NatRuleGroup OriginalPacketDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationinterface" title="DestinationInterface">DestinationInterface</a>" : <i>String</i>,
    "<a href="#destinationzone" title="DestinationZone">DestinationZone</a>" : <i>String</i>,
    "<a href="#service" title="Service">Service</a>" : <i>String</i>,
    "<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourcezones" title="SourceZones">SourceZones</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>: <i>
      - String</i>
<a href="#destinationinterface" title="DestinationInterface">DestinationInterface</a>: <i>String</i>
<a href="#destinationzone" title="DestinationZone">DestinationZone</a>: <i>String</i>
<a href="#service" title="Service">Service</a>: <i>String</i>
<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>: <i>
      - String</i>
<a href="#sourcezones" title="SourceZones">SourceZones</a>: <i>
      - String</i>
</pre>

## Properties

#### DestinationAddresses

List of destination address(es).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationInterface

Egress interface from route lookup (default:
`any`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationZone

The destination zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

Service (default: `any`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddresses

List of source address(es).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceZones

The list of source zone(s).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

