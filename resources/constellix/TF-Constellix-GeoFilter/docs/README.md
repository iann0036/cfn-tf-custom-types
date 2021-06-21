# TF::Constellix::GeoFilter

Manage Geofilters for A, AAAA, CNAME or ANAME records.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Constellix::GeoFilter",
    "Properties" : {
        "<a href="#asn" title="Asn">Asn</a>" : <i>[ Double, ... ]</i>,
        "<a href="#filterruleslimit" title="FilterRulesLimit">FilterRulesLimit</a>" : <i>Double</i>,
        "<a href="#geoipcontinents" title="GeoipContinents">GeoipContinents</a>" : <i>[ String, ... ]</i>,
        "<a href="#geoipcountries" title="GeoipCountries">GeoipCountries</a>" : <i>[ String, ... ]</i>,
        "<a href="#geoipregions" title="GeoipRegions">GeoipRegions</a>" : <i>[ String, ... ]</i>,
        "<a href="#ipv4" title="Ipv4">Ipv4</a>" : <i>[ String, ... ]</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Constellix::GeoFilter
Properties:
    <a href="#asn" title="Asn">Asn</a>: <i>
      - Double</i>
    <a href="#filterruleslimit" title="FilterRulesLimit">FilterRulesLimit</a>: <i>Double</i>
    <a href="#geoipcontinents" title="GeoipContinents">GeoipContinents</a>: <i>
      - String</i>
    <a href="#geoipcountries" title="GeoipCountries">GeoipCountries</a>: <i>
      - String</i>
    <a href="#geoipregions" title="GeoipRegions">GeoipRegions</a>: <i>
      - String</i>
    <a href="#ipv4" title="Ipv4">Ipv4</a>: <i>
      - String</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Asn

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterRulesLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoipContinents

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoipCountries

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoipRegions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

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
