# TF::AzureDevOps::BuildDefinition

Manages a Build Definition within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::BuildDefinition",
    "Properties" : {
        "<a href="#agentpoolname" title="AgentPoolName">AgentPoolName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#variablegroups" title="VariableGroups">VariableGroups</a>" : <i>[ Double, ... ]</i>,
        "<a href="#citrigger" title="CiTrigger">CiTrigger</a>" : <i>[ <a href="citriggerdefinition.md">CiTriggerDefinition</a>, ... ]</i>,
        "<a href="#pullrequesttrigger" title="PullRequestTrigger">PullRequestTrigger</a>" : <i>[ <a href="pullrequesttriggerdefinition.md">PullRequestTriggerDefinition</a>, ... ]</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>[ <a href="repositorydefinition.md">RepositoryDefinition</a>, ... ]</i>,
        "<a href="#variable" title="Variable">Variable</a>" : <i>[ <a href="variabledefinition.md">VariableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::BuildDefinition
Properties:
    <a href="#agentpoolname" title="AgentPoolName">AgentPoolName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#variablegroups" title="VariableGroups">VariableGroups</a>: <i>
      - Double</i>
    <a href="#citrigger" title="CiTrigger">CiTrigger</a>: <i>
      - <a href="citriggerdefinition.md">CiTriggerDefinition</a></i>
    <a href="#pullrequesttrigger" title="PullRequestTrigger">PullRequestTrigger</a>: <i>
      - <a href="pullrequesttriggerdefinition.md">PullRequestTriggerDefinition</a></i>
    <a href="#repository" title="Repository">Repository</a>: <i>
      - <a href="repositorydefinition.md">RepositoryDefinition</a></i>
    <a href="#variable" title="Variable">Variable</a>: <i>
      - <a href="variabledefinition.md">VariableDefinition</a></i>
</pre>

## Properties

#### AgentPoolName

The agent pool that should execute the build.
- `repository` - (Required) A `repository` block as documented below.
- `ci_trigger` - (Optional) Continuous Integration trigger.
- `pull_request_trigger` - (Optional) Pull Request Integration Integration trigger.
- `variable_groups` - (Optional) A list of variable group IDs (integers) to link to the build definition.
- `variable` - (Optional) A list of `variable` blocks, as documented below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the build definition.
- `path` - (Optional) The folder path of the build definition.
- `agent_pool_name` - (Optional) The agent pool that should execute the build.
- `repository` - (Required) A `repository` block as documented below.
- `ci_trigger` - (Optional) Continuous Integration trigger.
- `pull_request_trigger` - (Optional) Pull Request Integration Integration trigger.
- `variable_groups` - (Optional) A list of variable group IDs (integers) to link to the build definition.
- `variable` - (Optional) A list of `variable` blocks, as documented below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The folder path of the build definition.
- `agent_pool_name` - (Optional) The agent pool that should execute the build.
- `repository` - (Required) A `repository` block as documented below.
- `ci_trigger` - (Optional) Continuous Integration trigger.
- `pull_request_trigger` - (Optional) Pull Request Integration Integration trigger.
- `variable_groups` - (Optional) A list of variable group IDs (integers) to link to the build definition.
- `variable` - (Optional) A list of `variable` blocks, as documented below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID or project name.
- `name` - (Optional) The name of the build definition.
- `path` - (Optional) The folder path of the build definition.
- `agent_pool_name` - (Optional) The agent pool that should execute the build.
- `repository` - (Required) A `repository` block as documented below.
- `ci_trigger` - (Optional) Continuous Integration trigger.
- `pull_request_trigger` - (Optional) Pull Request Integration Integration trigger.
- `variable_groups` - (Optional) A list of variable group IDs (integers) to link to the build definition.
- `variable` - (Optional) A list of `variable` blocks, as documented below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VariableGroups

A list of variable group IDs (integers) to link to the build definition.
- `variable` - (Optional) A list of `variable` blocks, as documented below.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiTrigger

_Required_: No

_Type_: List of <a href="citriggerdefinition.md">CiTriggerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullRequestTrigger

_Required_: No

_Type_: List of <a href="pullrequesttriggerdefinition.md">PullRequestTriggerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

_Required_: No

_Type_: List of <a href="repositorydefinition.md">RepositoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variable

_Required_: No

_Type_: List of <a href="variabledefinition.md">VariableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Revision

Returns the <code>Revision</code> value.

