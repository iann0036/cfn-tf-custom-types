# Terraform::AzureRM::ApplicationGateway

Manages an Application Gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ApplicationGateway",
    "Properties" : {
        "<a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#authenticationcertificate" title="AuthenticationCertificate">AuthenticationCertificate</a>" : <i>[ <a href="authenticationcertificate.md">AuthenticationCertificate</a>, ... ]</i>,
        "<a href="#autoscaleconfiguration" title="AutoscaleConfiguration">AutoscaleConfiguration</a>" : <i>[ <a href="autoscaleconfiguration.md">AutoscaleConfiguration</a>, ... ]</i>,
        "<a href="#backendaddresspool" title="BackendAddressPool">BackendAddressPool</a>" : <i>[ <a href="backendaddresspool.md">BackendAddressPool</a>, ... ]</i>,
        "<a href="#backendhttpsettings" title="BackendHttpSettings">BackendHttpSettings</a>" : <i>[ <a href="backendhttpsettings.md">BackendHttpSettings</a>, ... ]</i>,
        "<a href="#customerrorconfiguration" title="CustomErrorConfiguration">CustomErrorConfiguration</a>" : <i>[ <a href="customerrorconfiguration.md">CustomErrorConfiguration</a>, ... ]</i>,
        "<a href="#frontendipconfiguration" title="FrontendIpConfiguration">FrontendIpConfiguration</a>" : <i>[ <a href="frontendipconfiguration.md">FrontendIpConfiguration</a>, ... ]</i>,
        "<a href="#frontendport" title="FrontendPort">FrontendPort</a>" : <i>[ <a href="frontendport.md">FrontendPort</a>, ... ]</i>,
        "<a href="#gatewayipconfiguration" title="GatewayIpConfiguration">GatewayIpConfiguration</a>" : <i>[ <a href="gatewayipconfiguration.md">GatewayIpConfiguration</a>, ... ]</i>,
        "<a href="#httplistener" title="HttpListener">HttpListener</a>" : <i>[ <a href="httplistener.md">HttpListener</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#probe" title="Probe">Probe</a>" : <i>[ <a href="probe.md">Probe</a>, ... ]</i>,
        "<a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>" : <i>[ <a href="redirectconfiguration.md">RedirectConfiguration</a>, ... ]</i>,
        "<a href="#requestroutingrule" title="RequestRoutingRule">RequestRoutingRule</a>" : <i>[ <a href="requestroutingrule.md">RequestRoutingRule</a>, ... ]</i>,
        "<a href="#rewriteruleset" title="RewriteRuleSet">RewriteRuleSet</a>" : <i>[ <a href="rewriteruleset.md">RewriteRuleSet</a>, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ <a href="sku.md">Sku</a>, ... ]</i>,
        "<a href="#sslcertificate" title="SslCertificate">SslCertificate</a>" : <i>[ <a href="sslcertificate.md">SslCertificate</a>, ... ]</i>,
        "<a href="#sslpolicy" title="SslPolicy">SslPolicy</a>" : <i>[ <a href="sslpolicy.md">SslPolicy</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#trustedrootcertificate" title="TrustedRootCertificate">TrustedRootCertificate</a>" : <i>[ <a href="trustedrootcertificate.md">TrustedRootCertificate</a>, ... ]</i>,
        "<a href="#urlpathmap" title="UrlPathMap">UrlPathMap</a>" : <i>[ <a href="urlpathmap.md">UrlPathMap</a>, ... ]</i>,
        "<a href="#wafconfiguration" title="WafConfiguration">WafConfiguration</a>" : <i>[ <a href="wafconfiguration.md">WafConfiguration</a>, ... ]</i>,
        "<a href="#connectiondraining" title="ConnectionDraining">ConnectionDraining</a>" : <i>[ <a href="connectiondraining.md">ConnectionDraining</a>, ... ]</i>,
        "<a href="#match" title="Match">Match</a>" : <i>[ <a href="match.md">Match</a>, ... ]</i>,
        "<a href="#rewriterule" title="RewriteRule">RewriteRule</a>" : <i>[ <a href="rewriterule.md">RewriteRule</a>, ... ]</i>,
        "<a href="#pathrule" title="PathRule">PathRule</a>" : <i>[ <a href="pathrule.md">PathRule</a>, ... ]</i>,
        "<a href="#disabledrulegroup" title="DisabledRuleGroup">DisabledRuleGroup</a>" : <i>[ <a href="disabledrulegroup.md">DisabledRuleGroup</a>, ... ]</i>,
        "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ <a href="exclusion.md">Exclusion</a>, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="condition.md">Condition</a>, ... ]</i>,
        "<a href="#requestheaderconfiguration" title="RequestHeaderConfiguration">RequestHeaderConfiguration</a>" : <i>[ <a href="requestheaderconfiguration.md">RequestHeaderConfiguration</a>, ... ]</i>,
        "<a href="#responseheaderconfiguration" title="ResponseHeaderConfiguration">ResponseHeaderConfiguration</a>" : <i>[ <a href="responseheaderconfiguration.md">ResponseHeaderConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ApplicationGateway
Properties:
    <a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#authenticationcertificate" title="AuthenticationCertificate">AuthenticationCertificate</a>: <i>
      - <a href="authenticationcertificate.md">AuthenticationCertificate</a></i>
    <a href="#autoscaleconfiguration" title="AutoscaleConfiguration">AutoscaleConfiguration</a>: <i>
      - <a href="autoscaleconfiguration.md">AutoscaleConfiguration</a></i>
    <a href="#backendaddresspool" title="BackendAddressPool">BackendAddressPool</a>: <i>
      - <a href="backendaddresspool.md">BackendAddressPool</a></i>
    <a href="#backendhttpsettings" title="BackendHttpSettings">BackendHttpSettings</a>: <i>
      - <a href="backendhttpsettings.md">BackendHttpSettings</a></i>
    <a href="#customerrorconfiguration" title="CustomErrorConfiguration">CustomErrorConfiguration</a>: <i>
      - <a href="customerrorconfiguration.md">CustomErrorConfiguration</a></i>
    <a href="#frontendipconfiguration" title="FrontendIpConfiguration">FrontendIpConfiguration</a>: <i>
      - <a href="frontendipconfiguration.md">FrontendIpConfiguration</a></i>
    <a href="#frontendport" title="FrontendPort">FrontendPort</a>: <i>
      - <a href="frontendport.md">FrontendPort</a></i>
    <a href="#gatewayipconfiguration" title="GatewayIpConfiguration">GatewayIpConfiguration</a>: <i>
      - <a href="gatewayipconfiguration.md">GatewayIpConfiguration</a></i>
    <a href="#httplistener" title="HttpListener">HttpListener</a>: <i>
      - <a href="httplistener.md">HttpListener</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#probe" title="Probe">Probe</a>: <i>
      - <a href="probe.md">Probe</a></i>
    <a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>: <i>
      - <a href="redirectconfiguration.md">RedirectConfiguration</a></i>
    <a href="#requestroutingrule" title="RequestRoutingRule">RequestRoutingRule</a>: <i>
      - <a href="requestroutingrule.md">RequestRoutingRule</a></i>
    <a href="#rewriteruleset" title="RewriteRuleSet">RewriteRuleSet</a>: <i>
      - <a href="rewriteruleset.md">RewriteRuleSet</a></i>
    <a href="#sku" title="Sku">Sku</a>: <i>
      - <a href="sku.md">Sku</a></i>
    <a href="#sslcertificate" title="SslCertificate">SslCertificate</a>: <i>
      - <a href="sslcertificate.md">SslCertificate</a></i>
    <a href="#sslpolicy" title="SslPolicy">SslPolicy</a>: <i>
      - <a href="sslpolicy.md">SslPolicy</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#trustedrootcertificate" title="TrustedRootCertificate">TrustedRootCertificate</a>: <i>
      - <a href="trustedrootcertificate.md">TrustedRootCertificate</a></i>
    <a href="#urlpathmap" title="UrlPathMap">UrlPathMap</a>: <i>
      - <a href="urlpathmap.md">UrlPathMap</a></i>
    <a href="#wafconfiguration" title="WafConfiguration">WafConfiguration</a>: <i>
      - <a href="wafconfiguration.md">WafConfiguration</a></i>
    <a href="#connectiondraining" title="ConnectionDraining">ConnectionDraining</a>: <i>
      - <a href="connectiondraining.md">ConnectionDraining</a></i>
    <a href="#match" title="Match">Match</a>: <i>
      - <a href="match.md">Match</a></i>
    <a href="#rewriterule" title="RewriteRule">RewriteRule</a>: <i>
      - <a href="rewriterule.md">RewriteRule</a></i>
    <a href="#pathrule" title="PathRule">PathRule</a>: <i>
      - <a href="pathrule.md">PathRule</a></i>
    <a href="#disabledrulegroup" title="DisabledRuleGroup">DisabledRuleGroup</a>: <i>
      - <a href="disabledrulegroup.md">DisabledRuleGroup</a></i>
    <a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - <a href="exclusion.md">Exclusion</a></i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="condition.md">Condition</a></i>
    <a href="#requestheaderconfiguration" title="RequestHeaderConfiguration">RequestHeaderConfiguration</a>: <i>
      - <a href="requestheaderconfiguration.md">RequestHeaderConfiguration</a></i>
    <a href="#responseheaderconfiguration" title="ResponseHeaderConfiguration">ResponseHeaderConfiguration</a>: <i>
      - <a href="responseheaderconfiguration.md">ResponseHeaderConfiguration</a></i>
</pre>

## Properties

#### EnableHttp2

Is HTTP2 enabled on the application gateway resource? Defaults to `false`.

_Required_: No

_Type_: Boolean

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

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

A collection of availability zones to spread the Application Gateway over.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationCertificate

_Required_: No

_Type_: List of <a href="authenticationcertificate.md">AuthenticationCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleConfiguration

_Required_: No

_Type_: List of <a href="autoscaleconfiguration.md">AutoscaleConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendAddressPool

_Required_: No

_Type_: List of <a href="backendaddresspool.md">BackendAddressPool</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendHttpSettings

_Required_: No

_Type_: List of <a href="backendhttpsettings.md">BackendHttpSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomErrorConfiguration

_Required_: No

_Type_: List of <a href="customerrorconfiguration.md">CustomErrorConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendIpConfiguration

_Required_: No

_Type_: List of <a href="frontendipconfiguration.md">FrontendIpConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPort

_Required_: No

_Type_: List of <a href="frontendport.md">FrontendPort</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIpConfiguration

_Required_: No

_Type_: List of <a href="gatewayipconfiguration.md">GatewayIpConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpListener

_Required_: No

_Type_: List of <a href="httplistener.md">HttpListener</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identity.md">Identity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Probe

_Required_: No

_Type_: List of <a href="probe.md">Probe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectConfiguration

_Required_: No

_Type_: List of <a href="redirectconfiguration.md">RedirectConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestRoutingRule

_Required_: No

_Type_: List of <a href="requestroutingrule.md">RequestRoutingRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteRuleSet

_Required_: No

_Type_: List of <a href="rewriteruleset.md">RewriteRuleSet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: List of <a href="sku.md">Sku</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificate

_Required_: No

_Type_: List of <a href="sslcertificate.md">SslCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPolicy

_Required_: No

_Type_: List of <a href="sslpolicy.md">SslPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedRootCertificate

_Required_: No

_Type_: List of <a href="trustedrootcertificate.md">TrustedRootCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlPathMap

_Required_: No

_Type_: List of <a href="urlpathmap.md">UrlPathMap</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafConfiguration

_Required_: No

_Type_: List of <a href="wafconfiguration.md">WafConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionDraining

_Required_: No

_Type_: List of <a href="connectiondraining.md">ConnectionDraining</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of <a href="match.md">Match</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteRule

_Required_: No

_Type_: List of <a href="rewriterule.md">RewriteRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRule

_Required_: No

_Type_: List of <a href="pathrule.md">PathRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisabledRuleGroup

_Required_: No

_Type_: List of <a href="disabledrulegroup.md">DisabledRuleGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No

_Type_: List of <a href="exclusion.md">Exclusion</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="condition.md">Condition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaderConfiguration

_Required_: No

_Type_: List of <a href="requestheaderconfiguration.md">RequestHeaderConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeaderConfiguration

_Required_: No

_Type_: List of <a href="responseheaderconfiguration.md">ResponseHeaderConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

