# Terraform::AzureRM::BatchPool StartTask

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commandline" title="CommandLine">CommandLine</a>" : <i>String</i>,
    "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="starttask-environment.md">Environment</a>, ... ]</i>,
    "<a href="#maxtaskretrycount" title="MaxTaskRetryCount">MaxTaskRetryCount</a>" : <i>Double</i>,
    "<a href="#waitforsuccess" title="WaitForSuccess">WaitForSuccess</a>" : <i>Boolean</i>,
    "<a href="#resourcefile" title="ResourceFile">ResourceFile</a>" : <i>[ <a href="starttask-resourcefile.md">ResourceFile</a>, ... ]</i>,
    "<a href="#useridentity" title="UserIdentity">UserIdentity</a>" : <i>[ <a href="starttask-useridentity.md">UserIdentity</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#commandline" title="CommandLine">CommandLine</a>: <i>String</i>
<a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="starttask-environment.md">Environment</a></i>
<a href="#maxtaskretrycount" title="MaxTaskRetryCount">MaxTaskRetryCount</a>: <i>Double</i>
<a href="#waitforsuccess" title="WaitForSuccess">WaitForSuccess</a>: <i>Boolean</i>
<a href="#resourcefile" title="ResourceFile">ResourceFile</a>: <i>
      - <a href="starttask-resourcefile.md">ResourceFile</a></i>
<a href="#useridentity" title="UserIdentity">UserIdentity</a>: <i>
      - <a href="starttask-useridentity.md">UserIdentity</a></i>
</pre>

## Properties

#### CommandLine

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No

_Type_: List of <a href="starttask-environment.md">Environment</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTaskRetryCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForSuccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceFile

_Required_: No

_Type_: List of <a href="starttask-resourcefile.md">ResourceFile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdentity

_Required_: No

_Type_: List of <a href="starttask-useridentity.md">UserIdentity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

