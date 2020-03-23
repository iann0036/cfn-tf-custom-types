# Terraform::AWS::AppmeshRoute Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#httproute" title="HttpRoute">HttpRoute</a>" : <i>[ <a href="spec-httproute.md">HttpRoute</a>, ... ]</i>,
    "<a href="#tcproute" title="TcpRoute">TcpRoute</a>" : <i>[ <a href="spec-tcproute.md">TcpRoute</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#httproute" title="HttpRoute">HttpRoute</a>: <i>
      - <a href="spec-httproute.md">HttpRoute</a></i>
<a href="#tcproute" title="TcpRoute">TcpRoute</a>: <i>
      - <a href="spec-tcproute.md">TcpRoute</a></i>
</pre>

## Properties

#### Priority

The priority for the route, between `0` and `1000`.
Routes are matched based on the specified value, where `0` is the highest priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRoute

_Required_: No

_Type_: List of <a href="spec-httproute.md">HttpRoute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpRoute

_Required_: No

_Type_: List of <a href="spec-tcproute.md">TcpRoute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

