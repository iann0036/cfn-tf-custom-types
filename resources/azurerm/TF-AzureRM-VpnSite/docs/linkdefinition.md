# TF::AzureRM::VpnSite LinkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#providername" title="ProviderName">ProviderName</a>" : <i>String</i>,
    "<a href="#speedinmbps" title="SpeedInMbps">SpeedInMbps</a>" : <i>Double</i>,
    "<a href="#bgp" title="Bgp">Bgp</a>" : <i>[ <a href="bgpdefinition.md">BgpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#providername" title="ProviderName">ProviderName</a>: <i>String</i>
<a href="#speedinmbps" title="SpeedInMbps">SpeedInMbps</a>: <i>Double</i>
<a href="#bgp" title="Bgp">Bgp</a>: <i>
      - <a href="bgpdefinition.md">BgpDefinition</a></i>
</pre>

## Properties

#### Fqdn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpeedInMbps

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bgp

_Required_: No

_Type_: List of <a href="bgpdefinition.md">BgpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

