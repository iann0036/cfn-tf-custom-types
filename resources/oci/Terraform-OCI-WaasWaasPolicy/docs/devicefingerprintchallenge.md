# Terraform::OCI::WaasWaasPolicy DeviceFingerprintChallenge

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#actionexpirationinseconds" title="ActionExpirationInSeconds">ActionExpirationInSeconds</a>" : <i>Double</i>,
    "<a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>" : <i>Double</i>,
    "<a href="#failurethresholdexpirationinseconds" title="FailureThresholdExpirationInSeconds">FailureThresholdExpirationInSeconds</a>" : <i>Double</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#maxaddresscount" title="MaxAddressCount">MaxAddressCount</a>" : <i>Double</i>,
    "<a href="#maxaddresscountexpirationinseconds" title="MaxAddressCountExpirationInSeconds">MaxAddressCountExpirationInSeconds</a>" : <i>Double</i>,
    "<a href="#challengesettings" title="ChallengeSettings">ChallengeSettings</a>" : <i>[ &lt;a href=&#34;devicefingerprintchallenge-challengesettings.md&#34;&gt;ChallengeSettings&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#actionexpirationinseconds" title="ActionExpirationInSeconds">ActionExpirationInSeconds</a>: <i>Double</i>
<a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>: <i>Double</i>
<a href="#failurethresholdexpirationinseconds" title="FailureThresholdExpirationInSeconds">FailureThresholdExpirationInSeconds</a>: <i>Double</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#maxaddresscount" title="MaxAddressCount">MaxAddressCount</a>: <i>Double</i>
<a href="#maxaddresscountexpirationinseconds" title="MaxAddressCountExpirationInSeconds">MaxAddressCountExpirationInSeconds</a>: <i>Double</i>
<a href="#challengesettings" title="ChallengeSettings">ChallengeSettings</a>: <i>
      - &lt;a href=&#34;devicefingerprintchallenge-challengesettings.md&#34;&gt;ChallengeSettings&lt;/a&gt;</i>
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

#### IsEnabled

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAddressCount

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAddressCountExpirationInSeconds

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChallengeSettings

_Required_: No
_Type_: List of &lt;a href=&#34;devicefingerprintchallenge-challengesettings.md&#34;&gt;ChallengeSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

