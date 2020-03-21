# Terraform::AWS::AppmeshRoute Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#httproute" title="HttpRoute">HttpRoute</a>" : <i>[ &lt;a href=&#34;spec-httproute.md&#34;&gt;HttpRoute&lt;/a&gt;, ... ]</i>,
    "<a href="#tcproute" title="TcpRoute">TcpRoute</a>" : <i>[ &lt;a href=&#34;spec-tcproute.md&#34;&gt;TcpRoute&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#httproute" title="HttpRoute">HttpRoute</a>: <i>
      - &lt;a href=&#34;spec-httproute.md&#34;&gt;HttpRoute&lt;/a&gt;</i>
<a href="#tcproute" title="TcpRoute">TcpRoute</a>: <i>
      - &lt;a href=&#34;spec-tcproute.md&#34;&gt;TcpRoute&lt;/a&gt;</i>
</pre>

## Properties

#### Priority

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRoute

_Required_: No
_Type_: List of &lt;a href=&#34;spec-httproute.md&#34;&gt;HttpRoute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpRoute

_Required_: No
_Type_: List of &lt;a href=&#34;spec-tcproute.md&#34;&gt;TcpRoute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

