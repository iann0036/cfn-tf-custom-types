# TF::OctopusDeploy::DeploymentProcess DeployKubernetesSecretActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#canbeusedforprojectversioning" title="CanBeUsedForProjectVersioning">CanBeUsedForProjectVersioning</a>" : <i>Boolean</i>,
    "<a href="#channels" title="Channels">Channels</a>" : <i>[ String, ... ]</i>,
    "<a href="#condition" title="Condition">Condition</a>" : <i>String</i>,
    "<a href="#environments" title="Environments">Environments</a>" : <i>[ String, ... ]</i>,
    "<a href="#excludedenvironments" title="ExcludedEnvironments">ExcludedEnvironments</a>" : <i>[ String, ... ]</i>,
    "<a href="#features" title="Features">Features</a>" : <i>[ String, ... ]</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#isdisabled" title="IsDisabled">IsDisabled</a>" : <i>Boolean</i>,
    "<a href="#isrequired" title="IsRequired">IsRequired</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
    "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="propertiesdefinition.md">PropertiesDefinition</a>, ... ]</i>,
    "<a href="#runonserver" title="RunOnServer">RunOnServer</a>" : <i>Boolean</i>,
    "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>,
    "<a href="#secretvalues" title="SecretValues">SecretValues</a>" : <i>[ <a href="secretvaluesdefinition.md">SecretValuesDefinition</a>, ... ]</i>,
    "<a href="#tenanttags" title="TenantTags">TenantTags</a>" : <i>[ String, ... ]</i>,
    "<a href="#actiontemplate" title="ActionTemplate">ActionTemplate</a>" : <i>[ <a href="actiontemplatedefinition.md">ActionTemplateDefinition</a>, ... ]</i>,
    "<a href="#container" title="Container">Container</a>" : <i>[ <a href="containerdefinition.md">ContainerDefinition</a>, ... ]</i>,
    "<a href="#package" title="Package">Package</a>" : <i>[ <a href="packagedefinition.md">PackageDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#canbeusedforprojectversioning" title="CanBeUsedForProjectVersioning">CanBeUsedForProjectVersioning</a>: <i>Boolean</i>
<a href="#channels" title="Channels">Channels</a>: <i>
      - String</i>
<a href="#condition" title="Condition">Condition</a>: <i>String</i>
<a href="#environments" title="Environments">Environments</a>: <i>
      - String</i>
<a href="#excludedenvironments" title="ExcludedEnvironments">ExcludedEnvironments</a>: <i>
      - String</i>
<a href="#features" title="Features">Features</a>: <i>
      - String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#isdisabled" title="IsDisabled">IsDisabled</a>: <i>Boolean</i>
<a href="#isrequired" title="IsRequired">IsRequired</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#notes" title="Notes">Notes</a>: <i>String</i>
<a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="propertiesdefinition.md">PropertiesDefinition</a></i>
<a href="#runonserver" title="RunOnServer">RunOnServer</a>: <i>Boolean</i>
<a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
<a href="#secretvalues" title="SecretValues">SecretValues</a>: <i>
      - <a href="secretvaluesdefinition.md">SecretValuesDefinition</a></i>
<a href="#tenanttags" title="TenantTags">TenantTags</a>: <i>
      - String</i>
<a href="#actiontemplate" title="ActionTemplate">ActionTemplate</a>: <i>
      - <a href="actiontemplatedefinition.md">ActionTemplateDefinition</a></i>
<a href="#container" title="Container">Container</a>: <i>
      - <a href="containerdefinition.md">ContainerDefinition</a></i>
<a href="#package" title="Package">Package</a>: <i>
      - <a href="packagedefinition.md">PackageDefinition</a></i>
</pre>

## Properties

#### CanBeUsedForProjectVersioning

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Channels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environments

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedEnvironments

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Features

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsRequired

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No

_Type_: List of <a href="propertiesdefinition.md">PropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunOnServer

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretValues

_Required_: Yes

_Type_: List of <a href="secretvaluesdefinition.md">SecretValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionTemplate

_Required_: No

_Type_: List of <a href="actiontemplatedefinition.md">ActionTemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: List of <a href="containerdefinition.md">ContainerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Package

_Required_: No

_Type_: List of <a href="packagedefinition.md">PackageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

