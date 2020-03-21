# Terraform::FlexibleEngine::MrsClusterV1 ComponentList

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#componentname" title="ComponentName">ComponentName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#componentname" title="ComponentName">ComponentName</a>: <i>String</i>
</pre>

## Properties

#### ComponentName

Component name Currently, Hadoop, Spark, HBase,
Hive, Hue, Loader, Flume, Kafka and Storm are supported. Loader and Flume are
not supported by MRS 1.3.0.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

