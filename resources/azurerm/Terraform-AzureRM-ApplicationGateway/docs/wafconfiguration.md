# Terraform::AzureRM::ApplicationGateway WafConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#fileuploadlimitmb" title="FileUploadLimitMb">FileUploadLimitMb</a>" : <i>Double</i>,
    "<a href="#firewallmode" title="FirewallMode">FirewallMode</a>" : <i>String</i>,
    "<a href="#maxrequestbodysizekb" title="MaxRequestBodySizeKb">MaxRequestBodySizeKb</a>" : <i>Double</i>,
    "<a href="#requestbodycheck" title="RequestBodyCheck">RequestBodyCheck</a>" : <i>Boolean</i>,
    "<a href="#rulesettype" title="RuleSetType">RuleSetType</a>" : <i>String</i>,
    "<a href="#rulesetversion" title="RuleSetVersion">RuleSetVersion</a>" : <i>String</i>,
    "<a href="#disabledrulegroup" title="DisabledRuleGroup">DisabledRuleGroup</a>" : <i>[ <a href="wafconfiguration-disabledrulegroup.md">DisabledRuleGroup</a>, ... ]</i>,
    "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ <a href="wafconfiguration-exclusion.md">Exclusion</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#fileuploadlimitmb" title="FileUploadLimitMb">FileUploadLimitMb</a>: <i>Double</i>
<a href="#firewallmode" title="FirewallMode">FirewallMode</a>: <i>String</i>
<a href="#maxrequestbodysizekb" title="MaxRequestBodySizeKb">MaxRequestBodySizeKb</a>: <i>Double</i>
<a href="#requestbodycheck" title="RequestBodyCheck">RequestBodyCheck</a>: <i>Boolean</i>
<a href="#rulesettype" title="RuleSetType">RuleSetType</a>: <i>String</i>
<a href="#rulesetversion" title="RuleSetVersion">RuleSetVersion</a>: <i>String</i>
<a href="#disabledrulegroup" title="DisabledRuleGroup">DisabledRuleGroup</a>: <i>
      - <a href="wafconfiguration-disabledrulegroup.md">DisabledRuleGroup</a></i>
<a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - <a href="wafconfiguration-exclusion.md">Exclusion</a></i>
</pre>

## Properties

#### Enabled

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileUploadLimitMb

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallMode

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRequestBodySizeKb

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestBodyCheck

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSetType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSetVersion

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisabledRuleGroup

_Required_: No
_Type_: List of <a href="wafconfiguration-disabledrulegroup.md">DisabledRuleGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No
_Type_: List of <a href="wafconfiguration-exclusion.md">Exclusion</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

