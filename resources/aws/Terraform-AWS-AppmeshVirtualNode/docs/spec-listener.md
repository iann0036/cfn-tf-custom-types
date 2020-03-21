# Terraform::AWS::AppmeshVirtualNode Spec Listener

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ &lt;a href=&#34;spec-listener-healthcheck.md&#34;&gt;HealthCheck&lt;/a&gt;, ... ]</i>,
    "<a href="#portmapping" title="PortMapping">PortMapping</a>" : <i>[ &lt;a href=&#34;spec-listener-portmapping.md&#34;&gt;PortMapping&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - &lt;a href=&#34;spec-listener-healthcheck.md&#34;&gt;HealthCheck&lt;/a&gt;</i>
<a href="#portmapping" title="PortMapping">PortMapping</a>: <i>
      - &lt;a href=&#34;spec-listener-portmapping.md&#34;&gt;PortMapping&lt;/a&gt;</i>
</pre>

## Properties

#### HealthCheck

_Required_: No
_Type_: List of &lt;a href=&#34;spec-listener-healthcheck.md&#34;&gt;HealthCheck&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortMapping

_Required_: No
_Type_: List of &lt;a href=&#34;spec-listener-portmapping.md&#34;&gt;PortMapping&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

