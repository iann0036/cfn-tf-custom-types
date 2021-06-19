# TF::AzureRM::IotSecuritySolution RecommendationsEnabledDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acrauthentication" title="AcrAuthentication">AcrAuthentication</a>" : <i>Boolean</i>,
    "<a href="#agentsendunutilizedmsg" title="AgentSendUnutilizedMsg">AgentSendUnutilizedMsg</a>" : <i>Boolean</i>,
    "<a href="#baseline" title="Baseline">Baseline</a>" : <i>Boolean</i>,
    "<a href="#edgehubmemoptimize" title="EdgeHubMemOptimize">EdgeHubMemOptimize</a>" : <i>Boolean</i>,
    "<a href="#edgeloggingoption" title="EdgeLoggingOption">EdgeLoggingOption</a>" : <i>Boolean</i>,
    "<a href="#inconsistentmodulesettings" title="InconsistentModuleSettings">InconsistentModuleSettings</a>" : <i>Boolean</i>,
    "<a href="#installagent" title="InstallAgent">InstallAgent</a>" : <i>Boolean</i>,
    "<a href="#ipfilterdenyall" title="IpFilterDenyAll">IpFilterDenyAll</a>" : <i>Boolean</i>,
    "<a href="#ipfilterpermissiverule" title="IpFilterPermissiveRule">IpFilterPermissiveRule</a>" : <i>Boolean</i>,
    "<a href="#openports" title="OpenPorts">OpenPorts</a>" : <i>Boolean</i>,
    "<a href="#permissivefirewallpolicy" title="PermissiveFirewallPolicy">PermissiveFirewallPolicy</a>" : <i>Boolean</i>,
    "<a href="#permissiveinputfirewallrules" title="PermissiveInputFirewallRules">PermissiveInputFirewallRules</a>" : <i>Boolean</i>,
    "<a href="#permissiveoutputfirewallrules" title="PermissiveOutputFirewallRules">PermissiveOutputFirewallRules</a>" : <i>Boolean</i>,
    "<a href="#privilegeddockeroptions" title="PrivilegedDockerOptions">PrivilegedDockerOptions</a>" : <i>Boolean</i>,
    "<a href="#sharedcredentials" title="SharedCredentials">SharedCredentials</a>" : <i>Boolean</i>,
    "<a href="#vulnerabletlsciphersuite" title="VulnerableTlsCipherSuite">VulnerableTlsCipherSuite</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#acrauthentication" title="AcrAuthentication">AcrAuthentication</a>: <i>Boolean</i>
<a href="#agentsendunutilizedmsg" title="AgentSendUnutilizedMsg">AgentSendUnutilizedMsg</a>: <i>Boolean</i>
<a href="#baseline" title="Baseline">Baseline</a>: <i>Boolean</i>
<a href="#edgehubmemoptimize" title="EdgeHubMemOptimize">EdgeHubMemOptimize</a>: <i>Boolean</i>
<a href="#edgeloggingoption" title="EdgeLoggingOption">EdgeLoggingOption</a>: <i>Boolean</i>
<a href="#inconsistentmodulesettings" title="InconsistentModuleSettings">InconsistentModuleSettings</a>: <i>Boolean</i>
<a href="#installagent" title="InstallAgent">InstallAgent</a>: <i>Boolean</i>
<a href="#ipfilterdenyall" title="IpFilterDenyAll">IpFilterDenyAll</a>: <i>Boolean</i>
<a href="#ipfilterpermissiverule" title="IpFilterPermissiveRule">IpFilterPermissiveRule</a>: <i>Boolean</i>
<a href="#openports" title="OpenPorts">OpenPorts</a>: <i>Boolean</i>
<a href="#permissivefirewallpolicy" title="PermissiveFirewallPolicy">PermissiveFirewallPolicy</a>: <i>Boolean</i>
<a href="#permissiveinputfirewallrules" title="PermissiveInputFirewallRules">PermissiveInputFirewallRules</a>: <i>Boolean</i>
<a href="#permissiveoutputfirewallrules" title="PermissiveOutputFirewallRules">PermissiveOutputFirewallRules</a>: <i>Boolean</i>
<a href="#privilegeddockeroptions" title="PrivilegedDockerOptions">PrivilegedDockerOptions</a>: <i>Boolean</i>
<a href="#sharedcredentials" title="SharedCredentials">SharedCredentials</a>: <i>Boolean</i>
<a href="#vulnerabletlsciphersuite" title="VulnerableTlsCipherSuite">VulnerableTlsCipherSuite</a>: <i>Boolean</i>
</pre>

## Properties

#### AcrAuthentication

Is Principal Authentication enabled for the ACR repository? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentSendUnutilizedMsg

Is Agent send underutilized messages enabled? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Baseline

Is Security related system configuration issues identified? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeHubMemOptimize

Is IoT Edge Hub memory optimized? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeLoggingOption

Is logging configured for IoT Edge module? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InconsistentModuleSettings

Is inconsistent module settings enabled for SecurityGroup? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallAgent

is Azure IoT Security agent installed? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpFilterDenyAll

Is Default IP filter policy denied? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpFilterPermissiveRule

Is IP filter rule source allowable IP range too large? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenPorts

Is any ports open on the device? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissiveFirewallPolicy

Does firewall policy exist which allow necessary communication to/from the device? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissiveInputFirewallRules

Is only necessary addresses or ports are permitted in? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissiveOutputFirewallRules

Is only necessary addresses or ports are permitted out? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivilegedDockerOptions

Is high level permissions are needed for the module? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedCredentials

Is any credentials shared among devices? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VulnerableTlsCipherSuite

Does TLS cipher suite need to be updated? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

