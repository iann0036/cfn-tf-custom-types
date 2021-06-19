# TF::AVI::Applicationprofile FilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#devicesref" title="DevicesRef">DevicesRef</a>" : <i>String</i>,
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#ipaddrsref" title="IpAddrsRef">IpAddrsRef</a>" : <i>String</i>,
    "<a href="#level" title="Level">Level</a>" : <i>String</i>,
    "<a href="#match" title="Match">Match</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#useragent" title="UserAgent">UserAgent</a>" : <i>[ String, ... ]</i>,
    "<a href="#ipaddrprefixes" title="IpAddrPrefixes">IpAddrPrefixes</a>" : <i>[ <a href="ipaddrprefixesdefinition.md">IpAddrPrefixesDefinition</a>, ... ]</i>,
    "<a href="#ipaddrranges" title="IpAddrRanges">IpAddrRanges</a>" : <i>[ <a href="ipaddrrangesdefinition.md">IpAddrRangesDefinition</a>, ... ]</i>,
    "<a href="#ipaddrs" title="IpAddrs">IpAddrs</a>" : <i>[ <a href="ipaddrsdefinition.md">IpAddrsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#devicesref" title="DevicesRef">DevicesRef</a>: <i>String</i>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#ipaddrsref" title="IpAddrsRef">IpAddrsRef</a>: <i>String</i>
<a href="#level" title="Level">Level</a>: <i>String</i>
<a href="#match" title="Match">Match</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#useragent" title="UserAgent">UserAgent</a>: <i>
      - String</i>
<a href="#ipaddrprefixes" title="IpAddrPrefixes">IpAddrPrefixes</a>: <i>
      - <a href="ipaddrprefixesdefinition.md">IpAddrPrefixesDefinition</a></i>
<a href="#ipaddrranges" title="IpAddrRanges">IpAddrRanges</a>: <i>
      - <a href="ipaddrrangesdefinition.md">IpAddrRangesDefinition</a></i>
<a href="#ipaddrs" title="IpAddrs">IpAddrs</a>: <i>
      - <a href="ipaddrsdefinition.md">IpAddrsDefinition</a></i>
</pre>

## Properties

#### DevicesRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddrsRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAgent

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddrPrefixes

_Required_: No

_Type_: List of <a href="ipaddrprefixesdefinition.md">IpAddrPrefixesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddrRanges

_Required_: No

_Type_: List of <a href="ipaddrrangesdefinition.md">IpAddrRangesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddrs

_Required_: No

_Type_: List of <a href="ipaddrsdefinition.md">IpAddrsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

