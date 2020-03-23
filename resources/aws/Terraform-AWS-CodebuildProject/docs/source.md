# Terraform::AWS::CodebuildProject Source

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#buildspec" title="Buildspec">Buildspec</a>" : <i>String</i>,
    "<a href="#gitclonedepth" title="GitCloneDepth">GitCloneDepth</a>" : <i>Double</i>,
    "<a href="#insecuressl" title="InsecureSsl">InsecureSsl</a>" : <i>Boolean</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#reportbuildstatus" title="ReportBuildStatus">ReportBuildStatus</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#auth" title="Auth">Auth</a>" : <i>[ <a href="source-auth.md">Auth</a>, ... ]</i>,
    "<a href="#gitsubmodulesconfig" title="GitSubmodulesConfig">GitSubmodulesConfig</a>" : <i>[ <a href="source-gitsubmodulesconfig.md">GitSubmodulesConfig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#buildspec" title="Buildspec">Buildspec</a>: <i>String</i>
<a href="#gitclonedepth" title="GitCloneDepth">GitCloneDepth</a>: <i>Double</i>
<a href="#insecuressl" title="InsecureSsl">InsecureSsl</a>: <i>Boolean</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#reportbuildstatus" title="ReportBuildStatus">ReportBuildStatus</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#auth" title="Auth">Auth</a>: <i>
      - <a href="source-auth.md">Auth</a></i>
<a href="#gitsubmodulesconfig" title="GitSubmodulesConfig">GitSubmodulesConfig</a>: <i>
      - <a href="source-gitsubmodulesconfig.md">GitSubmodulesConfig</a></i>
</pre>

## Properties

#### Buildspec

The build spec declaration to use for this build project's related builds. This must be set when `type` is `NO_SOURCE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitCloneDepth

Truncate git history to this many commits.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsecureSsl

Ignore SSL warnings when connecting to source control.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location of the source code from git or s3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportBuildStatus

Set to `true` to report the status of a build's start and finish to your source provider. This option is only valid when the `type` is `BITBUCKET` or `GITHUB`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET`, `S3` or `NO_SOURCE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Auth

_Required_: No

_Type_: List of <a href="source-auth.md">Auth</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitSubmodulesConfig

_Required_: No

_Type_: List of <a href="source-gitsubmodulesconfig.md">GitSubmodulesConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

