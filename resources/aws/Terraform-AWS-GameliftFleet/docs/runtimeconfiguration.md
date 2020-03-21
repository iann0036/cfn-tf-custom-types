# Terraform::AWS::GameliftFleet RuntimeConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#gamesessionactivationtimeoutseconds" title="GameSessionActivationTimeoutSeconds">GameSessionActivationTimeoutSeconds</a>" : <i>Double</i>,
    "<a href="#maxconcurrentgamesessionactivations" title="MaxConcurrentGameSessionActivations">MaxConcurrentGameSessionActivations</a>" : <i>Double</i>,
    "<a href="#serverprocess" title="ServerProcess">ServerProcess</a>" : <i>[ &lt;a href=&#34;runtimeconfiguration-serverprocess.md&#34;&gt;ServerProcess&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#gamesessionactivationtimeoutseconds" title="GameSessionActivationTimeoutSeconds">GameSessionActivationTimeoutSeconds</a>: <i>Double</i>
<a href="#maxconcurrentgamesessionactivations" title="MaxConcurrentGameSessionActivations">MaxConcurrentGameSessionActivations</a>: <i>Double</i>
<a href="#serverprocess" title="ServerProcess">ServerProcess</a>: <i>
      - &lt;a href=&#34;runtimeconfiguration-serverprocess.md&#34;&gt;ServerProcess&lt;/a&gt;</i>
</pre>

## Properties

#### GameSessionActivationTimeoutSeconds

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentGameSessionActivations

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerProcess

_Required_: No
_Type_: List of &lt;a href=&#34;runtimeconfiguration-serverprocess.md&#34;&gt;ServerProcess&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

