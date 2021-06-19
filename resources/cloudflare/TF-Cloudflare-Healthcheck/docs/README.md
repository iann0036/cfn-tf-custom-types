# TF::Cloudflare::Healthcheck

Standalone Health Checks provide a way to monitor origin servers without needing a Cloudflare Load Balancer.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::Healthcheck",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#allowinsecure" title="AllowInsecure">AllowInsecure</a>" : <i>Boolean</i>,
        "<a href="#checkregions" title="CheckRegions">CheckRegions</a>" : <i>[ String, ... ]</i>,
        "<a href="#consecutivefails" title="ConsecutiveFails">ConsecutiveFails</a>" : <i>Double</i>,
        "<a href="#consecutivesuccesses" title="ConsecutiveSuccesses">ConsecutiveSuccesses</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#expectedbody" title="ExpectedBody">ExpectedBody</a>" : <i>String</i>,
        "<a href="#expectedcodes" title="ExpectedCodes">ExpectedCodes</a>" : <i>[ String, ... ]</i>,
        "<a href="#followredirects" title="FollowRedirects">FollowRedirects</a>" : <i>Boolean</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationemailaddresses" title="NotificationEmailAddresses">NotificationEmailAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#notificationsuspended" title="NotificationSuspended">NotificationSuspended</a>" : <i>Boolean</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#retries" title="Retries">Retries</a>" : <i>Double</i>,
        "<a href="#suspended" title="Suspended">Suspended</a>" : <i>Boolean</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#header" title="Header">Header</a>" : <i>[ <a href="headerdefinition.md">HeaderDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::Healthcheck
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#allowinsecure" title="AllowInsecure">AllowInsecure</a>: <i>Boolean</i>
    <a href="#checkregions" title="CheckRegions">CheckRegions</a>: <i>
      - String</i>
    <a href="#consecutivefails" title="ConsecutiveFails">ConsecutiveFails</a>: <i>Double</i>
    <a href="#consecutivesuccesses" title="ConsecutiveSuccesses">ConsecutiveSuccesses</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#expectedbody" title="ExpectedBody">ExpectedBody</a>: <i>String</i>
    <a href="#expectedcodes" title="ExpectedCodes">ExpectedCodes</a>: <i>
      - String</i>
    <a href="#followredirects" title="FollowRedirects">FollowRedirects</a>: <i>Boolean</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationemailaddresses" title="NotificationEmailAddresses">NotificationEmailAddresses</a>: <i>
      - String</i>
    <a href="#notificationsuspended" title="NotificationSuspended">NotificationSuspended</a>: <i>Boolean</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#retries" title="Retries">Retries</a>: <i>Double</i>
    <a href="#suspended" title="Suspended">Suspended</a>: <i>Boolean</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#header" title="Header">Header</a>: <i>
      - <a href="headerdefinition.md">HeaderDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Address

The hostname or IP address of the origin server to run health checks on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowInsecure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckRegions

A list of regions from which to run health checks. If not set Cloudflare will pick a default region. Valid values: `WNAM`, `ENAM`, `WEU`, `EEU`, `NSAM`, `SSAM`, `OC`, `ME`, `NAF`, `SAF`, `IN`, `SEAS`, `NEAS`, `ALL_REGIONS`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsecutiveFails

The number of consecutive fails required from a health check before changing the health to unhealthy. (Default: `1`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsecutiveSuccesses

The number of consecutive successes required from a health check before changing the health to healthy. (Default: `1`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-readable description of the health check.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedCodes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowRedirects

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations. (Default: `60`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEmailAddresses

A list of email addresses we want to send the notifications to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationSuspended

Whether the notifications are suspended or not. Useful for maintenance periods. Valid values: `true` or `false` (Default: `false`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port number to connect to for the health check.  Valid values are in the range `0-65535` (Default: `80`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retries

The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. (Default: `2`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Suspended

If suspended, no health checks are sent to the origin. Valid values: `true` or `false` (Default: `false`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

The timeout (in seconds) before marking the health check as failed. (Default: `5`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The protocol to use for the health check. Valid values: `HTTP`, `HTTPS`, `TCP`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The DNS zone ID to which apply settings.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="headerdefinition.md">HeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedOn

Returns the <code>CreatedOn</code> value.

#### Id

Returns the <code>Id</code> value.

#### ModifiedOn

Returns the <code>ModifiedOn</code> value.

