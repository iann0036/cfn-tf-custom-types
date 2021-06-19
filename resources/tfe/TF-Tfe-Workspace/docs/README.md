# TF::Tfe::Workspace

Provides a workspace resource.

~> **NOTE:** Using `global_remote_state` or `remote_state_consumer_ids` requires using the provider with Terraform Cloud or an instance of Terraform Enterprise at least as recent as v202104-1.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Tfe::Workspace",
    "Properties" : {
        "<a href="#agentpoolid" title="AgentPoolId">AgentPoolId</a>" : <i>String</i>,
        "<a href="#allowdestroyplan" title="AllowDestroyPlan">AllowDestroyPlan</a>" : <i>Boolean</i>,
        "<a href="#autoapply" title="AutoApply">AutoApply</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#executionmode" title="ExecutionMode">ExecutionMode</a>" : <i>String</i>,
        "<a href="#filetriggersenabled" title="FileTriggersEnabled">FileTriggersEnabled</a>" : <i>Boolean</i>,
        "<a href="#globalremotestate" title="GlobalRemoteState">GlobalRemoteState</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#operations" title="Operations">Operations</a>" : <i>Boolean</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#queueallruns" title="QueueAllRuns">QueueAllRuns</a>" : <i>Boolean</i>,
        "<a href="#remotestateconsumerids" title="RemoteStateConsumerIds">RemoteStateConsumerIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#speculativeenabled" title="SpeculativeEnabled">SpeculativeEnabled</a>" : <i>Boolean</i>,
        "<a href="#sshkeyid" title="SshKeyId">SshKeyId</a>" : <i>String</i>,
        "<a href="#terraformversion" title="TerraformVersion">TerraformVersion</a>" : <i>String</i>,
        "<a href="#triggerprefixes" title="TriggerPrefixes">TriggerPrefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#workingdirectory" title="WorkingDirectory">WorkingDirectory</a>" : <i>String</i>,
        "<a href="#vcsrepo" title="VcsRepo">VcsRepo</a>" : <i>[ <a href="vcsrepodefinition.md">VcsRepoDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Tfe::Workspace
Properties:
    <a href="#agentpoolid" title="AgentPoolId">AgentPoolId</a>: <i>String</i>
    <a href="#allowdestroyplan" title="AllowDestroyPlan">AllowDestroyPlan</a>: <i>Boolean</i>
    <a href="#autoapply" title="AutoApply">AutoApply</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#executionmode" title="ExecutionMode">ExecutionMode</a>: <i>String</i>
    <a href="#filetriggersenabled" title="FileTriggersEnabled">FileTriggersEnabled</a>: <i>Boolean</i>
    <a href="#globalremotestate" title="GlobalRemoteState">GlobalRemoteState</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#operations" title="Operations">Operations</a>: <i>Boolean</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#queueallruns" title="QueueAllRuns">QueueAllRuns</a>: <i>Boolean</i>
    <a href="#remotestateconsumerids" title="RemoteStateConsumerIds">RemoteStateConsumerIds</a>: <i>
      - String</i>
    <a href="#speculativeenabled" title="SpeculativeEnabled">SpeculativeEnabled</a>: <i>Boolean</i>
    <a href="#sshkeyid" title="SshKeyId">SshKeyId</a>: <i>String</i>
    <a href="#terraformversion" title="TerraformVersion">TerraformVersion</a>: <i>String</i>
    <a href="#triggerprefixes" title="TriggerPrefixes">TriggerPrefixes</a>: <i>
      - String</i>
    <a href="#workingdirectory" title="WorkingDirectory">WorkingDirectory</a>: <i>String</i>
    <a href="#vcsrepo" title="VcsRepo">VcsRepo</a>: <i>
      - <a href="vcsrepodefinition.md">VcsRepoDefinition</a></i>
</pre>

## Properties

#### AgentPoolId

The ID of an agent pool to assign to the workspace. Requires `execution_mode`
to be set to `agent`. This value _must not_ be provided if `execution_mode` is set to any other value or if `operations` is
provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowDestroyPlan

Whether destroy plans can be queued on the workspace.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoApply

Whether to automatically apply changes when a
Terraform plan is successful. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description for the workspace.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionMode

Which [execution mode](https://www.terraform.io/docs/cloud/workspaces/settings.html#execution-mode) to use. Using Terraform Cloud, valid
values are `remote`, `local` or `agent`. Using Terraform Enterprise, only `remote` and `local` execution modes are
valid.  When set to `local`, the workspace will be used for state storage only. Defaults to `remote`. This value _must
not_ be provided if `operations` is provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileTriggersEnabled

Whether to filter runs based on the changed files
in a VCS push. If enabled, the working directory and trigger prefixes describe a set of
paths which must contain changes for a VCS push to trigger a run. If disabled, any push will
trigger a run. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalRemoteState

Whether the workspace allows all workspaces in the organization to access its state data during runs. If false, then only specifically approved workspaces can access its state (`remote_state_consumer_ids`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the workspace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operations

**Deprecated** Whether to use remote execution mode. When set to `false`, the workspace will
be used for state storage only. Defaults to `true`. This value _must not_ be provided if `execution_mode` is
provided.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

Name of the organization.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueAllRuns

Whether the workspace should start automatically performing
runs immediately after its creation. When set to `false`, runs triggered by a webhook
(such as a commit in VCS) will not be queued until at least one run has been manually
queued. Defaults to `true`. **Note:** This default differs from the Terraform Cloud API default, which is `false`.
The provider uses `true` as any workspace provisioned with `false` would need to then have a run manually queued out-of-band
before accepting webhooks.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteStateConsumerIds

The set of workspace IDs set as explicit remote state consumers for the given workspace.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpeculativeEnabled

Whether this workspace allows speculative
plans. Setting this to `false` prevents Terraform Cloud or the Terraform
Enterprise instance from running plans on pull requests, which can improve
security if the VCS repository is public or includes untrusted contributors.
Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyId

The ID of an SSH key to assign to the workspace.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerraformVersion

The version of Terraform to use for this workspace. Defaults to
the latest available version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerPrefixes

List of repository-root-relative paths which describe all locations
to be tracked for changes.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingDirectory

A relative path that Terraform will execute
within.  Defaults to the root of your repository.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcsRepo

_Required_: No

_Type_: List of <a href="vcsrepodefinition.md">VcsRepoDefinition</a>

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

