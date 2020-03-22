# Terraform::PowerDNS::Zone

Provides a PowerDNS zone.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PowerDNS::Zone",
    "Properties" : {
        "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameservers" title="Nameservers">Nameservers</a>" : <i>[ String, ... ]</i>,
        "<a href="#soaeditapi" title="SoaEditApi">SoaEditApi</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PowerDNS::Zone
Properties:
    <a href="#kind" title="Kind">Kind</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameservers" title="Nameservers">Nameservers</a>: <i>
      - String</i>
    <a href="#soaeditapi" title="SoaEditApi">SoaEditApi</a>: <i>String</i>
</pre>

## Properties

#### Kind

The kind of the zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nameservers

The zone nameservers.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoaEditApi

This should map to one of the [supported API values](https://doc.powerdns.com/authoritative/dnsupdate.html#soa-edit-dnsupdate-settings) *or* in [case you wish to remove the setting](https://doc.powerdns.com/authoritative/domainmetadata.html#soa-edit-api), set this argument as `\"\"` (that will translate to the API value `""`).

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

