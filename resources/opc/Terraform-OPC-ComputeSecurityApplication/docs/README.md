# Terraform::OPC::ComputeSecurityApplication

The ``opc_compute_security_application`` resource creates and manages a security application in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::ComputeSecurityApplication",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dport" title="Dport">Dport</a>" : <i>String</i>,
        "<a href="#icmpcode" title="Icmpcode">Icmpcode</a>" : <i>String</i>,
        "<a href="#icmptype" title="Icmptype">Icmptype</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::ComputeSecurityApplication
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dport" title="Dport">Dport</a>: <i>String</i>
    <a href="#icmpcode" title="Icmpcode">Icmpcode</a>: <i>String</i>
    <a href="#icmptype" title="Icmptype">Icmptype</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dport

The port, or range of ports, to enable for this application, e.g `8080`, `6000-7000`. This must be set if the `protocol` is set to `tcp` or `udp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmpcode

The ICMP code to enable for this application, if the `protocol` is `icmp`. Must be one of
`admin`, `df`, `host`, `network`, `port` or `protocol`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmptype

The ICMP type to enable for this application, if the `protocol` is `icmp`. Must be one of
`echo`, `reply`, `ttl`, `traceroute`, `unreachable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The unique (within the identity domain) name of the application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol to enable for this application. Must be one of
`tcp`, `udp`, `ah`, `esp`, `icmp`, `icmpv6`, `igmp`, `ipip`, `gre`, `mplsip`, `ospf`, `pim`, `rdp`, `sctp` or `all`.

_Required_: Yes

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

