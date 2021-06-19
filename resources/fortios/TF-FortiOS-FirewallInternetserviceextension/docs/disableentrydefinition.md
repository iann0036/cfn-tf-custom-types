# TF::FortiOS::FirewallInternetserviceextension DisableEntryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>Double</i>,
    "<a href="#iprange" title="IpRange">IpRange</a>" : <i>[ <a href="iprangedefinition.md">IpRangeDefinition</a>, ... ]</i>,
    "<a href="#portrange" title="PortRange">PortRange</a>" : <i>[ <a href="portrangedefinition.md">PortRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>Double</i>
<a href="#iprange" title="IpRange">IpRange</a>: <i>
      - <a href="iprangedefinition.md">IpRangeDefinition</a></i>
<a href="#portrange" title="PortRange">PortRange</a>: <i>
      - <a href="portrangedefinition.md">PortRangeDefinition</a></i>
</pre>

## Properties

#### Id

Disable entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Integer value for the TCP/IP port (0 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Integer value for the protocol type as defined by IANA (0 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRange

_Required_: No

_Type_: List of <a href="iprangedefinition.md">IpRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortRange

_Required_: No

_Type_: List of <a href="portrangedefinition.md">PortRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

