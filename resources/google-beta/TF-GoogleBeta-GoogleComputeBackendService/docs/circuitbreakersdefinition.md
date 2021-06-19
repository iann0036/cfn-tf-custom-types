# TF::GoogleBeta::GoogleComputeBackendService CircuitBreakersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxconnections" title="MaxConnections">MaxConnections</a>" : <i>Double</i>,
    "<a href="#maxpendingrequests" title="MaxPendingRequests">MaxPendingRequests</a>" : <i>Double</i>,
    "<a href="#maxrequests" title="MaxRequests">MaxRequests</a>" : <i>Double</i>,
    "<a href="#maxrequestsperconnection" title="MaxRequestsPerConnection">MaxRequestsPerConnection</a>" : <i>Double</i>,
    "<a href="#maxretries" title="MaxRetries">MaxRetries</a>" : <i>Double</i>,
    "<a href="#connecttimeout" title="ConnectTimeout">ConnectTimeout</a>" : <i>[ <a href="connecttimeoutdefinition.md">ConnectTimeoutDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxconnections" title="MaxConnections">MaxConnections</a>: <i>Double</i>
<a href="#maxpendingrequests" title="MaxPendingRequests">MaxPendingRequests</a>: <i>Double</i>
<a href="#maxrequests" title="MaxRequests">MaxRequests</a>: <i>Double</i>
<a href="#maxrequestsperconnection" title="MaxRequestsPerConnection">MaxRequestsPerConnection</a>: <i>Double</i>
<a href="#maxretries" title="MaxRetries">MaxRetries</a>: <i>Double</i>
<a href="#connecttimeout" title="ConnectTimeout">ConnectTimeout</a>: <i>
      - <a href="connecttimeoutdefinition.md">ConnectTimeoutDefinition</a></i>
</pre>

## Properties

#### MaxConnections

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPendingRequests

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRequests

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRequestsPerConnection

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRetries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectTimeout

_Required_: No

_Type_: List of <a href="connecttimeoutdefinition.md">ConnectTimeoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

