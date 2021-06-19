# TF::AWS::GameliftFleet RuntimeConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#gamesessionactivationtimeoutseconds" title="GameSessionActivationTimeoutSeconds">GameSessionActivationTimeoutSeconds</a>" : <i>Double</i>,
    "<a href="#maxconcurrentgamesessionactivations" title="MaxConcurrentGameSessionActivations">MaxConcurrentGameSessionActivations</a>" : <i>Double</i>,
    "<a href="#serverprocess" title="ServerProcess">ServerProcess</a>" : <i>[ <a href="serverprocessdefinition.md">ServerProcessDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#gamesessionactivationtimeoutseconds" title="GameSessionActivationTimeoutSeconds">GameSessionActivationTimeoutSeconds</a>: <i>Double</i>
<a href="#maxconcurrentgamesessionactivations" title="MaxConcurrentGameSessionActivations">MaxConcurrentGameSessionActivations</a>: <i>Double</i>
<a href="#serverprocess" title="ServerProcess">ServerProcess</a>: <i>
      - <a href="serverprocessdefinition.md">ServerProcessDefinition</a></i>
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

_Type_: List of <a href="serverprocessdefinition.md">ServerProcessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

