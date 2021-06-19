# TF::AzureRM::ContainerGroup DnsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nameservers" title="Nameservers">Nameservers</a>" : <i>[ String, ... ]</i>,
    "<a href="#options" title="Options">Options</a>" : <i>[ String, ... ]</i>,
    "<a href="#searchdomains" title="SearchDomains">SearchDomains</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nameservers" title="Nameservers">Nameservers</a>: <i>
      - String</i>
<a href="#options" title="Options">Options</a>: <i>
      - String</i>
<a href="#searchdomains" title="SearchDomains">SearchDomains</a>: <i>
      - String</i>
</pre>

## Properties

#### Nameservers

A list of nameservers the containers will search out to resolve requests.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

A list of [resolver configuration options](https://man7.org/linux/man-pages/man5/resolv.conf.5.html).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchDomains

A list of search domains that DNS requests will search along.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

