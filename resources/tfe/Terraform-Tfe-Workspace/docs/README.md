# Terraform::Tfe::Workspace

Provides a workspace resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Tfe::Workspace",
    "Properties" : {
        "<a href="#autoapply" title="AutoApply">AutoApply</a>" : <i>Boolean</i>,
        "<a href="#filetriggersenabled" title="FileTriggersEnabled">FileTriggersEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#operations" title="Operations">Operations</a>" : <i>Boolean</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#queueallruns" title="QueueAllRuns">QueueAllRuns</a>" : <i>Boolean</i>,
        "<a href="#sshkeyid" title="SshKeyId">SshKeyId</a>" : <i>String</i>,
        "<a href="#terraformversion" title="TerraformVersion">TerraformVersion</a>" : <i>String</i>,
        "<a href="#triggerprefixes" title="TriggerPrefixes">TriggerPrefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#workingdirectory" title="WorkingDirectory">WorkingDirectory</a>" : <i>String</i>,
        "<a href="#vcsrepo" title="VcsRepo">VcsRepo</a>" : <i>[ <a href="vcsrepo.md">VcsRepo</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Tfe::Workspace
Properties:
    <a href="#autoapply" title="AutoApply">AutoApply</a>: <i>Boolean</i>
    <a href="#filetriggersenabled" title="FileTriggersEnabled">FileTriggersEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#operations" title="Operations">Operations</a>: <i>Boolean</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#queueallruns" title="QueueAllRuns">QueueAllRuns</a>: <i>Boolean</i>
    <a href="#sshkeyid" title="SshKeyId">SshKeyId</a>: <i>String</i>
    <a href="#terraformversion" title="TerraformVersion">TerraformVersion</a>: <i>String</i>
    <a href="#triggerprefixes" title="TriggerPrefixes">TriggerPrefixes</a>: <i>
      - String</i>
    <a href="#workingdirectory" title="WorkingDirectory">WorkingDirectory</a>: <i>String</i>
    <a href="#vcsrepo" title="VcsRepo">VcsRepo</a>: <i>
      - <a href="vcsrepo.md">VcsRepo</a></i>
</pre>

## Properties

#### AutoApply

Whether to automatically apply changes when a
Terraform plan is successful. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileTriggersEnabled

Whether to filter runs based on the changed files in a VCS push. If enabled, the working directory and trigger prefixes describe a set of paths which must contain changes for a VCS push to trigger a run. If disabled, any push will trigger a run. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the workspace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operations

Whether to use remote execution mode. When set
to `false`, the workspace will be used for state storage only.
Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

Name of the organization.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueAllRuns

Whether all runs should be queued. When set
to `false`, runs triggered by a VCS change will not be queued until at least
one run is manually queued. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyId

The ID of an SSH key to assign to the workspace.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerraformVersion

The version of Terraform to use for this workspace. Defaults to the latest available version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerPrefixes

List of repository-root-relative paths which describe all locations to be tracked for changes.

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

_Type_: List of <a href="vcsrepo.md">VcsRepo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ExternalId

Returns the <code>ExternalId</code> value.

