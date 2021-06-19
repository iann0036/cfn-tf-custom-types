# TF::GoogleBeta::GoogleOsConfigGuestPolicies RecipesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#desiredstate" title="DesiredState">DesiredState</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#artifacts" title="Artifacts">Artifacts</a>" : <i>[ <a href="artifactsdefinition.md">ArtifactsDefinition</a>, ... ]</i>,
    "<a href="#installsteps" title="InstallSteps">InstallSteps</a>" : <i>[ <a href="installstepsdefinition.md">InstallStepsDefinition</a>, ... ]</i>,
    "<a href="#updatesteps" title="UpdateSteps">UpdateSteps</a>" : <i>[ <a href="updatestepsdefinition.md">UpdateStepsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#desiredstate" title="DesiredState">DesiredState</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#artifacts" title="Artifacts">Artifacts</a>: <i>
      - <a href="artifactsdefinition.md">ArtifactsDefinition</a></i>
<a href="#installsteps" title="InstallSteps">InstallSteps</a>: <i>
      - <a href="installstepsdefinition.md">InstallStepsDefinition</a></i>
<a href="#updatesteps" title="UpdateSteps">UpdateSteps</a>: <i>
      - <a href="updatestepsdefinition.md">UpdateStepsDefinition</a></i>
</pre>

## Properties

#### DesiredState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Artifacts

_Required_: No

_Type_: List of <a href="artifactsdefinition.md">ArtifactsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallSteps

_Required_: No

_Type_: List of <a href="installstepsdefinition.md">InstallStepsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateSteps

_Required_: No

_Type_: List of <a href="updatestepsdefinition.md">UpdateStepsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

