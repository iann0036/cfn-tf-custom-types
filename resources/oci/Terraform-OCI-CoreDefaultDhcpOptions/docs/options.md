# Terraform::OCI::CoreDefaultDhcpOptions Options

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customdnsservers" title="CustomDnsServers">CustomDnsServers</a>" : <i>[ String, ... ]</i>,
    "<a href="#searchdomainnames" title="SearchDomainNames">SearchDomainNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#servertype" title="ServerType">ServerType</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#customdnsservers" title="CustomDnsServers">CustomDnsServers</a>: <i>
      - String</i>
<a href="#searchdomainnames" title="SearchDomainNames">SearchDomainNames</a>: <i>
      - String</i>
<a href="#servertype" title="ServerType">ServerType</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CustomDnsServers

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchDomainNames

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

