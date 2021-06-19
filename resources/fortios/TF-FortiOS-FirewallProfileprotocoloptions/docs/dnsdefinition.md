# TF::FortiOS::FirewallProfileprotocoloptions DnsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ports" title="Ports">Ports</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ports" title="Ports">Ports</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### Ports

Ports to scan for content (1 - 65535, default = 53).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable the active status of scanning for this protocol. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

