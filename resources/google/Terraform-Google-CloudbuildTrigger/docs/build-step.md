# Terraform::Google::CloudbuildTrigger Build Step

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#args" title="Args">Args</a>" : <i>[ String, ... ]</i>,
    "<a href="#dir" title="Dir">Dir</a>" : <i>String</i>,
    "<a href="#entrypoint" title="Entrypoint">Entrypoint</a>" : <i>String</i>,
    "<a href="#env" title="Env">Env</a>" : <i>[ String, ... ]</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#secretenv" title="SecretEnv">SecretEnv</a>" : <i>[ String, ... ]</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>String</i>,
    "<a href="#timing" title="Timing">Timing</a>" : <i>String</i>,
    "<a href="#waitfor" title="WaitFor">WaitFor</a>" : <i>[ String, ... ]</i>,
    "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ <a href="build-step-volumes.md">Volumes</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#args" title="Args">Args</a>: <i>
      - String</i>
<a href="#dir" title="Dir">Dir</a>: <i>String</i>
<a href="#entrypoint" title="Entrypoint">Entrypoint</a>: <i>String</i>
<a href="#env" title="Env">Env</a>: <i>
      - String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#secretenv" title="SecretEnv">SecretEnv</a>: <i>
      - String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>String</i>
<a href="#timing" title="Timing">Timing</a>: <i>String</i>
<a href="#waitfor" title="WaitFor">WaitFor</a>: <i>
      - String</i>
<a href="#volumes" title="Volumes">Volumes</a>: <i>
      - <a href="build-step-volumes.md">Volumes</a></i>
</pre>

## Properties

#### Args

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entrypoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretEnv

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timing

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitFor

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No

_Type_: List of <a href="build-step-volumes.md">Volumes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

