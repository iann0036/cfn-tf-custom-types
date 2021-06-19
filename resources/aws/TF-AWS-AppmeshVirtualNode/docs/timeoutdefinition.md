# TF::AWS::AppmeshVirtualNode TimeoutDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#grpc" title="Grpc">Grpc</a>" : <i>[ <a href="grpcdefinition.md">GrpcDefinition</a>, ... ]</i>,
    "<a href="#http" title="Http">Http</a>" : <i>[ <a href="httpdefinition.md">HttpDefinition</a>, ... ]</i>,
    "<a href="#http2" title="Http2">Http2</a>" : <i>[ <a href="http2definition.md">Http2Definition</a>, ... ]</i>,
    "<a href="#tcp" title="Tcp">Tcp</a>" : <i>[ <a href="tcpdefinition.md">TcpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#grpc" title="Grpc">Grpc</a>: <i>
      - <a href="grpcdefinition.md">GrpcDefinition</a></i>
<a href="#http" title="Http">Http</a>: <i>
      - <a href="httpdefinition.md">HttpDefinition</a></i>
<a href="#http2" title="Http2">Http2</a>: <i>
      - <a href="http2definition.md">Http2Definition</a></i>
<a href="#tcp" title="Tcp">Tcp</a>: <i>
      - <a href="tcpdefinition.md">TcpDefinition</a></i>
</pre>

## Properties

#### Grpc

_Required_: No

_Type_: List of <a href="grpcdefinition.md">GrpcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="httpdefinition.md">HttpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2

_Required_: No

_Type_: List of <a href="http2definition.md">Http2Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tcp

_Required_: No

_Type_: List of <a href="tcpdefinition.md">TcpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

