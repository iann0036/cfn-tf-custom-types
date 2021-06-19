# TF::Linode::Firewall

Manages a Linode Firewall.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Linode::Firewall",
    "Properties" : {
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#inboundpolicy" title="InboundPolicy">InboundPolicy</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#linodes" title="Linodes">Linodes</a>" : <i>[ Double, ... ]</i>,
        "<a href="#outboundpolicy" title="OutboundPolicy">OutboundPolicy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#inbound" title="Inbound">Inbound</a>" : <i>[ <a href="inbounddefinition.md">InboundDefinition</a>, ... ]</i>,
        "<a href="#outbound" title="Outbound">Outbound</a>" : <i>[ <a href="outbounddefinition.md">OutboundDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Linode::Firewall
Properties:
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#inboundpolicy" title="InboundPolicy">InboundPolicy</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#linodes" title="Linodes">Linodes</a>: <i>
      - Double</i>
    <a href="#outboundpolicy" title="OutboundPolicy">OutboundPolicy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#inbound" title="Inbound">Inbound</a>: <i>
      - <a href="inbounddefinition.md">InboundDefinition</a></i>
    <a href="#outbound" title="Outbound">Outbound</a>: <i>
      - <a href="outbounddefinition.md">OutboundDefinition</a></i>
</pre>

## Properties

#### Disabled

If `true`, the Firewall's rules are not enforced (defaults to `false`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundPolicy

The default behavior for inbound traffic. This setting can be overridden by updating the inbound.action property of the Firewall Rule. (`ACCEPT`, `DROP`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

This Firewall's unique label.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Linodes

A list of IDs of Linodes this Firewall should govern it's network traffic for.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundPolicy

The default behavior for outbound traffic. This setting can be overridden by updating the outbound.action property for an individual Firewall Rule. (`ACCEPT`, `DROP`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inbound

_Required_: No

_Type_: List of <a href="inbounddefinition.md">InboundDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outbound

_Required_: No

_Type_: List of <a href="outbounddefinition.md">OutboundDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Devices

Returns the <code>Devices</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

