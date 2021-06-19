# TF::Datadog::SyntheticsTest OptionsListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acceptselfsigned" title="AcceptSelfSigned">AcceptSelfSigned</a>" : <i>Boolean</i>,
    "<a href="#allowinsecure" title="AllowInsecure">AllowInsecure</a>" : <i>Boolean</i>,
    "<a href="#followredirects" title="FollowRedirects">FollowRedirects</a>" : <i>Boolean</i>,
    "<a href="#minfailureduration" title="MinFailureDuration">MinFailureDuration</a>" : <i>Double</i>,
    "<a href="#minlocationfailed" title="MinLocationFailed">MinLocationFailed</a>" : <i>Double</i>,
    "<a href="#monitorname" title="MonitorName">MonitorName</a>" : <i>String</i>,
    "<a href="#monitorpriority" title="MonitorPriority">MonitorPriority</a>" : <i>Double</i>,
    "<a href="#noscreenshot" title="NoScreenshot">NoScreenshot</a>" : <i>Boolean</i>,
    "<a href="#tickevery" title="TickEvery">TickEvery</a>" : <i>Double</i>,
    "<a href="#monitoroptions" title="MonitorOptions">MonitorOptions</a>" : <i>[ <a href="monitoroptionsdefinition.md">MonitorOptionsDefinition</a>, ... ]</i>,
    "<a href="#retry" title="Retry">Retry</a>" : <i>[ <a href="retrydefinition.md">RetryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#acceptselfsigned" title="AcceptSelfSigned">AcceptSelfSigned</a>: <i>Boolean</i>
<a href="#allowinsecure" title="AllowInsecure">AllowInsecure</a>: <i>Boolean</i>
<a href="#followredirects" title="FollowRedirects">FollowRedirects</a>: <i>Boolean</i>
<a href="#minfailureduration" title="MinFailureDuration">MinFailureDuration</a>: <i>Double</i>
<a href="#minlocationfailed" title="MinLocationFailed">MinLocationFailed</a>: <i>Double</i>
<a href="#monitorname" title="MonitorName">MonitorName</a>: <i>String</i>
<a href="#monitorpriority" title="MonitorPriority">MonitorPriority</a>: <i>Double</i>
<a href="#noscreenshot" title="NoScreenshot">NoScreenshot</a>: <i>Boolean</i>
<a href="#tickevery" title="TickEvery">TickEvery</a>: <i>Double</i>
<a href="#monitoroptions" title="MonitorOptions">MonitorOptions</a>: <i>
      - <a href="monitoroptionsdefinition.md">MonitorOptionsDefinition</a></i>
<a href="#retry" title="Retry">Retry</a>: <i>
      - <a href="retrydefinition.md">RetryDefinition</a></i>
</pre>

## Properties

#### AcceptSelfSigned

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowInsecure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowRedirects

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinFailureDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinLocationFailed

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorPriority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoScreenshot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TickEvery

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorOptions

_Required_: No

_Type_: List of <a href="monitoroptionsdefinition.md">MonitorOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retry

_Required_: No

_Type_: List of <a href="retrydefinition.md">RetryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

