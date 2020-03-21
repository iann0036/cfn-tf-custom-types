# Terraform::Kubernetes::Endpoints Subset

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>[ &lt;a href=&#34;subset-address.md&#34;&gt;Address&lt;/a&gt;, ... ]</i>,
    "<a href="#notreadyaddress" title="NotReadyAddress">NotReadyAddress</a>" : <i>[ &lt;a href=&#34;subset-notreadyaddress.md&#34;&gt;NotReadyAddress&lt;/a&gt;, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>[ &lt;a href=&#34;subset-port.md&#34;&gt;Port&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>
      - &lt;a href=&#34;subset-address.md&#34;&gt;Address&lt;/a&gt;</i>
<a href="#notreadyaddress" title="NotReadyAddress">NotReadyAddress</a>: <i>
      - &lt;a href=&#34;subset-notreadyaddress.md&#34;&gt;NotReadyAddress&lt;/a&gt;</i>
<a href="#port" title="Port">Port</a>: <i>
      - &lt;a href=&#34;subset-port.md&#34;&gt;Port&lt;/a&gt;</i>
</pre>

## Properties

#### Address

_Required_: No
_Type_: List of &lt;a href=&#34;subset-address.md&#34;&gt;Address&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotReadyAddress

_Required_: No
_Type_: List of &lt;a href=&#34;subset-notreadyaddress.md&#34;&gt;NotReadyAddress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No
_Type_: List of &lt;a href=&#34;subset-port.md&#34;&gt;Port&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

