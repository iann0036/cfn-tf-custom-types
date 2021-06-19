# TF::AWS::AppmeshRoute SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#grpcroute" title="GrpcRoute">GrpcRoute</a>" : <i>[ <a href="grpcroutedefinition.md">GrpcRouteDefinition</a>, ... ]</i>,
    "<a href="#http2route" title="Http2Route">Http2Route</a>" : <i>[ <a href="http2routedefinition.md">Http2RouteDefinition</a>, ... ]</i>,
    "<a href="#httproute" title="HttpRoute">HttpRoute</a>" : <i>[ <a href="httproutedefinition.md">HttpRouteDefinition</a>, ... ]</i>,
    "<a href="#tcproute" title="TcpRoute">TcpRoute</a>" : <i>[ <a href="tcproutedefinition.md">TcpRouteDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#grpcroute" title="GrpcRoute">GrpcRoute</a>: <i>
      - <a href="grpcroutedefinition.md">GrpcRouteDefinition</a></i>
<a href="#http2route" title="Http2Route">Http2Route</a>: <i>
      - <a href="http2routedefinition.md">Http2RouteDefinition</a></i>
<a href="#httproute" title="HttpRoute">HttpRoute</a>: <i>
      - <a href="httproutedefinition.md">HttpRouteDefinition</a></i>
<a href="#tcproute" title="TcpRoute">TcpRoute</a>: <i>
      - <a href="tcproutedefinition.md">TcpRouteDefinition</a></i>
</pre>

## Properties

#### Priority

The priority for the route, between `0` and `1000`.
Routes are matched based on the specified value, where `0` is the highest priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrpcRoute

_Required_: No

_Type_: List of <a href="grpcroutedefinition.md">GrpcRouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2Route

_Required_: No

_Type_: List of <a href="http2routedefinition.md">Http2RouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRoute

_Required_: No

_Type_: List of <a href="httproutedefinition.md">HttpRouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpRoute

_Required_: No

_Type_: List of <a href="tcproutedefinition.md">TcpRouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

