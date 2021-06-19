# TF::AVI::Gslb SitesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#clusteruuid" title="ClusterUuid">ClusterUuid</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#hmshardenabled" title="HmShardEnabled">HmShardEnabled</a>" : <i>Boolean</i>,
    "<a href="#membertype" title="MemberType">MemberType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#ratio" title="Ratio">Ratio</a>" : <i>Double</i>,
    "<a href="#suspendmode" title="SuspendMode">SuspendMode</a>" : <i>Boolean</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#dnsvses" title="DnsVses">DnsVses</a>" : <i>[ <a href="dnsvsesdefinition.md">DnsVsesDefinition</a>, ... ]</i>,
    "<a href="#hmproxies" title="HmProxies">HmProxies</a>" : <i>[ <a href="hmproxiesdefinition.md">HmProxiesDefinition</a>, ... ]</i>,
    "<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>" : <i>[ <a href="ipaddressesdefinition.md">IpAddressesDefinition</a>, ... ]</i>,
    "<a href="#location" title="Location">Location</a>" : <i>[ <a href="locationdefinition.md">LocationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#clusteruuid" title="ClusterUuid">ClusterUuid</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#hmshardenabled" title="HmShardEnabled">HmShardEnabled</a>: <i>Boolean</i>
<a href="#membertype" title="MemberType">MemberType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#ratio" title="Ratio">Ratio</a>: <i>Double</i>
<a href="#suspendmode" title="SuspendMode">SuspendMode</a>: <i>Boolean</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#dnsvses" title="DnsVses">DnsVses</a>: <i>
      - <a href="dnsvsesdefinition.md">DnsVsesDefinition</a></i>
<a href="#hmproxies" title="HmProxies">HmProxies</a>: <i>
      - <a href="hmproxiesdefinition.md">HmProxiesDefinition</a></i>
<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>: <i>
      - <a href="ipaddressesdefinition.md">IpAddressesDefinition</a></i>
<a href="#location" title="Location">Location</a>: <i>
      - <a href="locationdefinition.md">LocationDefinition</a></i>
</pre>

## Properties

#### Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterUuid

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HmShardEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ratio

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuspendMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsVses

_Required_: No

_Type_: List of <a href="dnsvsesdefinition.md">DnsVsesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HmProxies

_Required_: No

_Type_: List of <a href="hmproxiesdefinition.md">HmProxiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddresses

_Required_: No

_Type_: List of <a href="ipaddressesdefinition.md">IpAddressesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: List of <a href="locationdefinition.md">LocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

