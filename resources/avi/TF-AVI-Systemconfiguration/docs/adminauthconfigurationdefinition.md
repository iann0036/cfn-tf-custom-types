# TF::AVI::Systemconfiguration AdminAuthConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowlocaluserlogin" title="AllowLocalUserLogin">AllowLocalUserLogin</a>" : <i>Boolean</i>,
    "<a href="#authprofileref" title="AuthProfileRef">AuthProfileRef</a>" : <i>String</i>,
    "<a href="#alternateauthconfigurations" title="AlternateAuthConfigurations">AlternateAuthConfigurations</a>" : <i>[ <a href="alternateauthconfigurationsdefinition.md">AlternateAuthConfigurationsDefinition</a>, ... ]</i>,
    "<a href="#mappingrules" title="MappingRules">MappingRules</a>" : <i>[ <a href="mappingrulesdefinition.md">MappingRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowlocaluserlogin" title="AllowLocalUserLogin">AllowLocalUserLogin</a>: <i>Boolean</i>
<a href="#authprofileref" title="AuthProfileRef">AuthProfileRef</a>: <i>String</i>
<a href="#alternateauthconfigurations" title="AlternateAuthConfigurations">AlternateAuthConfigurations</a>: <i>
      - <a href="alternateauthconfigurationsdefinition.md">AlternateAuthConfigurationsDefinition</a></i>
<a href="#mappingrules" title="MappingRules">MappingRules</a>: <i>
      - <a href="mappingrulesdefinition.md">MappingRulesDefinition</a></i>
</pre>

## Properties

#### AllowLocalUserLogin

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthProfileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlternateAuthConfigurations

_Required_: No

_Type_: List of <a href="alternateauthconfigurationsdefinition.md">AlternateAuthConfigurationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MappingRules

_Required_: No

_Type_: List of <a href="mappingrulesdefinition.md">MappingRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

