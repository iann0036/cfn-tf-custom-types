# TF::AzureRM::BatchPool StartTaskDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commandline" title="CommandLine">CommandLine</a>" : <i>String</i>,
    "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="environmentdefinition.md">EnvironmentDefinition</a>, ... ]</i>,
    "<a href="#maxtaskretrycount" title="MaxTaskRetryCount">MaxTaskRetryCount</a>" : <i>Double</i>,
    "<a href="#waitforsuccess" title="WaitForSuccess">WaitForSuccess</a>" : <i>Boolean</i>,
    "<a href="#resourcefile" title="ResourceFile">ResourceFile</a>" : <i>[ <a href="resourcefiledefinition.md">ResourceFileDefinition</a>, ... ]</i>,
    "<a href="#useridentity" title="UserIdentity">UserIdentity</a>" : <i>[ <a href="useridentitydefinition.md">UserIdentityDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#commandline" title="CommandLine">CommandLine</a>: <i>String</i>
<a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="environmentdefinition.md">EnvironmentDefinition</a></i>
<a href="#maxtaskretrycount" title="MaxTaskRetryCount">MaxTaskRetryCount</a>: <i>Double</i>
<a href="#waitforsuccess" title="WaitForSuccess">WaitForSuccess</a>: <i>Boolean</i>
<a href="#resourcefile" title="ResourceFile">ResourceFile</a>: <i>
      - <a href="resourcefiledefinition.md">ResourceFileDefinition</a></i>
<a href="#useridentity" title="UserIdentity">UserIdentity</a>: <i>
      - <a href="useridentitydefinition.md">UserIdentityDefinition</a></i>
</pre>

## Properties

#### CommandLine

The command line executed by the start task.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

A map of strings (key,value) that represents the environment variables to set in the start task.

_Required_: No

_Type_: List of <a href="environmentdefinition.md">EnvironmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTaskRetryCount

The number of retry count. Defaults to `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForSuccess

A flag that indicates if the Batch pool should wait for the start task to be completed. Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceFile

_Required_: No

_Type_: List of <a href="resourcefiledefinition.md">ResourceFileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdentity

_Required_: No

_Type_: List of <a href="useridentitydefinition.md">UserIdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

