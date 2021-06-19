# TF::AVI::Gslb ClientIpAddrGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#addrs" title="Addrs">Addrs</a>" : <i>[ <a href="addrsdefinition.md">AddrsDefinition</a>, ... ]</i>,
    "<a href="#prefixes" title="Prefixes">Prefixes</a>" : <i>[ <a href="prefixesdefinition.md">PrefixesDefinition</a>, ... ]</i>,
    "<a href="#ranges" title="Ranges">Ranges</a>" : <i>[ <a href="rangesdefinition.md">RangesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#addrs" title="Addrs">Addrs</a>: <i>
      - <a href="addrsdefinition.md">AddrsDefinition</a></i>
<a href="#prefixes" title="Prefixes">Prefixes</a>: <i>
      - <a href="prefixesdefinition.md">PrefixesDefinition</a></i>
<a href="#ranges" title="Ranges">Ranges</a>: <i>
      - <a href="rangesdefinition.md">RangesDefinition</a></i>
</pre>

## Properties

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Addrs

_Required_: No

_Type_: List of <a href="addrsdefinition.md">AddrsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefixes

_Required_: No

_Type_: List of <a href="prefixesdefinition.md">PrefixesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ranges

_Required_: No

_Type_: List of <a href="rangesdefinition.md">RangesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

