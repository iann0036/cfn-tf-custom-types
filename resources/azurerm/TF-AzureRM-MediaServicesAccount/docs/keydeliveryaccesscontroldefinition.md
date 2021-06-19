# TF::AzureRM::MediaServicesAccount KeyDeliveryAccessControlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
    "<a href="#ipallowlist" title="IpAllowList">IpAllowList</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
<a href="#ipallowlist" title="IpAllowList">IpAllowList</a>: <i>
      - String</i>
</pre>

## Properties

#### DefaultAction

The Default Action to use when no rules match from `ip_allow_list`. Possible values are `Allow` and `Deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAllowList

One or more IP Addresses, or CIDR Blocks which should be able to access the Key Delivery.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

