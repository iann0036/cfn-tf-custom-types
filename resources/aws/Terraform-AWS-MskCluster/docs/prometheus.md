# Terraform::AWS::MskCluster Prometheus

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#jmxexporter" title="JmxExporter">JmxExporter</a>" : <i>[ <a href="prometheus-jmxexporter.md">JmxExporter</a>, ... ]</i>,
    "<a href="#nodeexporter" title="NodeExporter">NodeExporter</a>" : <i>[ <a href="prometheus-nodeexporter.md">NodeExporter</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#jmxexporter" title="JmxExporter">JmxExporter</a>: <i>
      - <a href="prometheus-jmxexporter.md">JmxExporter</a></i>
<a href="#nodeexporter" title="NodeExporter">NodeExporter</a>: <i>
      - <a href="prometheus-nodeexporter.md">NodeExporter</a></i>
</pre>

## Properties

#### JmxExporter

_Required_: No

_Type_: List of <a href="prometheus-jmxexporter.md">JmxExporter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeExporter

_Required_: No

_Type_: List of <a href="prometheus-nodeexporter.md">NodeExporter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

