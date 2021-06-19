# TF::AzureRM::MediaContentKeyPolicy PolicyOptionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clearkeyconfigurationenabled" title="ClearKeyConfigurationEnabled">ClearKeyConfigurationEnabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#openrestrictionenabled" title="OpenRestrictionEnabled">OpenRestrictionEnabled</a>" : <i>Boolean</i>,
    "<a href="#widevineconfigurationtemplate" title="WidevineConfigurationTemplate">WidevineConfigurationTemplate</a>" : <i>String</i>,
    "<a href="#fairplayconfiguration" title="FairplayConfiguration">FairplayConfiguration</a>" : <i>[ <a href="fairplayconfigurationdefinition.md">FairplayConfigurationDefinition</a>, ... ]</i>,
    "<a href="#playreadyconfigurationlicense" title="PlayreadyConfigurationLicense">PlayreadyConfigurationLicense</a>" : <i>[ <a href="playreadyconfigurationlicensedefinition.md">PlayreadyConfigurationLicenseDefinition</a>, ... ]</i>,
    "<a href="#tokenrestriction" title="TokenRestriction">TokenRestriction</a>" : <i>[ <a href="tokenrestrictiondefinition.md">TokenRestrictionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clearkeyconfigurationenabled" title="ClearKeyConfigurationEnabled">ClearKeyConfigurationEnabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#openrestrictionenabled" title="OpenRestrictionEnabled">OpenRestrictionEnabled</a>: <i>Boolean</i>
<a href="#widevineconfigurationtemplate" title="WidevineConfigurationTemplate">WidevineConfigurationTemplate</a>: <i>String</i>
<a href="#fairplayconfiguration" title="FairplayConfiguration">FairplayConfiguration</a>: <i>
      - <a href="fairplayconfigurationdefinition.md">FairplayConfigurationDefinition</a></i>
<a href="#playreadyconfigurationlicense" title="PlayreadyConfigurationLicense">PlayreadyConfigurationLicense</a>: <i>
      - <a href="playreadyconfigurationlicensedefinition.md">PlayreadyConfigurationLicenseDefinition</a></i>
<a href="#tokenrestriction" title="TokenRestriction">TokenRestriction</a>: <i>
      - <a href="tokenrestrictiondefinition.md">TokenRestrictionDefinition</a></i>
</pre>

## Properties

#### ClearKeyConfigurationEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenRestrictionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidevineConfigurationTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FairplayConfiguration

_Required_: No

_Type_: List of <a href="fairplayconfigurationdefinition.md">FairplayConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlayreadyConfigurationLicense

_Required_: No

_Type_: List of <a href="playreadyconfigurationlicensedefinition.md">PlayreadyConfigurationLicenseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenRestriction

_Required_: No

_Type_: List of <a href="tokenrestrictiondefinition.md">TokenRestrictionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

