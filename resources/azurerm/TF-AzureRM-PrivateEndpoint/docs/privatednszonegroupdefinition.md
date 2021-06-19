# TF::AzureRM::PrivateEndpoint PrivateDnsZoneGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#privatednszoneids" title="PrivateDnsZoneIds">PrivateDnsZoneIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#privatednszoneids" title="PrivateDnsZoneIds">PrivateDnsZoneIds</a>: <i>
      - String</i>
</pre>

## Properties

#### Name

Specifies the Name of the Private DNS Zone Group. Changing this forces a new `private_dns_zone_group` resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateDnsZoneIds

Specifies the list of Private DNS Zones to include within the `private_dns_zone_group`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

