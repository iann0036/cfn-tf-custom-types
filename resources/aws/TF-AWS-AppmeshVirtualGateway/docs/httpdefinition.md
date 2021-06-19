# TF::AWS::AppmeshVirtualGateway HttpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxconnections" title="MaxConnections">MaxConnections</a>" : <i>Double</i>,
    "<a href="#maxpendingrequests" title="MaxPendingRequests">MaxPendingRequests</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#maxconnections" title="MaxConnections">MaxConnections</a>: <i>Double</i>
<a href="#maxpendingrequests" title="MaxPendingRequests">MaxPendingRequests</a>: <i>Double</i>
</pre>

## Properties

#### MaxConnections

Maximum number of outbound TCP connections Envoy can establish concurrently with all hosts in upstream cluster. Minimum value of `1`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPendingRequests

Number of overflowing requests after `max_connections` Envoy will queue to upstream cluster. Minimum value of `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

