# TF::Checkly::Check

`checkly_check` allows users to manage checkly checks. Add a `checkly_check` resource to your resource file.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Checkly::Check",
    "Properties" : {
        "<a href="#activated" title="Activated">Activated</a>" : <i>Boolean</i>,
        "<a href="#degradedresponsetime" title="DegradedResponseTime">DegradedResponseTime</a>" : <i>Double</i>,
        "<a href="#doublecheck" title="DoubleCheck">DoubleCheck</a>" : <i>Boolean</i>,
        "<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>" : <i>[ <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>, ... ]</i>,
        "<a href="#frequency" title="Frequency">Frequency</a>" : <i>Double</i>,
        "<a href="#frequencyoffset" title="FrequencyOffset">FrequencyOffset</a>" : <i>Double</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>Double</i>,
        "<a href="#grouporder" title="GroupOrder">GroupOrder</a>" : <i>Double</i>,
        "<a href="#localsetupscript" title="LocalSetupScript">LocalSetupScript</a>" : <i>String</i>,
        "<a href="#localteardownscript" title="LocalTeardownScript">LocalTeardownScript</a>" : <i>String</i>,
        "<a href="#locations" title="Locations">Locations</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxresponsetime" title="MaxResponseTime">MaxResponseTime</a>" : <i>Double</i>,
        "<a href="#muted" title="Muted">Muted</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#script" title="Script">Script</a>" : <i>String</i>,
        "<a href="#setupsnippetid" title="SetupSnippetId">SetupSnippetId</a>" : <i>Double</i>,
        "<a href="#shouldfail" title="ShouldFail">ShouldFail</a>" : <i>Boolean</i>,
        "<a href="#sslcheck" title="SslCheck">SslCheck</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#teardownsnippetid" title="TeardownSnippetId">TeardownSnippetId</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#useglobalalertsettings" title="UseGlobalAlertSettings">UseGlobalAlertSettings</a>" : <i>Boolean</i>,
        "<a href="#alertchannelsubscription" title="AlertChannelSubscription">AlertChannelSubscription</a>" : <i>[ <a href="alertchannelsubscriptiondefinition.md">AlertChannelSubscriptionDefinition</a>, ... ]</i>,
        "<a href="#alertsettings" title="AlertSettings">AlertSettings</a>" : <i>[ <a href="alertsettingsdefinition.md">AlertSettingsDefinition</a>, ... ]</i>,
        "<a href="#request" title="Request">Request</a>" : <i>[ <a href="requestdefinition.md">RequestDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Checkly::Check
Properties:
    <a href="#activated" title="Activated">Activated</a>: <i>Boolean</i>
    <a href="#degradedresponsetime" title="DegradedResponseTime">DegradedResponseTime</a>: <i>Double</i>
    <a href="#doublecheck" title="DoubleCheck">DoubleCheck</a>: <i>Boolean</i>
    <a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>: <i>
      - <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a></i>
    <a href="#frequency" title="Frequency">Frequency</a>: <i>Double</i>
    <a href="#frequencyoffset" title="FrequencyOffset">FrequencyOffset</a>: <i>Double</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>Double</i>
    <a href="#grouporder" title="GroupOrder">GroupOrder</a>: <i>Double</i>
    <a href="#localsetupscript" title="LocalSetupScript">LocalSetupScript</a>: <i>String</i>
    <a href="#localteardownscript" title="LocalTeardownScript">LocalTeardownScript</a>: <i>String</i>
    <a href="#locations" title="Locations">Locations</a>: <i>
      - String</i>
    <a href="#maxresponsetime" title="MaxResponseTime">MaxResponseTime</a>: <i>Double</i>
    <a href="#muted" title="Muted">Muted</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#script" title="Script">Script</a>: <i>String</i>
    <a href="#setupsnippetid" title="SetupSnippetId">SetupSnippetId</a>: <i>Double</i>
    <a href="#shouldfail" title="ShouldFail">ShouldFail</a>: <i>Boolean</i>
    <a href="#sslcheck" title="SslCheck">SslCheck</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#teardownsnippetid" title="TeardownSnippetId">TeardownSnippetId</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#useglobalalertsettings" title="UseGlobalAlertSettings">UseGlobalAlertSettings</a>: <i>Boolean</i>
    <a href="#alertchannelsubscription" title="AlertChannelSubscription">AlertChannelSubscription</a>: <i>
      - <a href="alertchannelsubscriptiondefinition.md">AlertChannelSubscriptionDefinition</a></i>
    <a href="#alertsettings" title="AlertSettings">AlertSettings</a>: <i>
      - <a href="alertsettingsdefinition.md">AlertSettingsDefinition</a></i>
    <a href="#request" title="Request">Request</a>: <i>
      - <a href="requestdefinition.md">RequestDefinition</a></i>
</pre>

## Properties

#### Activated

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DegradedResponseTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DoubleCheck

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariables

_Required_: No

_Type_: List of <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Frequency

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrequencyOffset

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupOrder

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSetupScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalTeardownScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locations

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxResponseTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Muted

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the check.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetupSnippetId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldFail

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCheck

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeardownSnippetId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the check. Possible values are `API`, and `BROWSER`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseGlobalAlertSettings

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertChannelSubscription

_Required_: No

_Type_: List of <a href="alertchannelsubscriptiondefinition.md">AlertChannelSubscriptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertSettings

_Required_: No

_Type_: List of <a href="alertsettingsdefinition.md">AlertSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of <a href="requestdefinition.md">RequestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

