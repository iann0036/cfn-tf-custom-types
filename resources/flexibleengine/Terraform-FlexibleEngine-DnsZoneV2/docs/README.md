# Terraform::FlexibleEngine::DnsZoneV2

Manages a DNS zone in the FlexibleEngine DNS Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::DnsZoneV2",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>" : <i>[ <a href="valuespecs.md">ValueSpecs</a>, ... ]</i>,
        "<a href="#zonetype" title="ZoneType">ZoneType</a>" : <i>String</i>,
        "<a href="#router" title="Router">Router</a>" : <i>[ <a href="router.md">Router</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::DnsZoneV2
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>: <i>
      - <a href="valuespecs.md">ValueSpecs</a></i>
    <a href="#zonetype" title="ZoneType">ZoneType</a>: <i>String</i>
    <a href="#router" title="Router">Router</a>: <i>
      - <a href="router.md">Router</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Description

A description of the zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

The email contact for the zone record.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the zone. Note the `.` at the end of the name.
Changing this creates a new DNS zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new DNS zone. Changing this creates a new DNS zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

The time to live (TTL) of the zone.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueSpecs

Map of additional options. Changing this creates a
new DNS zone.

_Required_: No

_Type_: List of <a href="valuespecs.md">ValueSpecs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneType

The type of zone. Can either be `public` or `private`.
Changing this creates a new DNS zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Router

_Required_: No

_Type_: List of <a href="router.md">Router</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Masters

Returns the <code>Masters</code> value.

