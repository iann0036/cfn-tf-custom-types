# TF::AWS::AmplifyBranch

Provides an Amplify Branch resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AmplifyBranch",
    "Properties" : {
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#backendenvironmentarn" title="BackendEnvironmentArn">BackendEnvironmentArn</a>" : <i>String</i>,
        "<a href="#basicauthcredentials" title="BasicAuthCredentials">BasicAuthCredentials</a>" : <i>String</i>,
        "<a href="#branchname" title="BranchName">BranchName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#enableautobuild" title="EnableAutoBuild">EnableAutoBuild</a>" : <i>Boolean</i>,
        "<a href="#enablebasicauth" title="EnableBasicAuth">EnableBasicAuth</a>" : <i>Boolean</i>,
        "<a href="#enablenotification" title="EnableNotification">EnableNotification</a>" : <i>Boolean</i>,
        "<a href="#enableperformancemode" title="EnablePerformanceMode">EnablePerformanceMode</a>" : <i>Boolean</i>,
        "<a href="#enablepullrequestpreview" title="EnablePullRequestPreview">EnablePullRequestPreview</a>" : <i>Boolean</i>,
        "<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>" : <i>[ <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>, ... ]</i>,
        "<a href="#framework" title="Framework">Framework</a>" : <i>String</i>,
        "<a href="#pullrequestenvironmentname" title="PullRequestEnvironmentName">PullRequestEnvironmentName</a>" : <i>String</i>,
        "<a href="#stage" title="Stage">Stage</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AmplifyBranch
Properties:
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#backendenvironmentarn" title="BackendEnvironmentArn">BackendEnvironmentArn</a>: <i>String</i>
    <a href="#basicauthcredentials" title="BasicAuthCredentials">BasicAuthCredentials</a>: <i>String</i>
    <a href="#branchname" title="BranchName">BranchName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#enableautobuild" title="EnableAutoBuild">EnableAutoBuild</a>: <i>Boolean</i>
    <a href="#enablebasicauth" title="EnableBasicAuth">EnableBasicAuth</a>: <i>Boolean</i>
    <a href="#enablenotification" title="EnableNotification">EnableNotification</a>: <i>Boolean</i>
    <a href="#enableperformancemode" title="EnablePerformanceMode">EnablePerformanceMode</a>: <i>Boolean</i>
    <a href="#enablepullrequestpreview" title="EnablePullRequestPreview">EnablePullRequestPreview</a>: <i>Boolean</i>
    <a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>: <i>
      - <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a></i>
    <a href="#framework" title="Framework">Framework</a>: <i>String</i>
    <a href="#pullrequestenvironmentname" title="PullRequestEnvironmentName">PullRequestEnvironmentName</a>: <i>String</i>
    <a href="#stage" title="Stage">Stage</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>String</i>
</pre>

## Properties

#### AppId

The unique ID for an Amplify app.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendEnvironmentArn

The Amazon Resource Name (ARN) for a backend environment that is part of an Amplify app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAuthCredentials

The basic authorization credentials for the branch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BranchName

The name for the branch.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description for the branch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name for a branch. This is used as the default domain prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoBuild

Enables auto building for the branch.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBasicAuth

Enables basic authorization for the branch.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNotification

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePerformanceMode

Enables performance mode for the branch.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePullRequestPreview

Enables pull request previews for this branch.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariables

The environment variables for the branch.

_Required_: No

_Type_: List of <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Framework

The framework for the branch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullRequestEnvironmentName

The Amplify environment name for the pull request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stage

Describes the current stage for the branch. Valid values: `PRODUCTION`, `BETA`, `DEVELOPMENT`, `EXPERIMENTAL`, `PULL_REQUEST`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

The content Time To Live (TTL) for the website in seconds.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### AssociatedResources

Returns the <code>AssociatedResources</code> value.

#### CustomDomains

Returns the <code>CustomDomains</code> value.

#### DestinationBranch

Returns the <code>DestinationBranch</code> value.

#### Id

Returns the <code>Id</code> value.

#### SourceBranch

Returns the <code>SourceBranch</code> value.

