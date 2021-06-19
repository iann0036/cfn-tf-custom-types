# TF::AzureRM::HpcCache DnsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#searchdomain" title="SearchDomain">SearchDomain</a>" : <i>String</i>,
    "<a href="#servers" title="Servers">Servers</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#searchdomain" title="SearchDomain">SearchDomain</a>: <i>String</i>
<a href="#servers" title="Servers">Servers</a>: <i>
      - String</i>
</pre>

## Properties

#### SearchDomain

The DNS search domain for the HPC Cache.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servers

A list of DNS servers for the HPC Cache. At most three IP(s) are allowed to set.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

