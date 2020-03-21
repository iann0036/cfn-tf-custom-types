# Terraform::Kubernetes::Job Lifecycle PostStart

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exec" title="Exec">Exec</a>" : <i>[ <a href="lifecycle-poststart-exec.md">Exec</a>, ... ]</i>,
    "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>[ <a href="lifecycle-poststart-httpget.md">HttpGet</a>, ... ]</i>,
    "<a href="#tcpsocket" title="TcpSocket">TcpSocket</a>" : <i>[ <a href="lifecycle-poststart-tcpsocket.md">TcpSocket</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exec" title="Exec">Exec</a>: <i>
      - <a href="lifecycle-poststart-exec.md">Exec</a></i>
<a href="#httpget" title="HttpGet">HttpGet</a>: <i>
      - <a href="lifecycle-poststart-httpget.md">HttpGet</a></i>
<a href="#tcpsocket" title="TcpSocket">TcpSocket</a>: <i>
      - <a href="lifecycle-poststart-tcpsocket.md">TcpSocket</a></i>
</pre>

## Properties

#### Exec

_Required_: No

_Type_: List of <a href="lifecycle-poststart-exec.md">Exec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

_Required_: No

_Type_: List of <a href="lifecycle-poststart-httpget.md">HttpGet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpSocket

_Required_: No

_Type_: List of <a href="lifecycle-poststart-tcpsocket.md">TcpSocket</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

