# TF::AzureRM::StorageAccount NetworkRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bypass" title="Bypass">Bypass</a>" : <i>[ String, ... ]</i>,
    "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
    "<a href="#iprules" title="IpRules">IpRules</a>" : <i>[ String, ... ]</i>,
    "<a href="#virtualnetworksubnetids" title="VirtualNetworkSubnetIds">VirtualNetworkSubnetIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#privatelinkaccess" title="PrivateLinkAccess">PrivateLinkAccess</a>" : <i>[ <a href="privatelinkaccessdefinition.md">PrivateLinkAccessDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bypass" title="Bypass">Bypass</a>: <i>
      - String</i>
<a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
<a href="#iprules" title="IpRules">IpRules</a>: <i>
      - String</i>
<a href="#virtualnetworksubnetids" title="VirtualNetworkSubnetIds">VirtualNetworkSubnetIds</a>: <i>
      - String</i>
<a href="#privatelinkaccess" title="PrivateLinkAccess">PrivateLinkAccess</a>: <i>
      - <a href="privatelinkaccessdefinition.md">PrivateLinkAccessDefinition</a></i>
</pre>

## Properties

#### Bypass

Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Valid options are
any combination of `Logging`, `Metrics`, `AzureServices`, or `None`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAction

Specifies the default action of allow or deny when no other rules match. Valid options are `Deny` or `Allow`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRules

List of public IP or IP ranges in CIDR Format. Only IPV4 addresses are allowed. Private IP address ranges (as defined in [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)) are not allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkSubnetIds

A list of resource ids for subnets.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateLinkAccess

_Required_: No

_Type_: List of <a href="privatelinkaccessdefinition.md">PrivateLinkAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

