# TF::AzureDevOps::BuildDefinition PullRequestTriggerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commentrequired" title="CommentRequired">CommentRequired</a>" : <i>String</i>,
    "<a href="#initialbranch" title="InitialBranch">InitialBranch</a>" : <i>String</i>,
    "<a href="#useyaml" title="UseYaml">UseYaml</a>" : <i>Boolean</i>,
    "<a href="#forks" title="Forks">Forks</a>" : <i>[ <a href="forksdefinition.md">ForksDefinition</a>, ... ]</i>,
    "<a href="#override" title="Override">Override</a>" : <i>[ <a href="overridedefinition.md">OverrideDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#commentrequired" title="CommentRequired">CommentRequired</a>: <i>String</i>
<a href="#initialbranch" title="InitialBranch">InitialBranch</a>: <i>String</i>
<a href="#useyaml" title="UseYaml">UseYaml</a>: <i>Boolean</i>
<a href="#forks" title="Forks">Forks</a>: <i>
      - <a href="forksdefinition.md">ForksDefinition</a></i>
<a href="#override" title="Override">Override</a>: <i>
      - <a href="overridedefinition.md">OverrideDefinition</a></i>
</pre>

## Properties

#### CommentRequired

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialBranch

When use_yaml is true set this to the name of the branch that the azure-pipelines.yml exists on. Defaults to `Managed by Terraform`.
- `forks` - (Required) Set permissions for Forked repositories.
- `override` - (Optional) Override the azure-pipeline file and use this configuration for all builds.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseYaml

Use the azure-pipeline file for the build configuration. Defaults to `false`.
- `initial_branch` - (Optional) When use_yaml is true set this to the name of the branch that the azure-pipelines.yml exists on. Defaults to `Managed by Terraform`.
- `forks` - (Required) Set permissions for Forked repositories.
- `override` - (Optional) Override the azure-pipeline file and use this configuration for all builds.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forks

_Required_: No

_Type_: List of <a href="forksdefinition.md">ForksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Override

_Required_: No

_Type_: List of <a href="overridedefinition.md">OverrideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

