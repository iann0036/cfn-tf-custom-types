# Terraform::VCD::NsxvDnat

Provides a vCloud Director DNAT resource for advanced edge gateways (NSX-V). This can be used to create,
modify, and delete destination NATs to map an external IP/port to an internal IP/port. Replaces
[`vcd_dnat`](/docs/providers/vcd/r/dnat.html) resource.

~> **Note:** This resource requires advanced edge gateway. For non-advanced edge gateways please
use the [`vcd_dnat`](/docs/providers/vcd/r/dnat.html) resource.

!> **Warning:** Do not use older [`vcd_dnat`](/docs/providers/vcd/r/dnat.html) resource with this one
because it will change IDs and this resource will not be able to lookup rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::NsxvDnat",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#icmptype" title="IcmpType">IcmpType</a>" : <i>String</i>,
        "<a href="#loggingenabled" title="LoggingEnabled">LoggingEnabled</a>" : <i>Boolean</i>,
        "<a href="#networkname" title="NetworkName">NetworkName</a>" : <i>String</i>,
        "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#originaladdress" title="OriginalAddress">OriginalAddress</a>" : <i>String</i>,
        "<a href="#originalport" title="OriginalPort">OriginalPort</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#ruletag" title="RuleTag">RuleTag</a>" : <i>Double</i>,
        "<a href="#ruletype" title="RuleType">RuleType</a>" : <i>String</i>,
        "<a href="#translatedaddress" title="TranslatedAddress">TranslatedAddress</a>" : <i>String</i>,
        "<a href="#translatedport" title="TranslatedPort">TranslatedPort</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::NsxvDnat
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#icmptype" title="IcmpType">IcmpType</a>: <i>String</i>
    <a href="#loggingenabled" title="LoggingEnabled">LoggingEnabled</a>: <i>Boolean</i>
    <a href="#networkname" title="NetworkName">NetworkName</a>: <i>String</i>
    <a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#originaladdress" title="OriginalAddress">OriginalAddress</a>: <i>String</i>
    <a href="#originalport" title="OriginalPort">OriginalPort</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#ruletag" title="RuleTag">RuleTag</a>: <i>Double</i>
    <a href="#ruletype" title="RuleType">RuleType</a>: <i>String</i>
    <a href="#translatedaddress" title="TranslatedAddress">TranslatedAddress</a>: <i>String</i>
    <a href="#translatedport" title="TranslatedPort">TranslatedPort</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
</pre>

## Properties

#### Description

Free text description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeGateway

The name of the edge gateway on which to apply the DNAT rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Defines if the rule is enabaled. Default `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpType

Only when `protocol` is set to `icmp`. One of `any`,
`address-mask-request`, `address-mask-reply`, `destination-unreachable`, `echo-request`,
`echo-reply`, `parameter-problem`, `redirect`, `router-advertisement`, `router-solicitation`,
`source-quench`, `time-exceeded`, `timestamp-request`, `timestamp-reply`. Default `any`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingEnabled

Defines if the logging for this rule is enabaled. Default `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkName

The name of the network on which to apply the DNAT rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

Type of the network on which to apply the DNAT rule. Possible values
`org` or `ext`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful
when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalAddress

IP address, range or subnet. This address must be the public IP
address of the edge gateway for which you are configuring the DNAT rule. In the packet being
inspected, this IP address or range would be those that appear as the destination IP address of the
packet. These packet destination addresses are the ones translated by this DNAT rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalPort

Select the port or port range that the incoming traffic uses on the
edge gateway to connect to the internal network on which the virtual machines are connected. This
selection is not available when the Protocol is set to `icmp` or `any`. Default `any`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Select the protocol to which the rule applies. One of `tcp`, `udp`,
`icmp`, `any`. Default `any`
protocols, select Any.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleTag

This can be used to specify user-controlled rule tag. If not specified,
it will report rule ID after creation. Must be between 65537-131072.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedAddress

IP address, range or subnet. IP addresses to which destination
addresses on inbound packets will be translated. These addresses are the IP addresses of the one or
more virtual machines for which you are configuring DNAT so that they can receive traffic from the
external network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedPort

Select the port or port range that inbound traffic is connecting
to on the virtual machines on the internal network. These ports are the ones into which the DNAT
rule is translating for the packets inbound to the virtual machines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

