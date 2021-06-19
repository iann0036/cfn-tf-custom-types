# TF::AzureRM::VirtualHubConnection StaticVnetRouteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addressprefixes" title="AddressPrefixes">AddressPrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nexthopipaddress" title="NextHopIpAddress">NextHopIpAddress</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#addressprefixes" title="AddressPrefixes">AddressPrefixes</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nexthopipaddress" title="NextHopIpAddress">NextHopIpAddress</a>: <i>String</i>
</pre>

## Properties

#### AddressPrefixes

A list of CIDR Ranges which should be used as Address Prefixes.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name which should be used for this Static Route.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopIpAddress

The IP Address which should be used for the Next Hop.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

