# TF::AzureRM::ApplicationGateway

Manages an Application Gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::ApplicationGateway",
    "Properties" : {
        "<a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>" : <i>Boolean</i>,
        "<a href="#firewallpolicyid" title="FirewallPolicyId">FirewallPolicyId</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#authenticationcertificate" title="AuthenticationCertificate">AuthenticationCertificate</a>" : <i>[ <a href="authenticationcertificatedefinition.md">AuthenticationCertificateDefinition</a>, ... ]</i>,
        "<a href="#autoscaleconfiguration" title="AutoscaleConfiguration">AutoscaleConfiguration</a>" : <i>[ <a href="autoscaleconfigurationdefinition.md">AutoscaleConfigurationDefinition</a>, ... ]</i>,
        "<a href="#backendaddresspool" title="BackendAddressPool">BackendAddressPool</a>" : <i>[ <a href="backendaddresspooldefinition.md">BackendAddressPoolDefinition</a>, ... ]</i>,
        "<a href="#backendhttpsettings" title="BackendHttpSettings">BackendHttpSettings</a>" : <i>[ <a href="backendhttpsettingsdefinition.md">BackendHttpSettingsDefinition</a>, ... ]</i>,
        "<a href="#customerrorconfiguration" title="CustomErrorConfiguration">CustomErrorConfiguration</a>" : <i>[ <a href="customerrorconfigurationdefinition.md">CustomErrorConfigurationDefinition</a>, ... ]</i>,
        "<a href="#frontendipconfiguration" title="FrontendIpConfiguration">FrontendIpConfiguration</a>" : <i>[ <a href="frontendipconfigurationdefinition.md">FrontendIpConfigurationDefinition</a>, ... ]</i>,
        "<a href="#frontendport" title="FrontendPort">FrontendPort</a>" : <i>[ <a href="frontendportdefinition.md">FrontendPortDefinition</a>, ... ]</i>,
        "<a href="#gatewayipconfiguration" title="GatewayIpConfiguration">GatewayIpConfiguration</a>" : <i>[ <a href="gatewayipconfigurationdefinition.md">GatewayIpConfigurationDefinition</a>, ... ]</i>,
        "<a href="#httplistener" title="HttpListener">HttpListener</a>" : <i>[ <a href="httplistenerdefinition.md">HttpListenerDefinition</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#probe" title="Probe">Probe</a>" : <i>[ <a href="probedefinition.md">ProbeDefinition</a>, ... ]</i>,
        "<a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>" : <i>[ <a href="redirectconfigurationdefinition.md">RedirectConfigurationDefinition</a>, ... ]</i>,
        "<a href="#requestroutingrule" title="RequestRoutingRule">RequestRoutingRule</a>" : <i>[ <a href="requestroutingruledefinition.md">RequestRoutingRuleDefinition</a>, ... ]</i>,
        "<a href="#rewriteruleset" title="RewriteRuleSet">RewriteRuleSet</a>" : <i>[ <a href="rewriterulesetdefinition.md">RewriteRuleSetDefinition</a>, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ <a href="skudefinition.md">SkuDefinition</a>, ... ]</i>,
        "<a href="#sslcertificate" title="SslCertificate">SslCertificate</a>" : <i>[ <a href="sslcertificatedefinition.md">SslCertificateDefinition</a>, ... ]</i>,
        "<a href="#sslpolicy" title="SslPolicy">SslPolicy</a>" : <i>[ <a href="sslpolicydefinition.md">SslPolicyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#trustedrootcertificate" title="TrustedRootCertificate">TrustedRootCertificate</a>" : <i>[ <a href="trustedrootcertificatedefinition.md">TrustedRootCertificateDefinition</a>, ... ]</i>,
        "<a href="#urlpathmap" title="UrlPathMap">UrlPathMap</a>" : <i>[ <a href="urlpathmapdefinition.md">UrlPathMapDefinition</a>, ... ]</i>,
        "<a href="#wafconfiguration" title="WafConfiguration">WafConfiguration</a>" : <i>[ <a href="wafconfigurationdefinition.md">WafConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::ApplicationGateway
Properties:
    <a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>: <i>Boolean</i>
    <a href="#firewallpolicyid" title="FirewallPolicyId">FirewallPolicyId</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#authenticationcertificate" title="AuthenticationCertificate">AuthenticationCertificate</a>: <i>
      - <a href="authenticationcertificatedefinition.md">AuthenticationCertificateDefinition</a></i>
    <a href="#autoscaleconfiguration" title="AutoscaleConfiguration">AutoscaleConfiguration</a>: <i>
      - <a href="autoscaleconfigurationdefinition.md">AutoscaleConfigurationDefinition</a></i>
    <a href="#backendaddresspool" title="BackendAddressPool">BackendAddressPool</a>: <i>
      - <a href="backendaddresspooldefinition.md">BackendAddressPoolDefinition</a></i>
    <a href="#backendhttpsettings" title="BackendHttpSettings">BackendHttpSettings</a>: <i>
      - <a href="backendhttpsettingsdefinition.md">BackendHttpSettingsDefinition</a></i>
    <a href="#customerrorconfiguration" title="CustomErrorConfiguration">CustomErrorConfiguration</a>: <i>
      - <a href="customerrorconfigurationdefinition.md">CustomErrorConfigurationDefinition</a></i>
    <a href="#frontendipconfiguration" title="FrontendIpConfiguration">FrontendIpConfiguration</a>: <i>
      - <a href="frontendipconfigurationdefinition.md">FrontendIpConfigurationDefinition</a></i>
    <a href="#frontendport" title="FrontendPort">FrontendPort</a>: <i>
      - <a href="frontendportdefinition.md">FrontendPortDefinition</a></i>
    <a href="#gatewayipconfiguration" title="GatewayIpConfiguration">GatewayIpConfiguration</a>: <i>
      - <a href="gatewayipconfigurationdefinition.md">GatewayIpConfigurationDefinition</a></i>
    <a href="#httplistener" title="HttpListener">HttpListener</a>: <i>
      - <a href="httplistenerdefinition.md">HttpListenerDefinition</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#probe" title="Probe">Probe</a>: <i>
      - <a href="probedefinition.md">ProbeDefinition</a></i>
    <a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>: <i>
      - <a href="redirectconfigurationdefinition.md">RedirectConfigurationDefinition</a></i>
    <a href="#requestroutingrule" title="RequestRoutingRule">RequestRoutingRule</a>: <i>
      - <a href="requestroutingruledefinition.md">RequestRoutingRuleDefinition</a></i>
    <a href="#rewriteruleset" title="RewriteRuleSet">RewriteRuleSet</a>: <i>
      - <a href="rewriterulesetdefinition.md">RewriteRuleSetDefinition</a></i>
    <a href="#sku" title="Sku">Sku</a>: <i>
      - <a href="skudefinition.md">SkuDefinition</a></i>
    <a href="#sslcertificate" title="SslCertificate">SslCertificate</a>: <i>
      - <a href="sslcertificatedefinition.md">SslCertificateDefinition</a></i>
    <a href="#sslpolicy" title="SslPolicy">SslPolicy</a>: <i>
      - <a href="sslpolicydefinition.md">SslPolicyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#trustedrootcertificate" title="TrustedRootCertificate">TrustedRootCertificate</a>: <i>
      - <a href="trustedrootcertificatedefinition.md">TrustedRootCertificateDefinition</a></i>
    <a href="#urlpathmap" title="UrlPathMap">UrlPathMap</a>: <i>
      - <a href="urlpathmapdefinition.md">UrlPathMapDefinition</a></i>
    <a href="#wafconfiguration" title="WafConfiguration">WafConfiguration</a>: <i>
      - <a href="wafconfigurationdefinition.md">WafConfigurationDefinition</a></i>
</pre>

## Properties

#### EnableHttp2

Is HTTP2 enabled on the application gateway resource? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallPolicyId

The ID of the Web Application Firewall Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The Azure region where the Application Gateway should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Application Gateway. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to the Application Gateway should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

A collection of availability zones to spread the Application Gateway over.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationCertificate

_Required_: No

_Type_: List of <a href="authenticationcertificatedefinition.md">AuthenticationCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleConfiguration

_Required_: No

_Type_: List of <a href="autoscaleconfigurationdefinition.md">AutoscaleConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendAddressPool

_Required_: No

_Type_: List of <a href="backendaddresspooldefinition.md">BackendAddressPoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendHttpSettings

_Required_: No

_Type_: List of <a href="backendhttpsettingsdefinition.md">BackendHttpSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomErrorConfiguration

_Required_: No

_Type_: List of <a href="customerrorconfigurationdefinition.md">CustomErrorConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendIpConfiguration

_Required_: No

_Type_: List of <a href="frontendipconfigurationdefinition.md">FrontendIpConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPort

_Required_: No

_Type_: List of <a href="frontendportdefinition.md">FrontendPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIpConfiguration

_Required_: No

_Type_: List of <a href="gatewayipconfigurationdefinition.md">GatewayIpConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpListener

_Required_: No

_Type_: List of <a href="httplistenerdefinition.md">HttpListenerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Probe

_Required_: No

_Type_: List of <a href="probedefinition.md">ProbeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectConfiguration

_Required_: No

_Type_: List of <a href="redirectconfigurationdefinition.md">RedirectConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestRoutingRule

_Required_: No

_Type_: List of <a href="requestroutingruledefinition.md">RequestRoutingRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteRuleSet

_Required_: No

_Type_: List of <a href="rewriterulesetdefinition.md">RewriteRuleSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: List of <a href="skudefinition.md">SkuDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificate

_Required_: No

_Type_: List of <a href="sslcertificatedefinition.md">SslCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPolicy

_Required_: No

_Type_: List of <a href="sslpolicydefinition.md">SslPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedRootCertificate

_Required_: No

_Type_: List of <a href="trustedrootcertificatedefinition.md">TrustedRootCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlPathMap

_Required_: No

_Type_: List of <a href="urlpathmapdefinition.md">UrlPathMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafConfiguration

_Required_: No

_Type_: List of <a href="wafconfigurationdefinition.md">WafConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

