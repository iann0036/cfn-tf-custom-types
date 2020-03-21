# Terraform::AzureRM::ApplicationGateway

CloudFormation equivalent of azurerm_application_gateway

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ApplicationGateway",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#authenticationcertificate" title="AuthenticationCertificate">AuthenticationCertificate</a>" : <i>[ &lt;a href=&#34;authenticationcertificate.md&#34;&gt;AuthenticationCertificate&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscaleconfiguration" title="AutoscaleConfiguration">AutoscaleConfiguration</a>" : <i>[ &lt;a href=&#34;autoscaleconfiguration.md&#34;&gt;AutoscaleConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#backendaddresspool" title="BackendAddressPool">BackendAddressPool</a>" : <i>[ &lt;a href=&#34;backendaddresspool.md&#34;&gt;BackendAddressPool&lt;/a&gt;, ... ]</i>,
        "<a href="#backendhttpsettings" title="BackendHttpSettings">BackendHttpSettings</a>" : <i>[ &lt;a href=&#34;backendhttpsettings.md&#34;&gt;BackendHttpSettings&lt;/a&gt;, ... ]</i>,
        "<a href="#customerrorconfiguration" title="CustomErrorConfiguration">CustomErrorConfiguration</a>" : <i>[ &lt;a href=&#34;customerrorconfiguration.md&#34;&gt;CustomErrorConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#frontendipconfiguration" title="FrontendIpConfiguration">FrontendIpConfiguration</a>" : <i>[ &lt;a href=&#34;frontendipconfiguration.md&#34;&gt;FrontendIpConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#frontendport" title="FrontendPort">FrontendPort</a>" : <i>[ &lt;a href=&#34;frontendport.md&#34;&gt;FrontendPort&lt;/a&gt;, ... ]</i>,
        "<a href="#gatewayipconfiguration" title="GatewayIpConfiguration">GatewayIpConfiguration</a>" : <i>[ &lt;a href=&#34;gatewayipconfiguration.md&#34;&gt;GatewayIpConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#httplistener" title="HttpListener">HttpListener</a>" : <i>[ &lt;a href=&#34;httplistener.md&#34;&gt;HttpListener&lt;/a&gt;, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;, ... ]</i>,
        "<a href="#probe" title="Probe">Probe</a>" : <i>[ &lt;a href=&#34;probe.md&#34;&gt;Probe&lt;/a&gt;, ... ]</i>,
        "<a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>" : <i>[ &lt;a href=&#34;redirectconfiguration.md&#34;&gt;RedirectConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#requestroutingrule" title="RequestRoutingRule">RequestRoutingRule</a>" : <i>[ &lt;a href=&#34;requestroutingrule.md&#34;&gt;RequestRoutingRule&lt;/a&gt;, ... ]</i>,
        "<a href="#rewriteruleset" title="RewriteRuleSet">RewriteRuleSet</a>" : <i>[ &lt;a href=&#34;rewriteruleset.md&#34;&gt;RewriteRuleSet&lt;/a&gt;, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ &lt;a href=&#34;sku.md&#34;&gt;Sku&lt;/a&gt;, ... ]</i>,
        "<a href="#sslcertificate" title="SslCertificate">SslCertificate</a>" : <i>[ &lt;a href=&#34;sslcertificate.md&#34;&gt;SslCertificate&lt;/a&gt;, ... ]</i>,
        "<a href="#sslpolicy" title="SslPolicy">SslPolicy</a>" : <i>[ &lt;a href=&#34;sslpolicy.md&#34;&gt;SslPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#trustedrootcertificate" title="TrustedRootCertificate">TrustedRootCertificate</a>" : <i>[ &lt;a href=&#34;trustedrootcertificate.md&#34;&gt;TrustedRootCertificate&lt;/a&gt;, ... ]</i>,
        "<a href="#urlpathmap" title="UrlPathMap">UrlPathMap</a>" : <i>[ &lt;a href=&#34;urlpathmap.md&#34;&gt;UrlPathMap&lt;/a&gt;, ... ]</i>,
        "<a href="#wafconfiguration" title="WafConfiguration">WafConfiguration</a>" : <i>[ &lt;a href=&#34;wafconfiguration.md&#34;&gt;WafConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#connectiondraining" title="ConnectionDraining">ConnectionDraining</a>" : <i>[ &lt;a href=&#34;connectiondraining.md&#34;&gt;ConnectionDraining&lt;/a&gt;, ... ]</i>,
        "<a href="#match" title="Match">Match</a>" : <i>[ &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;, ... ]</i>,
        "<a href="#rewriterule" title="RewriteRule">RewriteRule</a>" : <i>[ &lt;a href=&#34;rewriterule.md&#34;&gt;RewriteRule&lt;/a&gt;, ... ]</i>,
        "<a href="#pathrule" title="PathRule">PathRule</a>" : <i>[ &lt;a href=&#34;pathrule.md&#34;&gt;PathRule&lt;/a&gt;, ... ]</i>,
        "<a href="#disabledrulegroup" title="DisabledRuleGroup">DisabledRuleGroup</a>" : <i>[ &lt;a href=&#34;disabledrulegroup.md&#34;&gt;DisabledRuleGroup&lt;/a&gt;, ... ]</i>,
        "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ &lt;a href=&#34;exclusion.md&#34;&gt;Exclusion&lt;/a&gt;, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;, ... ]</i>,
        "<a href="#requestheaderconfiguration" title="RequestHeaderConfiguration">RequestHeaderConfiguration</a>" : <i>[ &lt;a href=&#34;requestheaderconfiguration.md&#34;&gt;RequestHeaderConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#responseheaderconfiguration" title="ResponseHeaderConfiguration">ResponseHeaderConfiguration</a>" : <i>[ &lt;a href=&#34;responseheaderconfiguration.md&#34;&gt;ResponseHeaderConfiguration&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ApplicationGateway
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#authenticationcertificate" title="AuthenticationCertificate">AuthenticationCertificate</a>: <i>
      - &lt;a href=&#34;authenticationcertificate.md&#34;&gt;AuthenticationCertificate&lt;/a&gt;</i>
    <a href="#autoscaleconfiguration" title="AutoscaleConfiguration">AutoscaleConfiguration</a>: <i>
      - &lt;a href=&#34;autoscaleconfiguration.md&#34;&gt;AutoscaleConfiguration&lt;/a&gt;</i>
    <a href="#backendaddresspool" title="BackendAddressPool">BackendAddressPool</a>: <i>
      - &lt;a href=&#34;backendaddresspool.md&#34;&gt;BackendAddressPool&lt;/a&gt;</i>
    <a href="#backendhttpsettings" title="BackendHttpSettings">BackendHttpSettings</a>: <i>
      - &lt;a href=&#34;backendhttpsettings.md&#34;&gt;BackendHttpSettings&lt;/a&gt;</i>
    <a href="#customerrorconfiguration" title="CustomErrorConfiguration">CustomErrorConfiguration</a>: <i>
      - &lt;a href=&#34;customerrorconfiguration.md&#34;&gt;CustomErrorConfiguration&lt;/a&gt;</i>
    <a href="#frontendipconfiguration" title="FrontendIpConfiguration">FrontendIpConfiguration</a>: <i>
      - &lt;a href=&#34;frontendipconfiguration.md&#34;&gt;FrontendIpConfiguration&lt;/a&gt;</i>
    <a href="#frontendport" title="FrontendPort">FrontendPort</a>: <i>
      - &lt;a href=&#34;frontendport.md&#34;&gt;FrontendPort&lt;/a&gt;</i>
    <a href="#gatewayipconfiguration" title="GatewayIpConfiguration">GatewayIpConfiguration</a>: <i>
      - &lt;a href=&#34;gatewayipconfiguration.md&#34;&gt;GatewayIpConfiguration&lt;/a&gt;</i>
    <a href="#httplistener" title="HttpListener">HttpListener</a>: <i>
      - &lt;a href=&#34;httplistener.md&#34;&gt;HttpListener&lt;/a&gt;</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;</i>
    <a href="#probe" title="Probe">Probe</a>: <i>
      - &lt;a href=&#34;probe.md&#34;&gt;Probe&lt;/a&gt;</i>
    <a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>: <i>
      - &lt;a href=&#34;redirectconfiguration.md&#34;&gt;RedirectConfiguration&lt;/a&gt;</i>
    <a href="#requestroutingrule" title="RequestRoutingRule">RequestRoutingRule</a>: <i>
      - &lt;a href=&#34;requestroutingrule.md&#34;&gt;RequestRoutingRule&lt;/a&gt;</i>
    <a href="#rewriteruleset" title="RewriteRuleSet">RewriteRuleSet</a>: <i>
      - &lt;a href=&#34;rewriteruleset.md&#34;&gt;RewriteRuleSet&lt;/a&gt;</i>
    <a href="#sku" title="Sku">Sku</a>: <i>
      - &lt;a href=&#34;sku.md&#34;&gt;Sku&lt;/a&gt;</i>
    <a href="#sslcertificate" title="SslCertificate">SslCertificate</a>: <i>
      - &lt;a href=&#34;sslcertificate.md&#34;&gt;SslCertificate&lt;/a&gt;</i>
    <a href="#sslpolicy" title="SslPolicy">SslPolicy</a>: <i>
      - &lt;a href=&#34;sslpolicy.md&#34;&gt;SslPolicy&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#trustedrootcertificate" title="TrustedRootCertificate">TrustedRootCertificate</a>: <i>
      - &lt;a href=&#34;trustedrootcertificate.md&#34;&gt;TrustedRootCertificate&lt;/a&gt;</i>
    <a href="#urlpathmap" title="UrlPathMap">UrlPathMap</a>: <i>
      - &lt;a href=&#34;urlpathmap.md&#34;&gt;UrlPathMap&lt;/a&gt;</i>
    <a href="#wafconfiguration" title="WafConfiguration">WafConfiguration</a>: <i>
      - &lt;a href=&#34;wafconfiguration.md&#34;&gt;WafConfiguration&lt;/a&gt;</i>
    <a href="#connectiondraining" title="ConnectionDraining">ConnectionDraining</a>: <i>
      - &lt;a href=&#34;connectiondraining.md&#34;&gt;ConnectionDraining&lt;/a&gt;</i>
    <a href="#match" title="Match">Match</a>: <i>
      - &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;</i>
    <a href="#rewriterule" title="RewriteRule">RewriteRule</a>: <i>
      - &lt;a href=&#34;rewriterule.md&#34;&gt;RewriteRule&lt;/a&gt;</i>
    <a href="#pathrule" title="PathRule">PathRule</a>: <i>
      - &lt;a href=&#34;pathrule.md&#34;&gt;PathRule&lt;/a&gt;</i>
    <a href="#disabledrulegroup" title="DisabledRuleGroup">DisabledRuleGroup</a>: <i>
      - &lt;a href=&#34;disabledrulegroup.md&#34;&gt;DisabledRuleGroup&lt;/a&gt;</i>
    <a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - &lt;a href=&#34;exclusion.md&#34;&gt;Exclusion&lt;/a&gt;</i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;</i>
    <a href="#requestheaderconfiguration" title="RequestHeaderConfiguration">RequestHeaderConfiguration</a>: <i>
      - &lt;a href=&#34;requestheaderconfiguration.md&#34;&gt;RequestHeaderConfiguration&lt;/a&gt;</i>
    <a href="#responseheaderconfiguration" title="ResponseHeaderConfiguration">ResponseHeaderConfiguration</a>: <i>
      - &lt;a href=&#34;responseheaderconfiguration.md&#34;&gt;ResponseHeaderConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttp2

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;authenticationcertificate.md&#34;&gt;AuthenticationCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;autoscaleconfiguration.md&#34;&gt;AutoscaleConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendAddressPool

_Required_: No

_Type_: List of &lt;a href=&#34;backendaddresspool.md&#34;&gt;BackendAddressPool&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendHttpSettings

_Required_: No

_Type_: List of &lt;a href=&#34;backendhttpsettings.md&#34;&gt;BackendHttpSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomErrorConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;customerrorconfiguration.md&#34;&gt;CustomErrorConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendIpConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;frontendipconfiguration.md&#34;&gt;FrontendIpConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPort

_Required_: No

_Type_: List of &lt;a href=&#34;frontendport.md&#34;&gt;FrontendPort&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIpConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;gatewayipconfiguration.md&#34;&gt;GatewayIpConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpListener

_Required_: No

_Type_: List of &lt;a href=&#34;httplistener.md&#34;&gt;HttpListener&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Probe

_Required_: No

_Type_: List of &lt;a href=&#34;probe.md&#34;&gt;Probe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;redirectconfiguration.md&#34;&gt;RedirectConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestRoutingRule

_Required_: No

_Type_: List of &lt;a href=&#34;requestroutingrule.md&#34;&gt;RequestRoutingRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteRuleSet

_Required_: No

_Type_: List of &lt;a href=&#34;rewriteruleset.md&#34;&gt;RewriteRuleSet&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: List of &lt;a href=&#34;sku.md&#34;&gt;Sku&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;sslcertificate.md&#34;&gt;SslCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;sslpolicy.md&#34;&gt;SslPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedRootCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;trustedrootcertificate.md&#34;&gt;TrustedRootCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlPathMap

_Required_: No

_Type_: List of &lt;a href=&#34;urlpathmap.md&#34;&gt;UrlPathMap&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;wafconfiguration.md&#34;&gt;WafConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionDraining

_Required_: No

_Type_: List of &lt;a href=&#34;connectiondraining.md&#34;&gt;ConnectionDraining&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteRule

_Required_: No

_Type_: List of &lt;a href=&#34;rewriterule.md&#34;&gt;RewriteRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRule

_Required_: No

_Type_: List of &lt;a href=&#34;pathrule.md&#34;&gt;PathRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisabledRuleGroup

_Required_: No

_Type_: List of &lt;a href=&#34;disabledrulegroup.md&#34;&gt;DisabledRuleGroup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No

_Type_: List of &lt;a href=&#34;exclusion.md&#34;&gt;Exclusion&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaderConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;requestheaderconfiguration.md&#34;&gt;RequestHeaderConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeaderConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;responseheaderconfiguration.md&#34;&gt;ResponseHeaderConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

