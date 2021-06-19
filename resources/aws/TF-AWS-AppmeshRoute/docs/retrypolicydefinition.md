# TF::AWS::AppmeshRoute RetryPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#httpretryevents" title="HttpRetryEvents">HttpRetryEvents</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxretries" title="MaxRetries">MaxRetries</a>" : <i>Double</i>,
    "<a href="#tcpretryevents" title="TcpRetryEvents">TcpRetryEvents</a>" : <i>[ String, ... ]</i>,
    "<a href="#perretrytimeout" title="PerRetryTimeout">PerRetryTimeout</a>" : <i>[ <a href="perretrytimeoutdefinition.md">PerRetryTimeoutDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#httpretryevents" title="HttpRetryEvents">HttpRetryEvents</a>: <i>
      - String</i>
<a href="#maxretries" title="MaxRetries">MaxRetries</a>: <i>Double</i>
<a href="#tcpretryevents" title="TcpRetryEvents">TcpRetryEvents</a>: <i>
      - String</i>
<a href="#perretrytimeout" title="PerRetryTimeout">PerRetryTimeout</a>: <i>
      - <a href="perretrytimeoutdefinition.md">PerRetryTimeoutDefinition</a></i>
</pre>

## Properties

#### HttpRetryEvents

List of HTTP retry events.
Valid values: `client-error` (HTTP status code 409), `gateway-error` (HTTP status codes 502, 503, and 504), `server-error` (HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511), `stream-error` (retry on refused stream).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRetries

The maximum number of retries.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpRetryEvents

List of TCP retry events. The only valid value is `connection-error`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerRetryTimeout

_Required_: No

_Type_: List of <a href="perretrytimeoutdefinition.md">PerRetryTimeoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

