# TF::AWS::AppmeshVirtualGateway Http2Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxrequests" title="MaxRequests">MaxRequests</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#maxrequests" title="MaxRequests">MaxRequests</a>: <i>Double</i>
</pre>

## Properties

#### MaxRequests

Maximum number of inflight requests Envoy can concurrently support across hosts in upstream cluster. Minimum value of `1`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

