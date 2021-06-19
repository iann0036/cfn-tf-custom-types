# TF::Dome9::CloudSecurityGroupRule ServicesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inbound" title="Inbound">Inbound</a>" : <i>[ <a href="inbounddefinition.md">InboundDefinition</a>, ... ]</i>,
    "<a href="#outbound" title="Outbound">Outbound</a>" : <i>[ <a href="outbounddefinition.md">OutboundDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#inbound" title="Inbound">Inbound</a>: <i>
      - <a href="inbounddefinition.md">InboundDefinition</a></i>
<a href="#outbound" title="Outbound">Outbound</a>: <i>
      - <a href="outbounddefinition.md">OutboundDefinition</a></i>
</pre>

## Properties

#### Inbound

_Required_: No

_Type_: List of <a href="inbounddefinition.md">InboundDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outbound

_Required_: No

_Type_: List of <a href="outbounddefinition.md">OutboundDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

