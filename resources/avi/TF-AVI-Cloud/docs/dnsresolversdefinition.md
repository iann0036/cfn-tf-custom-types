# TF::AVI::Cloud DnsResolversDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fixedttl" title="FixedTtl">FixedTtl</a>" : <i>Double</i>,
    "<a href="#minttl" title="MinTtl">MinTtl</a>" : <i>Double</i>,
    "<a href="#resolvername" title="ResolverName">ResolverName</a>" : <i>String</i>,
    "<a href="#usemgmt" title="UseMgmt">UseMgmt</a>" : <i>Boolean</i>,
    "<a href="#nameserverips" title="NameserverIps">NameserverIps</a>" : <i>[ <a href="nameserveripsdefinition.md">NameserverIpsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#fixedttl" title="FixedTtl">FixedTtl</a>: <i>Double</i>
<a href="#minttl" title="MinTtl">MinTtl</a>: <i>Double</i>
<a href="#resolvername" title="ResolverName">ResolverName</a>: <i>String</i>
<a href="#usemgmt" title="UseMgmt">UseMgmt</a>: <i>Boolean</i>
<a href="#nameserverips" title="NameserverIps">NameserverIps</a>: <i>
      - <a href="nameserveripsdefinition.md">NameserverIpsDefinition</a></i>
</pre>

## Properties

#### FixedTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolverName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseMgmt

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameserverIps

_Required_: No

_Type_: List of <a href="nameserveripsdefinition.md">NameserverIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

