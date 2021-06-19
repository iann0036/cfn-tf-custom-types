# TF::AWS::AmplifyApp

Provides an Amplify App resource, a fullstack serverless app hosted on the [AWS Amplify Console](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html).

~> **Note:** When you create/update an Amplify App from Terraform, you may end up with the error "BadRequestException: You should at least provide one valid token" because of authentication issues. See the section "Repository with Tokens" below.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AmplifyApp",
    "Properties" : {
        "<a href="#accesstoken" title="AccessToken">AccessToken</a>" : <i>String</i>,
        "<a href="#autobranchcreationpatterns" title="AutoBranchCreationPatterns">AutoBranchCreationPatterns</a>" : <i>[ String, ... ]</i>,
        "<a href="#basicauthcredentials" title="BasicAuthCredentials">BasicAuthCredentials</a>" : <i>String</i>,
        "<a href="#buildspec" title="BuildSpec">BuildSpec</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enableautobranchcreation" title="EnableAutoBranchCreation">EnableAutoBranchCreation</a>" : <i>Boolean</i>,
        "<a href="#enablebasicauth" title="EnableBasicAuth">EnableBasicAuth</a>" : <i>Boolean</i>,
        "<a href="#enablebranchautobuild" title="EnableBranchAutoBuild">EnableBranchAutoBuild</a>" : <i>Boolean</i>,
        "<a href="#enablebranchautodeletion" title="EnableBranchAutoDeletion">EnableBranchAutoDeletion</a>" : <i>Boolean</i>,
        "<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>" : <i>[ <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>, ... ]</i>,
        "<a href="#iamservicerolearn" title="IamServiceRoleArn">IamServiceRoleArn</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oauthtoken" title="OauthToken">OauthToken</a>" : <i>String</i>,
        "<a href="#platform" title="Platform">Platform</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#autobranchcreationconfig" title="AutoBranchCreationConfig">AutoBranchCreationConfig</a>" : <i>[ <a href="autobranchcreationconfigdefinition.md">AutoBranchCreationConfigDefinition</a>, ... ]</i>,
        "<a href="#customrule" title="CustomRule">CustomRule</a>" : <i>[ <a href="customruledefinition.md">CustomRuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AmplifyApp
Properties:
    <a href="#accesstoken" title="AccessToken">AccessToken</a>: <i>String</i>
    <a href="#autobranchcreationpatterns" title="AutoBranchCreationPatterns">AutoBranchCreationPatterns</a>: <i>
      - String</i>
    <a href="#basicauthcredentials" title="BasicAuthCredentials">BasicAuthCredentials</a>: <i>String</i>
    <a href="#buildspec" title="BuildSpec">BuildSpec</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enableautobranchcreation" title="EnableAutoBranchCreation">EnableAutoBranchCreation</a>: <i>Boolean</i>
    <a href="#enablebasicauth" title="EnableBasicAuth">EnableBasicAuth</a>: <i>Boolean</i>
    <a href="#enablebranchautobuild" title="EnableBranchAutoBuild">EnableBranchAutoBuild</a>: <i>Boolean</i>
    <a href="#enablebranchautodeletion" title="EnableBranchAutoDeletion">EnableBranchAutoDeletion</a>: <i>Boolean</i>
    <a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>: <i>
      - <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a></i>
    <a href="#iamservicerolearn" title="IamServiceRoleArn">IamServiceRoleArn</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oauthtoken" title="OauthToken">OauthToken</a>: <i>String</i>
    <a href="#platform" title="Platform">Platform</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#autobranchcreationconfig" title="AutoBranchCreationConfig">AutoBranchCreationConfig</a>: <i>
      - <a href="autobranchcreationconfigdefinition.md">AutoBranchCreationConfigDefinition</a></i>
    <a href="#customrule" title="CustomRule">CustomRule</a>: <i>
      - <a href="customruledefinition.md">CustomRuleDefinition</a></i>
</pre>

## Properties

#### AccessToken

The personal access token for a third-party source control system for an Amplify app. The personal access token is used to create a webhook and a read-only deploy key. The token is not stored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoBranchCreationPatterns

The automated branch creation glob patterns for an Amplify app.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAuthCredentials

The credentials for basic authorization for an Amplify app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildSpec

The [build specification](https://docs.aws.amazon.com/amplify/latest/userguide/build-settings.html) (build spec) for an Amplify app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description for an Amplify app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoBranchCreation

Enables automated branch creation for an Amplify app.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBasicAuth

Enables basic authorization for an Amplify app. This will apply to all branches that are part of this app.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBranchAutoBuild

Enables auto-building of branches for the Amplify App.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBranchAutoDeletion

Automatically disconnects a branch in the Amplify Console when you delete a branch from your Git repository.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariables

The environment variables map for an Amplify app.

_Required_: No

_Type_: List of <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamServiceRoleArn

The AWS Identity and Access Management (IAM) service role for an Amplify app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name for an Amplify app.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthToken

The OAuth token for a third-party source control system for an Amplify app. The OAuth token is used to create a webhook and a read-only deploy key. The OAuth token is not stored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platform

The platform or framework for an Amplify app. Valid values: `WEB`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

The repository for an Amplify app.

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

#### AutoBranchCreationConfig

_Required_: No

_Type_: List of <a href="autobranchcreationconfigdefinition.md">AutoBranchCreationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomRule

_Required_: No

_Type_: List of <a href="customruledefinition.md">CustomRuleDefinition</a>

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

#### DefaultDomain

Returns the <code>DefaultDomain</code> value.

#### Id

Returns the <code>Id</code> value.

#### ProductionBranch

Returns the <code>ProductionBranch</code> value.

