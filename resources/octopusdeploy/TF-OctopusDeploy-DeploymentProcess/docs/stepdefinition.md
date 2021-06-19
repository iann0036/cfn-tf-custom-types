# TF::OctopusDeploy::DeploymentProcess StepDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#condition" title="Condition">Condition</a>" : <i>String</i>,
    "<a href="#conditionexpression" title="ConditionExpression">ConditionExpression</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#packagerequirement" title="PackageRequirement">PackageRequirement</a>" : <i>String</i>,
    "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="propertiesdefinition.md">PropertiesDefinition</a>, ... ]</i>,
    "<a href="#starttrigger" title="StartTrigger">StartTrigger</a>" : <i>String</i>,
    "<a href="#targetroles" title="TargetRoles">TargetRoles</a>" : <i>[ String, ... ]</i>,
    "<a href="#windowsize" title="WindowSize">WindowSize</a>" : <i>String</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ <a href="actiondefinition.md">ActionDefinition</a>, ... ]</i>,
    "<a href="#applyterraformtemplateaction" title="ApplyTerraformTemplateAction">ApplyTerraformTemplateAction</a>" : <i>[ <a href="applyterraformtemplateactiondefinition.md">ApplyTerraformTemplateActionDefinition</a>, ... ]</i>,
    "<a href="#deploykubernetessecretaction" title="DeployKubernetesSecretAction">DeployKubernetesSecretAction</a>" : <i>[ <a href="deploykubernetessecretactiondefinition.md">DeployKubernetesSecretActionDefinition</a>, ... ]</i>,
    "<a href="#deploypackageaction" title="DeployPackageAction">DeployPackageAction</a>" : <i>[ <a href="deploypackageactiondefinition.md">DeployPackageActionDefinition</a>, ... ]</i>,
    "<a href="#deploywindowsserviceaction" title="DeployWindowsServiceAction">DeployWindowsServiceAction</a>" : <i>[ <a href="deploywindowsserviceactiondefinition.md">DeployWindowsServiceActionDefinition</a>, ... ]</i>,
    "<a href="#manualinterventionaction" title="ManualInterventionAction">ManualInterventionAction</a>" : <i>[ <a href="manualinterventionactiondefinition.md">ManualInterventionActionDefinition</a>, ... ]</i>,
    "<a href="#runkubectlscriptaction" title="RunKubectlScriptAction">RunKubectlScriptAction</a>" : <i>[ <a href="runkubectlscriptactiondefinition.md">RunKubectlScriptActionDefinition</a>, ... ]</i>,
    "<a href="#runscriptaction" title="RunScriptAction">RunScriptAction</a>" : <i>[ <a href="runscriptactiondefinition.md">RunScriptActionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#condition" title="Condition">Condition</a>: <i>String</i>
<a href="#conditionexpression" title="ConditionExpression">ConditionExpression</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#packagerequirement" title="PackageRequirement">PackageRequirement</a>: <i>String</i>
<a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="propertiesdefinition.md">PropertiesDefinition</a></i>
<a href="#starttrigger" title="StartTrigger">StartTrigger</a>: <i>String</i>
<a href="#targetroles" title="TargetRoles">TargetRoles</a>: <i>
      - String</i>
<a href="#windowsize" title="WindowSize">WindowSize</a>: <i>String</i>
<a href="#action" title="Action">Action</a>: <i>
      - <a href="actiondefinition.md">ActionDefinition</a></i>
<a href="#applyterraformtemplateaction" title="ApplyTerraformTemplateAction">ApplyTerraformTemplateAction</a>: <i>
      - <a href="applyterraformtemplateactiondefinition.md">ApplyTerraformTemplateActionDefinition</a></i>
<a href="#deploykubernetessecretaction" title="DeployKubernetesSecretAction">DeployKubernetesSecretAction</a>: <i>
      - <a href="deploykubernetessecretactiondefinition.md">DeployKubernetesSecretActionDefinition</a></i>
<a href="#deploypackageaction" title="DeployPackageAction">DeployPackageAction</a>: <i>
      - <a href="deploypackageactiondefinition.md">DeployPackageActionDefinition</a></i>
<a href="#deploywindowsserviceaction" title="DeployWindowsServiceAction">DeployWindowsServiceAction</a>: <i>
      - <a href="deploywindowsserviceactiondefinition.md">DeployWindowsServiceActionDefinition</a></i>
<a href="#manualinterventionaction" title="ManualInterventionAction">ManualInterventionAction</a>: <i>
      - <a href="manualinterventionactiondefinition.md">ManualInterventionActionDefinition</a></i>
<a href="#runkubectlscriptaction" title="RunKubectlScriptAction">RunKubectlScriptAction</a>: <i>
      - <a href="runkubectlscriptactiondefinition.md">RunKubectlScriptActionDefinition</a></i>
<a href="#runscriptaction" title="RunScriptAction">RunScriptAction</a>: <i>
      - <a href="runscriptactiondefinition.md">RunScriptActionDefinition</a></i>
</pre>

## Properties

#### Condition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionExpression

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageRequirement

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No

_Type_: List of <a href="propertiesdefinition.md">PropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTrigger

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRoles

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="actiondefinition.md">ActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyTerraformTemplateAction

_Required_: No

_Type_: List of <a href="applyterraformtemplateactiondefinition.md">ApplyTerraformTemplateActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployKubernetesSecretAction

_Required_: No

_Type_: List of <a href="deploykubernetessecretactiondefinition.md">DeployKubernetesSecretActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployPackageAction

_Required_: No

_Type_: List of <a href="deploypackageactiondefinition.md">DeployPackageActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployWindowsServiceAction

_Required_: No

_Type_: List of <a href="deploywindowsserviceactiondefinition.md">DeployWindowsServiceActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManualInterventionAction

_Required_: No

_Type_: List of <a href="manualinterventionactiondefinition.md">ManualInterventionActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunKubectlScriptAction

_Required_: No

_Type_: List of <a href="runkubectlscriptactiondefinition.md">RunKubectlScriptActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunScriptAction

_Required_: No

_Type_: List of <a href="runscriptactiondefinition.md">RunScriptActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

