# TF::AzureRM::ApplicationGateway BackendAddressPoolDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fqdns" title="Fqdns">Fqdns</a>" : <i>[ String, ... ]</i>,
    "<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#fqdns" title="Fqdns">Fqdns</a>: <i>
      - String</i>
<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Fqdns

A list of FQDN's which should be part of the Backend Address Pool.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddresses

A list of IP Addresses which should be part of the Backend Address Pool.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Backend Address Pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

