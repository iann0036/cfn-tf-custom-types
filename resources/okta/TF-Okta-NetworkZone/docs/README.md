# TF::Okta::NetworkZone

Creates an Okta Network Zone.

This resource allows you to create and configure an Okta Network Zone.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::NetworkZone",
    "Properties" : {
        "<a href="#dynamiclocations" title="DynamicLocations">DynamicLocations</a>" : <i>[ String, ... ]</i>,
        "<a href="#gateways" title="Gateways">Gateways</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#proxies" title="Proxies">Proxies</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#usage" title="Usage">Usage</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::NetworkZone
Properties:
    <a href="#dynamiclocations" title="DynamicLocations">DynamicLocations</a>: <i>
      - String</i>
    <a href="#gateways" title="Gateways">Gateways</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#proxies" title="Proxies">Proxies</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#usage" title="Usage">Usage</a>: <i>String</i>
</pre>

## Properties

#### DynamicLocations

Array of locations [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
and [ISO-3166-2](https://en.wikipedia.org/wiki/ISO_3166-2). Format code: countryCode OR countryCode-regionCode.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateways

Array of values in CIDR/range form.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the Network Zone Resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxies

Array of values in CIDR/range form. Can not be set if `usage` is set to `"BLOCKLIST"`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the Network Zone - can either be `"IP"` or `"DYNAMIC"` only.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Usage

Usage of the Network Zone - can be either `"POLICY"` or `"BLOCKLIST"`. By default, it is `"POLICY"`.

_Required_: No

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

