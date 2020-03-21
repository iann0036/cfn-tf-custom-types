# Terraform::Kubernetes::Deployment InitContainer Lifecycle PreStop

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exec" title="Exec">Exec</a>" : <i>[ &lt;a href=&#34;initcontainer-lifecycle-prestop-exec.md&#34;&gt;Exec&lt;/a&gt;, ... ]</i>,
    "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>[ &lt;a href=&#34;initcontainer-lifecycle-prestop-httpget.md&#34;&gt;HttpGet&lt;/a&gt;, ... ]</i>,
    "<a href="#tcpsocket" title="TcpSocket">TcpSocket</a>" : <i>[ &lt;a href=&#34;initcontainer-lifecycle-prestop-tcpsocket.md&#34;&gt;TcpSocket&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exec" title="Exec">Exec</a>: <i>
      - &lt;a href=&#34;initcontainer-lifecycle-prestop-exec.md&#34;&gt;Exec&lt;/a&gt;</i>
<a href="#httpget" title="HttpGet">HttpGet</a>: <i>
      - &lt;a href=&#34;initcontainer-lifecycle-prestop-httpget.md&#34;&gt;HttpGet&lt;/a&gt;</i>
<a href="#tcpsocket" title="TcpSocket">TcpSocket</a>: <i>
      - &lt;a href=&#34;initcontainer-lifecycle-prestop-tcpsocket.md&#34;&gt;TcpSocket&lt;/a&gt;</i>
</pre>

## Properties

#### Exec

_Required_: No
_Type_: List of &lt;a href=&#34;initcontainer-lifecycle-prestop-exec.md&#34;&gt;Exec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

_Required_: No
_Type_: List of &lt;a href=&#34;initcontainer-lifecycle-prestop-httpget.md&#34;&gt;HttpGet&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpSocket

_Required_: No
_Type_: List of &lt;a href=&#34;initcontainer-lifecycle-prestop-tcpsocket.md&#34;&gt;TcpSocket&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

