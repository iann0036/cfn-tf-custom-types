# TF::AzureRM::VpnGatewayConnection VpnLinkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bandwidthmbps" title="BandwidthMbps">BandwidthMbps</a>" : <i>Double</i>,
    "<a href="#bgpenabled" title="BgpEnabled">BgpEnabled</a>" : <i>Boolean</i>,
    "<a href="#localazureipaddressenabled" title="LocalAzureIpAddressEnabled">LocalAzureIpAddressEnabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#policybasedtrafficselectorenabled" title="PolicyBasedTrafficSelectorEnabled">PolicyBasedTrafficSelectorEnabled</a>" : <i>Boolean</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#ratelimitenabled" title="RatelimitEnabled">RatelimitEnabled</a>" : <i>Boolean</i>,
    "<a href="#routeweight" title="RouteWeight">RouteWeight</a>" : <i>Double</i>,
    "<a href="#sharedkey" title="SharedKey">SharedKey</a>" : <i>String</i>,
    "<a href="#vpnsitelinkid" title="VpnSiteLinkId">VpnSiteLinkId</a>" : <i>String</i>,
    "<a href="#ipsecpolicy" title="IpsecPolicy">IpsecPolicy</a>" : <i>[ <a href="ipsecpolicydefinition.md">IpsecPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bandwidthmbps" title="BandwidthMbps">BandwidthMbps</a>: <i>Double</i>
<a href="#bgpenabled" title="BgpEnabled">BgpEnabled</a>: <i>Boolean</i>
<a href="#localazureipaddressenabled" title="LocalAzureIpAddressEnabled">LocalAzureIpAddressEnabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#policybasedtrafficselectorenabled" title="PolicyBasedTrafficSelectorEnabled">PolicyBasedTrafficSelectorEnabled</a>: <i>Boolean</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#ratelimitenabled" title="RatelimitEnabled">RatelimitEnabled</a>: <i>Boolean</i>
<a href="#routeweight" title="RouteWeight">RouteWeight</a>: <i>Double</i>
<a href="#sharedkey" title="SharedKey">SharedKey</a>: <i>String</i>
<a href="#vpnsitelinkid" title="VpnSiteLinkId">VpnSiteLinkId</a>: <i>String</i>
<a href="#ipsecpolicy" title="IpsecPolicy">IpsecPolicy</a>: <i>
      - <a href="ipsecpolicydefinition.md">IpsecPolicyDefinition</a></i>
</pre>

## Properties

#### BandwidthMbps

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAzureIpAddressEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyBasedTrafficSelectorEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RatelimitEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteWeight

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnSiteLinkId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPolicy

_Required_: No

_Type_: List of <a href="ipsecpolicydefinition.md">IpsecPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

