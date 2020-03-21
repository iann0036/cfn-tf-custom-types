# Terraform::AzureRM::BatchPool StartTask

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commandline" title="CommandLine">CommandLine</a>" : <i>String</i>,
    "<a href="#environment" title="Environment">Environment</a>" : <i>[ &lt;a href=&#34;starttask-environment.md&#34;&gt;Environment&lt;/a&gt;, ... ]</i>,
    "<a href="#maxtaskretrycount" title="MaxTaskRetryCount">MaxTaskRetryCount</a>" : <i>Double</i>,
    "<a href="#waitforsuccess" title="WaitForSuccess">WaitForSuccess</a>" : <i>Boolean</i>,
    "<a href="#resourcefile" title="ResourceFile">ResourceFile</a>" : <i>[ &lt;a href=&#34;starttask-resourcefile.md&#34;&gt;ResourceFile&lt;/a&gt;, ... ]</i>,
    "<a href="#useridentity" title="UserIdentity">UserIdentity</a>" : <i>[ &lt;a href=&#34;starttask-useridentity.md&#34;&gt;UserIdentity&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#commandline" title="CommandLine">CommandLine</a>: <i>String</i>
<a href="#environment" title="Environment">Environment</a>: <i>
      - &lt;a href=&#34;starttask-environment.md&#34;&gt;Environment&lt;/a&gt;</i>
<a href="#maxtaskretrycount" title="MaxTaskRetryCount">MaxTaskRetryCount</a>: <i>Double</i>
<a href="#waitforsuccess" title="WaitForSuccess">WaitForSuccess</a>: <i>Boolean</i>
<a href="#resourcefile" title="ResourceFile">ResourceFile</a>: <i>
      - &lt;a href=&#34;starttask-resourcefile.md&#34;&gt;ResourceFile&lt;/a&gt;</i>
<a href="#useridentity" title="UserIdentity">UserIdentity</a>: <i>
      - &lt;a href=&#34;starttask-useridentity.md&#34;&gt;UserIdentity&lt;/a&gt;</i>
</pre>

## Properties

#### CommandLine

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No
_Type_: List of &lt;a href=&#34;starttask-environment.md&#34;&gt;Environment&lt;/a&gt;

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
_Type_: List of &lt;a href=&#34;starttask-resourcefile.md&#34;&gt;ResourceFile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdentity

_Required_: No
_Type_: List of &lt;a href=&#34;starttask-useridentity.md&#34;&gt;UserIdentity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

