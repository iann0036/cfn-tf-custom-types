# TF::AzureRM::ApplicationGateway WafConfigurationDefinition

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
    "<a href="#disabledrulegroup" title="DisabledRuleGroup">DisabledRuleGroup</a>" : <i>[ <a href="disabledrulegroupdefinition.md">DisabledRuleGroupDefinition</a>, ... ]</i>,
    "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ <a href="exclusiondefinition.md">ExclusionDefinition</a>, ... ]</i>
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
      - <a href="disabledrulegroupdefinition.md">DisabledRuleGroupDefinition</a></i>
<a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - <a href="exclusiondefinition.md">ExclusionDefinition</a></i>
</pre>

## Properties

#### Enabled

Is the Web Application Firewall be enabled?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileUploadLimitMb

The File Upload Limit in MB. Accepted values are in the range `1`MB to `750`MB for the `WAF_v2` SKU, and `1`MB to `500`MB for all other SKUs. Defaults to `100`MB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallMode

The Web Application Firewall Mode. Possible values are `Detection` and `Prevention`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRequestBodySizeKb

The Maximum Request Body Size in KB.  Accepted values are in the range `1`KB to `128`KB.  Defaults to `128`KB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestBodyCheck

Is Request Body Inspection enabled?  Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSetType

The Type of the Rule Set used for this Web Application Firewall. Currently, only `OWASP` is supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSetVersion

The Version of the Rule Set used for this Web Application Firewall. Possible values are `2.2.9`, `3.0`, and `3.1`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisabledRuleGroup

_Required_: No

_Type_: List of <a href="disabledrulegroupdefinition.md">DisabledRuleGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No

_Type_: List of <a href="exclusiondefinition.md">ExclusionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

