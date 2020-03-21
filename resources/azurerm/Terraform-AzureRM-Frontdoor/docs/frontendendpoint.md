# Terraform::AzureRM::Frontdoor FrontendEndpoint

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customhttpsprovisioningenabled" title="CustomHttpsProvisioningEnabled">CustomHttpsProvisioningEnabled</a>" : <i>Boolean</i>,
    "<a href="#hostname" title="HostName">HostName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sessionaffinityenabled" title="SessionAffinityEnabled">SessionAffinityEnabled</a>" : <i>Boolean</i>,
    "<a href="#sessionaffinityttlseconds" title="SessionAffinityTtlSeconds">SessionAffinityTtlSeconds</a>" : <i>Double</i>,
    "<a href="#webapplicationfirewallpolicylinkid" title="WebApplicationFirewallPolicyLinkId">WebApplicationFirewallPolicyLinkId</a>" : <i>String</i>,
    "<a href="#customhttpsconfiguration" title="CustomHttpsConfiguration">CustomHttpsConfiguration</a>" : <i>[ <a href="frontendendpoint-customhttpsconfiguration.md">CustomHttpsConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customhttpsprovisioningenabled" title="CustomHttpsProvisioningEnabled">CustomHttpsProvisioningEnabled</a>: <i>Boolean</i>
<a href="#hostname" title="HostName">HostName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sessionaffinityenabled" title="SessionAffinityEnabled">SessionAffinityEnabled</a>: <i>Boolean</i>
<a href="#sessionaffinityttlseconds" title="SessionAffinityTtlSeconds">SessionAffinityTtlSeconds</a>: <i>Double</i>
<a href="#webapplicationfirewallpolicylinkid" title="WebApplicationFirewallPolicyLinkId">WebApplicationFirewallPolicyLinkId</a>: <i>String</i>
<a href="#customhttpsconfiguration" title="CustomHttpsConfiguration">CustomHttpsConfiguration</a>: <i>
      - <a href="frontendendpoint-customhttpsconfiguration.md">CustomHttpsConfiguration</a></i>
</pre>

## Properties

#### CustomHttpsProvisioningEnabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinityEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinityTtlSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebApplicationFirewallPolicyLinkId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHttpsConfiguration

_Required_: No

_Type_: List of <a href="frontendendpoint-customhttpsconfiguration.md">CustomHttpsConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

