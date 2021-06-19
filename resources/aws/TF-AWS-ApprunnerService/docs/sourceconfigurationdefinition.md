# TF::AWS::ApprunnerService SourceConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autodeploymentsenabled" title="AutoDeploymentsEnabled">AutoDeploymentsEnabled</a>" : <i>Boolean</i>,
    "<a href="#authenticationconfiguration" title="AuthenticationConfiguration">AuthenticationConfiguration</a>" : <i>[ <a href="authenticationconfigurationdefinition.md">AuthenticationConfigurationDefinition</a>, ... ]</i>,
    "<a href="#coderepository" title="CodeRepository">CodeRepository</a>" : <i>[ <a href="coderepositorydefinition.md">CodeRepositoryDefinition</a>, ... ]</i>,
    "<a href="#imagerepository" title="ImageRepository">ImageRepository</a>" : <i>[ <a href="imagerepositorydefinition.md">ImageRepositoryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autodeploymentsenabled" title="AutoDeploymentsEnabled">AutoDeploymentsEnabled</a>: <i>Boolean</i>
<a href="#authenticationconfiguration" title="AuthenticationConfiguration">AuthenticationConfiguration</a>: <i>
      - <a href="authenticationconfigurationdefinition.md">AuthenticationConfigurationDefinition</a></i>
<a href="#coderepository" title="CodeRepository">CodeRepository</a>: <i>
      - <a href="coderepositorydefinition.md">CodeRepositoryDefinition</a></i>
<a href="#imagerepository" title="ImageRepository">ImageRepository</a>: <i>
      - <a href="imagerepositorydefinition.md">ImageRepositoryDefinition</a></i>
</pre>

## Properties

#### AutoDeploymentsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationConfiguration

_Required_: No

_Type_: List of <a href="authenticationconfigurationdefinition.md">AuthenticationConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodeRepository

_Required_: No

_Type_: List of <a href="coderepositorydefinition.md">CodeRepositoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageRepository

_Required_: No

_Type_: List of <a href="imagerepositorydefinition.md">ImageRepositoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

