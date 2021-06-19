# TF::AzureRM::FirewallApplicationRuleCollection RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#fqdntags" title="FqdnTags">FqdnTags</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourceipgroups" title="SourceIpGroups">SourceIpGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#targetfqdns" title="TargetFqdns">TargetFqdns</a>" : <i>[ String, ... ]</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>[ <a href="protocoldefinition.md">ProtocolDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#fqdntags" title="FqdnTags">FqdnTags</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>: <i>
      - String</i>
<a href="#sourceipgroups" title="SourceIpGroups">SourceIpGroups</a>: <i>
      - String</i>
<a href="#targetfqdns" title="TargetFqdns">TargetFqdns</a>: <i>
      - String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>
      - <a href="protocoldefinition.md">ProtocolDefinition</a></i>
</pre>

## Properties

#### Description

Specifies a description for the rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FqdnTags

A list of FQDN tags. Possible values are `AppServiceEnvironment`, `AzureBackup`, `AzureKubernetesService`, `HDInsight`, `MicrosoftActiveProtectionService`, `WindowsDiagnostics`, `WindowsUpdate` and `WindowsVirtualDesktop`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddresses

A list of source IP addresses and/or IP ranges.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIpGroups

A list of source IP Group IDs for the rule.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetFqdns

A list of FQDNs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: List of <a href="protocoldefinition.md">ProtocolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

