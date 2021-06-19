# TF::FortiOS::SystemAlarm GroupsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminauthfailurethreshold" title="AdminAuthFailureThreshold">AdminAuthFailureThreshold</a>" : <i>Double</i>,
    "<a href="#adminauthlockoutthreshold" title="AdminAuthLockoutThreshold">AdminAuthLockoutThreshold</a>" : <i>Double</i>,
    "<a href="#decryptionfailurethreshold" title="DecryptionFailureThreshold">DecryptionFailureThreshold</a>" : <i>Double</i>,
    "<a href="#encryptionfailurethreshold" title="EncryptionFailureThreshold">EncryptionFailureThreshold</a>" : <i>Double</i>,
    "<a href="#fwpolicyid" title="FwPolicyId">FwPolicyId</a>" : <i>Double</i>,
    "<a href="#fwpolicyidthreshold" title="FwPolicyIdThreshold">FwPolicyIdThreshold</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#logfullwarningthreshold" title="LogFullWarningThreshold">LogFullWarningThreshold</a>" : <i>Double</i>,
    "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
    "<a href="#replayattemptthreshold" title="ReplayAttemptThreshold">ReplayAttemptThreshold</a>" : <i>Double</i>,
    "<a href="#selftestfailurethreshold" title="SelfTestFailureThreshold">SelfTestFailureThreshold</a>" : <i>Double</i>,
    "<a href="#userauthfailurethreshold" title="UserAuthFailureThreshold">UserAuthFailureThreshold</a>" : <i>Double</i>,
    "<a href="#userauthlockoutthreshold" title="UserAuthLockoutThreshold">UserAuthLockoutThreshold</a>" : <i>Double</i>,
    "<a href="#fwpolicyviolations" title="FwPolicyViolations">FwPolicyViolations</a>" : <i>[ <a href="fwpolicyviolationsdefinition.md">FwPolicyViolationsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#adminauthfailurethreshold" title="AdminAuthFailureThreshold">AdminAuthFailureThreshold</a>: <i>Double</i>
<a href="#adminauthlockoutthreshold" title="AdminAuthLockoutThreshold">AdminAuthLockoutThreshold</a>: <i>Double</i>
<a href="#decryptionfailurethreshold" title="DecryptionFailureThreshold">DecryptionFailureThreshold</a>: <i>Double</i>
<a href="#encryptionfailurethreshold" title="EncryptionFailureThreshold">EncryptionFailureThreshold</a>: <i>Double</i>
<a href="#fwpolicyid" title="FwPolicyId">FwPolicyId</a>: <i>Double</i>
<a href="#fwpolicyidthreshold" title="FwPolicyIdThreshold">FwPolicyIdThreshold</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#logfullwarningthreshold" title="LogFullWarningThreshold">LogFullWarningThreshold</a>: <i>Double</i>
<a href="#period" title="Period">Period</a>: <i>Double</i>
<a href="#replayattemptthreshold" title="ReplayAttemptThreshold">ReplayAttemptThreshold</a>: <i>Double</i>
<a href="#selftestfailurethreshold" title="SelfTestFailureThreshold">SelfTestFailureThreshold</a>: <i>Double</i>
<a href="#userauthfailurethreshold" title="UserAuthFailureThreshold">UserAuthFailureThreshold</a>: <i>Double</i>
<a href="#userauthlockoutthreshold" title="UserAuthLockoutThreshold">UserAuthLockoutThreshold</a>: <i>Double</i>
<a href="#fwpolicyviolations" title="FwPolicyViolations">FwPolicyViolations</a>: <i>
      - <a href="fwpolicyviolationsdefinition.md">FwPolicyViolationsDefinition</a></i>
</pre>

## Properties

#### AdminAuthFailureThreshold

Admin authentication failure threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminAuthLockoutThreshold

Admin authentication lockout threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DecryptionFailureThreshold

Decryption failure threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionFailureThreshold

Encryption failure threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FwPolicyId

Firewall policy ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FwPolicyIdThreshold

Firewall policy ID threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Group ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogFullWarningThreshold

Log full warning threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

Time period in seconds (0 = from start up).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplayAttemptThreshold

Replay attempt threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelfTestFailureThreshold

Self-test failure threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAuthFailureThreshold

User authentication failure threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAuthLockoutThreshold

User authentication lockout threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FwPolicyViolations

_Required_: No

_Type_: List of <a href="fwpolicyviolationsdefinition.md">FwPolicyViolationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

