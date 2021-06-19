# TF::AWS::AmplifyApp AutoBranchCreationConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#basicauthcredentials" title="BasicAuthCredentials">BasicAuthCredentials</a>" : <i>String</i>,
    "<a href="#buildspec" title="BuildSpec">BuildSpec</a>" : <i>String</i>,
    "<a href="#enableautobuild" title="EnableAutoBuild">EnableAutoBuild</a>" : <i>Boolean</i>,
    "<a href="#enablebasicauth" title="EnableBasicAuth">EnableBasicAuth</a>" : <i>Boolean</i>,
    "<a href="#enableperformancemode" title="EnablePerformanceMode">EnablePerformanceMode</a>" : <i>Boolean</i>,
    "<a href="#enablepullrequestpreview" title="EnablePullRequestPreview">EnablePullRequestPreview</a>" : <i>Boolean</i>,
    "<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>" : <i>[ <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>, ... ]</i>,
    "<a href="#framework" title="Framework">Framework</a>" : <i>String</i>,
    "<a href="#pullrequestenvironmentname" title="PullRequestEnvironmentName">PullRequestEnvironmentName</a>" : <i>String</i>,
    "<a href="#stage" title="Stage">Stage</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#basicauthcredentials" title="BasicAuthCredentials">BasicAuthCredentials</a>: <i>String</i>
<a href="#buildspec" title="BuildSpec">BuildSpec</a>: <i>String</i>
<a href="#enableautobuild" title="EnableAutoBuild">EnableAutoBuild</a>: <i>Boolean</i>
<a href="#enablebasicauth" title="EnableBasicAuth">EnableBasicAuth</a>: <i>Boolean</i>
<a href="#enableperformancemode" title="EnablePerformanceMode">EnablePerformanceMode</a>: <i>Boolean</i>
<a href="#enablepullrequestpreview" title="EnablePullRequestPreview">EnablePullRequestPreview</a>: <i>Boolean</i>
<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>: <i>
      - <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a></i>
<a href="#framework" title="Framework">Framework</a>: <i>String</i>
<a href="#pullrequestenvironmentname" title="PullRequestEnvironmentName">PullRequestEnvironmentName</a>: <i>String</i>
<a href="#stage" title="Stage">Stage</a>: <i>String</i>
</pre>

## Properties

#### BasicAuthCredentials

The basic authorization credentials for the autocreated branch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildSpec

The build specification (build spec) for the autocreated branch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoBuild

Enables auto building for the autocreated branch.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBasicAuth

Enables basic authorization for the autocreated branch.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePerformanceMode

Enables performance mode for the branch.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePullRequestPreview

Enables pull request previews for the autocreated branch.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariables

_Required_: No

_Type_: List of <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Framework

The framework for the autocreated branch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullRequestEnvironmentName

The Amplify environment name for the pull request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stage

Describes the current stage for the autocreated branch. Valid values: `PRODUCTION`, `BETA`, `DEVELOPMENT`, `EXPERIMENTAL`, `PULL_REQUEST`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

