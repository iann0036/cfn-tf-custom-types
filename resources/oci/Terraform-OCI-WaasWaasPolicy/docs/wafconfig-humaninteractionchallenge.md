# Terraform::OCI::WaasWaasPolicy WafConfig HumanInteractionChallenge

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#actionexpirationinseconds" title="ActionExpirationInSeconds">ActionExpirationInSeconds</a>" : <i>Double</i>,
    "<a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>" : <i>Double</i>,
    "<a href="#failurethresholdexpirationinseconds" title="FailureThresholdExpirationInSeconds">FailureThresholdExpirationInSeconds</a>" : <i>Double</i>,
    "<a href="#interactionthreshold" title="InteractionThreshold">InteractionThreshold</a>" : <i>Double</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#recordingperiodinseconds" title="RecordingPeriodInSeconds">RecordingPeriodInSeconds</a>" : <i>Double</i>,
    "<a href="#challengesettings" title="ChallengeSettings">ChallengeSettings</a>" : <i>[ <a href="wafconfig-humaninteractionchallenge-challengesettings.md">ChallengeSettings</a>, ... ]</i>,
    "<a href="#sethttpheader" title="SetHttpHeader">SetHttpHeader</a>" : <i>[ <a href="wafconfig-humaninteractionchallenge-sethttpheader.md">SetHttpHeader</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#actionexpirationinseconds" title="ActionExpirationInSeconds">ActionExpirationInSeconds</a>: <i>Double</i>
<a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>: <i>Double</i>
<a href="#failurethresholdexpirationinseconds" title="FailureThresholdExpirationInSeconds">FailureThresholdExpirationInSeconds</a>: <i>Double</i>
<a href="#interactionthreshold" title="InteractionThreshold">InteractionThreshold</a>: <i>Double</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#recordingperiodinseconds" title="RecordingPeriodInSeconds">RecordingPeriodInSeconds</a>: <i>Double</i>
<a href="#challengesettings" title="ChallengeSettings">ChallengeSettings</a>: <i>
      - <a href="wafconfig-humaninteractionchallenge-challengesettings.md">ChallengeSettings</a></i>
<a href="#sethttpheader" title="SetHttpHeader">SetHttpHeader</a>: <i>
      - <a href="wafconfig-humaninteractionchallenge-sethttpheader.md">SetHttpHeader</a></i>
</pre>

## Properties

#### Action

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionExpirationInSeconds

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureThreshold

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureThresholdExpirationInSeconds

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InteractionThreshold

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordingPeriodInSeconds

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChallengeSettings

_Required_: No
_Type_: List of <a href="wafconfig-humaninteractionchallenge-challengesettings.md">ChallengeSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetHttpHeader

_Required_: No
_Type_: List of <a href="wafconfig-humaninteractionchallenge-sethttpheader.md">SetHttpHeader</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

