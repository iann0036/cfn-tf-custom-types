# Terraform::Tfe::Workspace

CloudFormation equivalent of tfe_workspace

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Tfe::Workspace",
    "Properties" : {
        "<a href="#autoapply" title="AutoApply">AutoApply</a>" : <i>Boolean</i>,
        "<a href="#filetriggersenabled" title="FileTriggersEnabled">FileTriggersEnabled</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileTriggersEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operations

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueAllRuns

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerraformVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerPrefixes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingDirectory

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

