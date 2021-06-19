# TF::Buildkite::Pipeline

CloudFormation equivalent of buildkite_pipeline

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Buildkite::Pipeline",
    "Properties" : {
        "<a href="#branchconfiguration" title="BranchConfiguration">BranchConfiguration</a>" : <i>String</i>,
        "<a href="#cancelintermediatebuilds" title="CancelIntermediateBuilds">CancelIntermediateBuilds</a>" : <i>Boolean</i>,
        "<a href="#cancelintermediatebuildsbranchfilter" title="CancelIntermediateBuildsBranchFilter">CancelIntermediateBuildsBranchFilter</a>" : <i>String</i>,
        "<a href="#defaultbranch" title="DefaultBranch">DefaultBranch</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#skipintermediatebuilds" title="SkipIntermediateBuilds">SkipIntermediateBuilds</a>" : <i>Boolean</i>,
        "<a href="#skipintermediatebuildsbranchfilter" title="SkipIntermediateBuildsBranchFilter">SkipIntermediateBuildsBranchFilter</a>" : <i>String</i>,
        "<a href="#steps" title="Steps">Steps</a>" : <i>String</i>,
        "<a href="#team" title="Team">Team</a>" : <i>[ <a href="teamdefinition.md">TeamDefinition</a>, ... ]</i>,
        "<a href="#providersettings" title="ProviderSettings">ProviderSettings</a>" : <i>[ <a href="providersettingsdefinition.md">ProviderSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Buildkite::Pipeline
Properties:
    <a href="#branchconfiguration" title="BranchConfiguration">BranchConfiguration</a>: <i>String</i>
    <a href="#cancelintermediatebuilds" title="CancelIntermediateBuilds">CancelIntermediateBuilds</a>: <i>Boolean</i>
    <a href="#cancelintermediatebuildsbranchfilter" title="CancelIntermediateBuildsBranchFilter">CancelIntermediateBuildsBranchFilter</a>: <i>String</i>
    <a href="#defaultbranch" title="DefaultBranch">DefaultBranch</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#skipintermediatebuilds" title="SkipIntermediateBuilds">SkipIntermediateBuilds</a>: <i>Boolean</i>
    <a href="#skipintermediatebuildsbranchfilter" title="SkipIntermediateBuildsBranchFilter">SkipIntermediateBuildsBranchFilter</a>: <i>String</i>
    <a href="#steps" title="Steps">Steps</a>: <i>String</i>
    <a href="#team" title="Team">Team</a>: <i>
      - <a href="teamdefinition.md">TeamDefinition</a></i>
    <a href="#providersettings" title="ProviderSettings">ProviderSettings</a>: <i>
      - <a href="providersettingsdefinition.md">ProviderSettingsDefinition</a></i>
</pre>

## Properties

#### BranchConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CancelIntermediateBuilds

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CancelIntermediateBuildsBranchFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultBranch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipIntermediateBuilds

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipIntermediateBuildsBranchFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Steps

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Team

_Required_: No

_Type_: List of <a href="teamdefinition.md">TeamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderSettings

_Required_: No

_Type_: List of <a href="providersettingsdefinition.md">ProviderSettingsDefinition</a>

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

#### Slug

Returns the <code>Slug</code> value.

#### WebhookUrl

Returns the <code>WebhookUrl</code> value.

