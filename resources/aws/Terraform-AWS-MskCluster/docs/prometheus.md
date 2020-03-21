# Terraform::AWS::MskCluster Prometheus

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#jmxexporter" title="JmxExporter">JmxExporter</a>" : <i>[ &lt;a href=&#34;prometheus-jmxexporter.md&#34;&gt;JmxExporter&lt;/a&gt;, ... ]</i>,
    "<a href="#nodeexporter" title="NodeExporter">NodeExporter</a>" : <i>[ &lt;a href=&#34;prometheus-nodeexporter.md&#34;&gt;NodeExporter&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#jmxexporter" title="JmxExporter">JmxExporter</a>: <i>
      - &lt;a href=&#34;prometheus-jmxexporter.md&#34;&gt;JmxExporter&lt;/a&gt;</i>
<a href="#nodeexporter" title="NodeExporter">NodeExporter</a>: <i>
      - &lt;a href=&#34;prometheus-nodeexporter.md&#34;&gt;NodeExporter&lt;/a&gt;</i>
</pre>

## Properties

#### JmxExporter

_Required_: No
_Type_: List of &lt;a href=&#34;prometheus-jmxexporter.md&#34;&gt;JmxExporter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeExporter

_Required_: No
_Type_: List of &lt;a href=&#34;prometheus-nodeexporter.md&#34;&gt;NodeExporter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

