# Terraform::AzureRM::VirtualHub Route

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addressprefixes" title="AddressPrefixes">AddressPrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#nexthopipaddress" title="NextHopIpAddress">NextHopIpAddress</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#addressprefixes" title="AddressPrefixes">AddressPrefixes</a>: <i>
      - String</i>
<a href="#nexthopipaddress" title="NextHopIpAddress">NextHopIpAddress</a>: <i>String</i>
</pre>

## Properties

#### AddressPrefixes

A list of Address Prefixes.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopIpAddress

The IP Address that Packets should be forwarded to as the Next Hop.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

