# TF::Panos::DosProtectionProfile

Manages DOS protection security profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::DosProtectionProfile",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#enablesessionsprotections" title="EnableSessionsProtections">EnableSessionsProtections</a>" : <i>Boolean</i>,
        "<a href="#maxconcurrentsessions" title="MaxConcurrentSessions">MaxConcurrentSessions</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#icmp" title="Icmp">Icmp</a>" : <i>[ <a href="icmpdefinition.md">IcmpDefinition</a>, ... ]</i>,
        "<a href="#icmpv6" title="Icmpv6">Icmpv6</a>" : <i>[ <a href="icmpv6definition.md">Icmpv6Definition</a>, ... ]</i>,
        "<a href="#other" title="Other">Other</a>" : <i>[ <a href="otherdefinition.md">OtherDefinition</a>, ... ]</i>,
        "<a href="#syn" title="Syn">Syn</a>" : <i>[ <a href="syndefinition.md">SynDefinition</a>, ... ]</i>,
        "<a href="#udp" title="Udp">Udp</a>" : <i>[ <a href="udpdefinition.md">UdpDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::DosProtectionProfile
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#enablesessionsprotections" title="EnableSessionsProtections">EnableSessionsProtections</a>: <i>Boolean</i>
    <a href="#maxconcurrentsessions" title="MaxConcurrentSessions">MaxConcurrentSessions</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#icmp" title="Icmp">Icmp</a>: <i>
      - <a href="icmpdefinition.md">IcmpDefinition</a></i>
    <a href="#icmpv6" title="Icmpv6">Icmpv6</a>: <i>
      - <a href="icmpv6definition.md">Icmpv6Definition</a></i>
    <a href="#other" title="Other">Other</a>: <i>
      - <a href="otherdefinition.md">OtherDefinition</a></i>
    <a href="#syn" title="Syn">Syn</a>: <i>
      - <a href="syndefinition.md">SynDefinition</a></i>
    <a href="#udp" title="Udp">Udp</a>: <i>
      - <a href="udpdefinition.md">UdpDefinition</a></i>
</pre>

## Properties

#### Description

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

The device group location (default: `shared`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSessionsProtections

Enable sessions protections.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentSessions

Max concurrent sessions.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The profile type.  Valid values are `aggregate` (default)
or `classified`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys location (default: `vsys1`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmp

_Required_: No

_Type_: List of <a href="icmpdefinition.md">IcmpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmpv6

_Required_: No

_Type_: List of <a href="icmpv6definition.md">Icmpv6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Other

_Required_: No

_Type_: List of <a href="otherdefinition.md">OtherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Syn

_Required_: No

_Type_: List of <a href="syndefinition.md">SynDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Udp

_Required_: No

_Type_: List of <a href="udpdefinition.md">UdpDefinition</a>

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

