# Terraform::Kubernetes::Job Spec InitContainer LivenessProbe HttpGet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#host" title="Host">Host</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>,
    "<a href="#scheme" title="Scheme">Scheme</a>" : <i>String</i>,
    "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>[ &lt;a href=&#34;spec-initcontainer-livenessprobe-httpget-httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#host" title="Host">Host</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
<a href="#scheme" title="Scheme">Scheme</a>: <i>String</i>
<a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>
      - &lt;a href=&#34;spec-initcontainer-livenessprobe-httpget-httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;</i>
</pre>

## Properties

#### Host

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheme

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No
_Type_: List of &lt;a href=&#34;spec-initcontainer-livenessprobe-httpget-httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

