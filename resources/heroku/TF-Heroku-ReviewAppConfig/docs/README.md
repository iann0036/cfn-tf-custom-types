# TF::Heroku::ReviewAppConfig

Provides a resource for configuring review apps. Using this resource also enables review apps for a pipeline.

-> **IMPORTANT!**
This resource can only be used after you create a pipeline, and the pipeline has been connected to a Github repository.
Please visit this [help article](https://devcenter.heroku.com/articles/github-integration-review-apps#setup)
for more information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Heroku::ReviewAppConfig",
    "Properties" : {
        "<a href="#automaticreviewapps" title="AutomaticReviewApps">AutomaticReviewApps</a>" : <i>Boolean</i>,
        "<a href="#basename" title="BaseName">BaseName</a>" : <i>String</i>,
        "<a href="#destroystaleapps" title="DestroyStaleApps">DestroyStaleApps</a>" : <i>Boolean</i>,
        "<a href="#orgrepo" title="OrgRepo">OrgRepo</a>" : <i>String</i>,
        "<a href="#pipelineid" title="PipelineId">PipelineId</a>" : <i>String</i>,
        "<a href="#staledays" title="StaleDays">StaleDays</a>" : <i>Double</i>,
        "<a href="#waitforci" title="WaitForCi">WaitForCi</a>" : <i>Boolean</i>,
        "<a href="#deploytarget" title="DeployTarget">DeployTarget</a>" : <i>[ <a href="deploytargetdefinition.md">DeployTargetDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Heroku::ReviewAppConfig
Properties:
    <a href="#automaticreviewapps" title="AutomaticReviewApps">AutomaticReviewApps</a>: <i>Boolean</i>
    <a href="#basename" title="BaseName">BaseName</a>: <i>String</i>
    <a href="#destroystaleapps" title="DestroyStaleApps">DestroyStaleApps</a>: <i>Boolean</i>
    <a href="#orgrepo" title="OrgRepo">OrgRepo</a>: <i>String</i>
    <a href="#pipelineid" title="PipelineId">PipelineId</a>: <i>String</i>
    <a href="#staledays" title="StaleDays">StaleDays</a>: <i>Double</i>
    <a href="#waitforci" title="WaitForCi">WaitForCi</a>: <i>Boolean</i>
    <a href="#deploytarget" title="DeployTarget">DeployTarget</a>: <i>
      - <a href="deploytargetdefinition.md">DeployTargetDefinition</a></i>
</pre>

## Properties

#### AutomaticReviewApps

If true, this will trigger the creation of review apps when pull-requests
are opened in the repo. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaseName

A unique prefix that will be used to create review app names.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestroyStaleApps

If `true`, this will trigger automatic deletion of review apps when they’re stale.
Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrgRepo

The full_name of the repository that you want to enable review-apps from.
Example `heroku/homebrew-brew`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelineId

The UUID of an existing pipeline.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaleDays

Destroy stale review apps automatically after these many days without any deploys.
Must be set with `destroy_stale_apps` and value needs to be between `1` and `30` inclusive.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForCi

If true, review apps will only be created when CI passes. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployTarget

_Required_: No

_Type_: List of <a href="deploytargetdefinition.md">DeployTargetDefinition</a>

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

Unique identifier of deploy target.
* `type` - (Required) Type of deploy target. Must be either `space` or `region`.

#### RepoId

Returns the <code>RepoId</code> value.

