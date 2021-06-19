# TF::Gridscale::Ipv6

Provides an IPv6 address resource. This can be used to create, modify, and delete IPv6 addresses.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gridscale::Ipv6",
    "Properties" : {
        "<a href="#failover" title="Failover">Failover</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reversedns" title="ReverseDns">ReverseDns</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gridscale::Ipv6
Properties:
    <a href="#failover" title="Failover">Failover</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reversedns" title="ReverseDns">ReverseDns</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Failover

Sets failover mode for this IP. If true, then this IP is no longer available for DHCP and can no longer be related to any server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

List of labels in the format [ "label1", "label2" ].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The human-readable name of the object. It supports the full UTF-8 character set, with a maximum of 64 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseDns

Defines the reverse DNS entry for the IP address (PTR Resource Record).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ChangeTime

Returns the <code>ChangeTime</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### CurrentPrice

Returns the <code>CurrentPrice</code> value.

#### DeleteBlock

Returns the <code>DeleteBlock</code> value.

#### Id

Returns the <code>Id</code> value.

#### Ip

Returns the <code>Ip</code> value.

#### LocationCountry

Returns the <code>LocationCountry</code> value.

#### LocationIata

Returns the <code>LocationIata</code> value.

#### LocationName

Returns the <code>LocationName</code> value.

#### LocationUuid

Returns the <code>LocationUuid</code> value.

#### Prefix

Returns the <code>Prefix</code> value.

#### Status

Returns the <code>Status</code> value.

#### UsageInMinutes

Returns the <code>UsageInMinutes</code> value.

