# Terraform::AWS::AppmeshVirtualNode Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backends" title="Backends">Backends</a>" : <i>[ String, ... ]</i>,
    "<a href="#backend" title="Backend">Backend</a>" : <i>[ &lt;a href=&#34;spec-backend.md&#34;&gt;Backend&lt;/a&gt;, ... ]</i>,
    "<a href="#listener" title="Listener">Listener</a>" : <i>[ &lt;a href=&#34;spec-listener.md&#34;&gt;Listener&lt;/a&gt;, ... ]</i>,
    "<a href="#logging" title="Logging">Logging</a>" : <i>[ &lt;a href=&#34;spec-logging.md&#34;&gt;Logging&lt;/a&gt;, ... ]</i>,
    "<a href="#servicediscovery" title="ServiceDiscovery">ServiceDiscovery</a>" : <i>[ &lt;a href=&#34;spec-servicediscovery.md&#34;&gt;ServiceDiscovery&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backends" title="Backends">Backends</a>: <i>
      - String</i>
<a href="#backend" title="Backend">Backend</a>: <i>
      - &lt;a href=&#34;spec-backend.md&#34;&gt;Backend&lt;/a&gt;</i>
<a href="#listener" title="Listener">Listener</a>: <i>
      - &lt;a href=&#34;spec-listener.md&#34;&gt;Listener&lt;/a&gt;</i>
<a href="#logging" title="Logging">Logging</a>: <i>
      - &lt;a href=&#34;spec-logging.md&#34;&gt;Logging&lt;/a&gt;</i>
<a href="#servicediscovery" title="ServiceDiscovery">ServiceDiscovery</a>: <i>
      - &lt;a href=&#34;spec-servicediscovery.md&#34;&gt;ServiceDiscovery&lt;/a&gt;</i>
</pre>

## Properties

#### Backends

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No
_Type_: List of &lt;a href=&#34;spec-backend.md&#34;&gt;Backend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No
_Type_: List of &lt;a href=&#34;spec-listener.md&#34;&gt;Listener&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No
_Type_: List of &lt;a href=&#34;spec-logging.md&#34;&gt;Logging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDiscovery

_Required_: No
_Type_: List of &lt;a href=&#34;spec-servicediscovery.md&#34;&gt;ServiceDiscovery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

