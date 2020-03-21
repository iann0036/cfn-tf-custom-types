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

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitCloneDepth

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsecureSsl

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportBuildStatus

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

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

