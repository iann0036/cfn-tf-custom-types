# TF::AzureRM::ApplicationGateway HttpListenerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#firewallpolicyid" title="FirewallPolicyId">FirewallPolicyId</a>" : <i>String</i>,
    "<a href="#frontendipconfigurationname" title="FrontendIpConfigurationName">FrontendIpConfigurationName</a>" : <i>String</i>,
    "<a href="#frontendportname" title="FrontendPortName">FrontendPortName</a>" : <i>String</i>,
    "<a href="#hostname" title="HostName">HostName</a>" : <i>String</i>,
    "<a href="#hostnames" title="HostNames">HostNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#requiresni" title="RequireSni">RequireSni</a>" : <i>Boolean</i>,
    "<a href="#sslcertificatename" title="SslCertificateName">SslCertificateName</a>" : <i>String</i>,
    "<a href="#customerrorconfiguration" title="CustomErrorConfiguration">CustomErrorConfiguration</a>" : <i>[ <a href="customerrorconfigurationdefinition.md">CustomErrorConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#firewallpolicyid" title="FirewallPolicyId">FirewallPolicyId</a>: <i>String</i>
<a href="#frontendipconfigurationname" title="FrontendIpConfigurationName">FrontendIpConfigurationName</a>: <i>String</i>
<a href="#frontendportname" title="FrontendPortName">FrontendPortName</a>: <i>String</i>
<a href="#hostname" title="HostName">HostName</a>: <i>String</i>
<a href="#hostnames" title="HostNames">HostNames</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#requiresni" title="RequireSni">RequireSni</a>: <i>Boolean</i>
<a href="#sslcertificatename" title="SslCertificateName">SslCertificateName</a>: <i>String</i>
<a href="#customerrorconfiguration" title="CustomErrorConfiguration">CustomErrorConfiguration</a>: <i>
      - <a href="customerrorconfigurationdefinition.md">CustomErrorConfigurationDefinition</a></i>
</pre>

## Properties

#### FirewallPolicyId

The ID of the Web Application Firewall Policy which should be used as a HTTP Listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendIpConfigurationName

The Name of the Frontend IP Configuration used for this HTTP Listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPortName

The Name of the Frontend Port use for this HTTP Listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

The Hostname which should be used for this HTTP Listener. Setting this value changes Listener Type to 'Multi site'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostNames

A list of Hostname(s) should be used for this HTTP Listener. It allows special wildcard characters.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Name of the HTTP Listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The Protocol to use for this HTTP Listener. Possible values are `Http` and `Https`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireSni

Should Server Name Indication be Required? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificateName

The name of the associated SSL Certificate which should be used for this HTTP Listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomErrorConfiguration

_Required_: No

_Type_: List of <a href="customerrorconfigurationdefinition.md">CustomErrorConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

