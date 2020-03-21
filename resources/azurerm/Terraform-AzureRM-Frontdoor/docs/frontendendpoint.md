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

Should the HTTPS protocol be enabled for a custom domain associated with the Front Door?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

Specifies the host name of the `frontend_endpoint`. Must be a domain name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the `frontend_endpoint`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinityEnabled

Whether to allow session affinity on this host. Valid options are `true` or `false` Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinityTtlSeconds

The TTL to use in seconds for session affinity, if applicable. Defaults to `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebApplicationFirewallPolicyLinkId

Defines the Web Application Firewall policy `ID` for each host.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHttpsConfiguration

_Required_: No

_Type_: List of <a href="frontendendpoint-customhttpsconfiguration.md">CustomHttpsConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

