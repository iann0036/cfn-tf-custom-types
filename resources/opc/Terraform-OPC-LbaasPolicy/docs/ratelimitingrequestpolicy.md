# Terraform::OPC::LbaasPolicy RateLimitingRequestPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#burstsize" title="BurstSize">BurstSize</a>" : <i>Double</i>,
    "<a href="#delayexcessiverequests" title="DelayExcessiveRequests">DelayExcessiveRequests</a>" : <i>Boolean</i>,
    "<a href="#httperrorcode" title="HttpErrorCode">HttpErrorCode</a>" : <i>Double</i>,
    "<a href="#logginglevel" title="LoggingLevel">LoggingLevel</a>" : <i>String</i>,
    "<a href="#ratelimitingcriteria" title="RateLimitingCriteria">RateLimitingCriteria</a>" : <i>String</i>,
    "<a href="#requestspersecond" title="RequestsPerSecond">RequestsPerSecond</a>" : <i>Double</i>,
    "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
    "<a href="#zonememorysize" title="ZoneMemorySize">ZoneMemorySize</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#burstsize" title="BurstSize">BurstSize</a>: <i>Double</i>
<a href="#delayexcessiverequests" title="DelayExcessiveRequests">DelayExcessiveRequests</a>: <i>Boolean</i>
<a href="#httperrorcode" title="HttpErrorCode">HttpErrorCode</a>: <i>Double</i>
<a href="#logginglevel" title="LoggingLevel">LoggingLevel</a>: <i>String</i>
<a href="#ratelimitingcriteria" title="RateLimitingCriteria">RateLimitingCriteria</a>: <i>String</i>
<a href="#requestspersecond" title="RequestsPerSecond">RequestsPerSecond</a>: <i>Double</i>
<a href="#zone" title="Zone">Zone</a>: <i>String</i>
<a href="#zonememorysize" title="ZoneMemorySize">ZoneMemorySize</a>: <i>Double</i>
</pre>

## Properties

#### BurstSize

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelayExcessiveRequests

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpErrorCode

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingLevel

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimitingCriteria

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestsPerSecond

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneMemorySize

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

